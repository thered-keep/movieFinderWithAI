function getOverview(movieTitle) {
    // Make an asynchronous request to your Flask backend
    fetch(`/getOverview?title=${encodeURIComponent(movieTitle)}`)
        .then(response => response.json())
        .then(data => {
            // Update the content of the 'actorsContainer' element with the list of actors
            const overviewContainer = document.getElementById('overviewContainer');
            const overview = data.overview;
            const img = data.img
            overviewContainer.innerHTML =
                `<div class="content">
                            <div class="overview-title" >
                                <h3>Movie Overview :</h3>
                            </div>
                            <p>${overview}</p>
                            <img src="${img}" class="movie-img">
                        </div>`;


        })
        .catch(error => console.error('Error:', error));
}
