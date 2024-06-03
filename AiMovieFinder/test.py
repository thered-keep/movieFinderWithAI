import pandas as pd

def search_overview(title) -> list:
    global df
    movie_index = df[df['Title'] == title].index[0]
    movie_overview = df.iloc[movie_index, 2]
    movie_img = df.iloc[movie_index, 8]
    movie_data = {
        'overview': movie_overview,
        'img': movie_img
    }
    return movie_data




def delete_half_of_csv(input_file, output_file):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(input_file)

    # Calculate the number of rows to delete
    num_rows_to_delete = len(df) // 2

    # Delete the first half of the rows
    remaining_rows = df.iloc[num_rows_to_delete:]

    # Write the remaining rows to the output CSV file
    remaining_rows.to_csv(output_file, index=False)


# Specify the input and output file paths
input_file_path = 'updatedMovies.csv'
output_file_path = 'updatedMovies.csv'

# Call the function to delete half of the CSV file
delete_half_of_csv(input_file_path, output_file_path)

print("Half of the CSV file has been deleted using pandas.")
if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=5000)
    df = pd.read_csv('mymoviedb.csv')
    print(search_overview("The Batman")["img"])
    #delete_half_of_csv(input_file_path, output_file_path)