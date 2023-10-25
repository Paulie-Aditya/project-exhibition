function submitMovie(id,name=null){
    console.log("Function called")
    if(id == "movie-id"){
      var movie = name;
    }
    if(id == "movie"){
      var movie = document.getElementById("movie").value;
      if (!movie){
        return;
      }
    }
    
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
      console.log(data)
      var s = `
      <h2 id="movie-name" align="center">${data.title}</h2>


      <table id="table">
      <tbody>
        <tr>
          <td id="movie-name">${(data.title)} </td>
          <td id="col2">
            <img src="${data.poster_url}" alt="${data.title}" />
          </td>
        </tr>
        <tr id="odd">
          <td id="col1">Movie Name</td>
          <td id="col2">${data.title}</td>
        </tr>
        <tr id="even">
          <td id="col1">Sentiment</td>
          <td id="col2" class="sentiment" style="color:${data.color}">${data.sentiment} ${data.percentage}</td>
        </tr>
        <tr id="odd">
          <td id="col1">Released date</td>
          <td id="col2">${data.release_year}</td>
        </tr>
        <tr id="even">
          <td id="col1">Genre</td>
          <td id="col2">${data.genre}</td>
        </tr>
        <tr id="odd">
          <td id="col1">Actors</td>
          <td id="col2">${data.cast}</td>
        </tr>
        <tr id="even">
          <td id="col1">Director</td>
          <td id="col2">${data.director}</td>
        </tr>
        <tr id="odd">
          <td id="col1">Plot</td>
          <td id="col2">${data.plot}</td>
        </tr>
        <tr id="even">
          <td id="col1">IMDb Rating</td>
          <td id="col2">${data.imdbRating} ⭐</td>
        </tr>
      </tbody>
    </table>
      `;
      document.getElementById("container").innerHTML = s;
      })

    .catch(error => {
        console.error("Error", error);
    })
}
