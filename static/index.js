function submitMovie(id,name=null,language=null){
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
    var lang = language;
    if (lang == null){
      lang = "English";
    }
    console.log(lang);

    // Sending data to backend
    fetch('/process', {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({movie: movie, lang:lang})
    })

    .then(response => response.json())
    .then(data => {
      console.log(data)
      eng_cols = {"name":"Name of Movie","sentiment":"Sentiment", "release":"Released date", "genre":"Genre", "cast":"Actors", "director":"Director", "plot":"Plot","imdb":"IMDb Rating"}
      hin_cols = {"name":"फिल्म का नाम","sentiment":"भाव", "release":"विमोचन तिथि", "genre":"शैली", "cast":"अभिनेताओं", "director":"निदेशक", "plot":"कहानी","imdb":"IMDb पर रेटिंग"}
      var eng = `
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
          <td id="col1">${eng_cols.name}</td>
          <td id="col2">${data.title}</td>
        </tr>
        <tr id="even">
          <td id="col1">${eng_cols.sentiment}</td>
          <td id="col2" class="sentiment" style="color:${data.color}">${data.sentiment} ${data.percentage}</td>
        </tr>
        <tr id="odd">
          <td id="col1">${eng_cols.release}</td>
          <td id="col2">${data.release_year}</td>
        </tr>
        <tr id="even">
          <td id="col1">${eng_cols.genre}</td>
          <td id="col2">${data.genre}</td>
        </tr>
        <tr id="odd">
          <td id="col1">${eng_cols.cast}</td>
          <td id="col2">${data.cast}</td>
        </tr>
        <tr id="even">
          <td id="col1">${eng_cols.director}</td>
          <td id="col2">${data.director}</td>
        </tr>
        <tr id="odd">
          <td id="col1">${eng_cols.plot}</td>
          <td id="col2">${data.plot}</td>
        </tr>
        <tr id="even">
          <td id="col1">${eng_cols.imdb}</td>
          <td id="col2">${data.imdbRating} ⭐</td>
        </tr>
      </tbody>
    </table>
      `;

      var hin = `
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
          <td id="col1">${hin_cols.name}</td>
          <td id="col2">${data.title}</td>
        </tr>
        <tr id="even">
          <td id="col1">${hin_cols.sentiment}</td>
          <td id="col2" class="sentiment" style="color:${data.color}">${data.sentiment} ${data.percentage}</td>
        </tr>
        <tr id="odd">
          <td id="col1">${hin_cols.release}</td>
          <td id="col2">${data.release_year}</td>
        </tr>
        <tr id="even">
          <td id="col1">${hin_cols.genre}</td>
          <td id="col2">${data.genre}</td>
        </tr>
        <tr id="odd">
          <td id="col1">${hin_cols.cast}</td>
          <td id="col2">${data.cast}</td>
        </tr>
        <tr id="even">
          <td id="col1">${hin_cols.director}</td>
          <td id="col2">${data.director}</td>
        </tr>
        <tr id="odd">
          <td id="col1">${hin_cols.plot}</td>
          <td id="col2">${data.plot}</td>
        </tr>
        <tr id="even">
          <td id="col1">${hin_cols.imdb}</td>
          <td id="col2">${data.imdbRating} ⭐</td>
        </tr>
      </tbody>
    </table>
      `;
      if(lang == "English"){
        document.getElementById("container").innerHTML = eng;
      }
      else if(lang == "Hindi"){
        document.getElementById("container").innerHTML = hin;
      }
      
      })

    .catch(error => {
        console.error("Error", error);
    })
}
