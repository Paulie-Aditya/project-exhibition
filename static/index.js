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
        // Handling Response from Backend
        console.log(data);
        handle_data(data);
        //console.log(data);
        
    })

    .catch(error => {
        console.error("Error", error);
    })
}

function handle_data(data) {
    console.log("handling");
    //document = "movie.html"
    //document.getElementById("title").innerHTML = data['title']
    fetch('/redirect-movie',{
        method: "GET"
    })
    .then(response=>  window.location.replace(response.url))
    .catch(error => {
        console.error("Error", error);
    })
   
}