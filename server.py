from flask import Flask, request, jsonify, render_template, redirect
import json 

import script

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def home():
    #return render_template('index.html')
    return render_template('new.html')


@app.route('/process', methods = ['POST'])
def process():
    data = request.get_json()
    movie = data['movie']
    response = script.sentiment_analysis(movie)
    #redirect("/movie")
    out_file = open("sample.json", "w") 
    json.dump(response, out_file)
    return jsonify(response)


@app.route("/login", methods = ['GET'])
def login():
    return render_template('login.html')

@app.route("/register", methods = ["GET"])
def register():
    return render_template("register.html")
'''

@app.route("/movie", methods = ["GET"])
def movie():
    return render_template("movie.html")
    #return redirect(location= "/movie",Response= render_template("movie.html"))

@app.route("/redirect-movie", methods=["GET"])
def redirect_movie():
    return redirect(location="/movie", code= 302)
'''

if __name__ == "__main__":
    app.run(debug=True)