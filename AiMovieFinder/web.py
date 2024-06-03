from flask import Flask, render_template, request
from flask import jsonify
from recommendations_model import before_serevr_ready
import pandas as pd
from recommendations_model import load_data, recommend

app = Flask(__name__)

nn_model, movies = before_serevr_ready()
# Initialize variables to store search type and query
search_query = ""
df = pd.read_csv('mymoviedb.csv')


def search_overview(title) -> str:
    global df
    movie_index = df[df['Title'] == title].index[0]
    movie_overview = df.iloc[movie_index, 2]
    movie_img = df.iloc[movie_index, 8]
    movie_data = {
        'overview': movie_overview,
        'img': movie_img
    }
    return movie_data


def recommended_titles(title) -> list:
    return recommend(title, nn_model, movies)


@app.route("/getOverview")
def getOverview():
    title = request.args.get("title")
    overview = search_overview(title)
    return jsonify(overview)


# Define routes
@app.route("/")
def index():
    return render_template("index.html", title="Find The Movie with AI")


@app.route("/search", methods=["POST"])
def search():
    global search_query
    search_result = []
    # Get the search type and query from the form
    search_query = request.form["search_query"]
    print("search_query"+" "+search_query)

    print("searching title")
    rec_movies = recommended_titles(search_query)
    search_result = rec_movies
    print(rec_movies)


    return render_template("index.html", title="Find The Movie with AI",search_result=search_result)


# Run the Flask app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
