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
    lang = data['lang']
    response = script.sentiment_analysis(movie, language=lang)
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

@app.route("/hindi", methods = ["GET"])
def hindi():
    return render_template("hindi.html")

if __name__ == "__main__":
    app.run(debug=True)