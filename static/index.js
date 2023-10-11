function submitMovie(){
    console.log("Function called")
    var movie = document.getElementById("movie").value;
    console.log(movie);

    // Sending data to backend
    fetch('/process', {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({movie: movie})
    })

    .then(response => response.json())
    .then(data => {
          var s = `
          <h2 align="center">Movie: ${data.title}</h2>

          <table border="2">
          <tbody>
            <tr>
              <td>Movie Name</td>
              <td>${data.title}</td>
            </tr>
            <tr>
              <td>Sentiment</td>
              <td>${data.sentiment} ${data.percentage}</td>
            </tr>
            <tr>
              <td>Released date</td>
              <td>${data.release_year}</td>
            </tr>
            <tr>
              <td>Genre</td>
              <td>${data.genre}</td>
            </tr>
            <tr>
              <td>Actors</td>
              <td>${data.cast}</td>
            </tr>
            <tr>
              <td>Director</td>
              <td>${data.director}</td>
            </tr>
            <tr>
              <td>Plot</td>
              <td>${data.plot}</td>
            </tr>
            <tr>
              <td>Poster</td>
              <td>
                <img src=${data.poster_url} alt=${data.title} />
              </td>
            </tr>
            <tr>
              <td>IMDb Rating</td>
              <td>${data.imdbRating}</td>
            </tr>
          </tbody>
        </table>
        `;
      document.getElementById("container").innerHTML = s;
      })
    /*
    .then(data => {
        // Handling Response from Backend
        console.log(data);
        
        handle_data(JSON.stringify(data));
        //console.log(data);
        
    })
    */

    .catch(error => {
        console.error("Error", error);
    })
}

/*
async function handle_data(data) {
    console.log("handling");
    let movie_data = JSON.parse(data);
    const container = document.querySelector("container")
    document.getElementById("img").innerHTML = movie_data.poster_url
    //container.getElementById("img").innerHTML = 
    /*fetch('/redirect-movie',{
        method: "GET"
    })

    .then(response=>  window.location.replace(response.url))
    
    .catch(error => {
        console.error("Error", error);
    })
    
   
}*/
