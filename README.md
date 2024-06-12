
# Movie Finder App

The Movie Finder App helps you discover the 10 most similar movies based on the title of a movie you provide. It leverages TensorFlow's Universal Sentence Encoder to transform movie titles into numerical vectors and uses K-Nearest Neighbors (KNN) to find the nearest movies.
## Features

- **Movie Search**: Find the top 10 movies similar to the movie title you enter.
- **Movie Overview**: Get the overview and image of the searched movie.
- **Web Interface**: User-friendly web interface built with Flask.

## Technology Stack

- **Backend**: Flask and Python
- **Frontend**: html ,javascript and css
- **Text Encoder**: TensorFlow Universal Sentence Encoder 
- **Machine Learning Algorithm**: K-Nearest Neighbors (KNN)

## Endpoints
### `/getOverview`
- **Method**: GET
- **Parameters**: 
  - `title` (str) - Title of the movie
-**returns**: overivew of the movie in json
### `/`
- **Method**: GET
-**returns**: the html template of the main page

### `/search`
- **Method**: POST
- **Parameters**:
  - `search_query` (str) - The movie title to search for
-**returns**: the rendered html template with the found movies list

## Installation Guide

### Prerequisites

- TensorFlow
- Flask
- versions and other dependencies specified in `requirements.txt`

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/moviefinder.git
   cd AiMovieFinder
   ```
2. **Run the web.py script**
