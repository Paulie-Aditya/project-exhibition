from flask import Flask, request, jsonify, render_template 
import script
import codecs
app = Flask(__name__)

@app.route("/", methods = ['GET'])
def home():
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def process():
    data = request.get_json()
    movie = data['movie']
    response = script.sentiment_analysis(movie)
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)