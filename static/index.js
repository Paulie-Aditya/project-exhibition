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
        
    })

    .catch(error => {
        console.error("Error", error);
    })
}