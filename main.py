from flask import Flask, jsonify, request
import csv

all_articles = []

with open("Articles.csv",encoding = 'unicode_escape') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

app = Flask(__name__)

@app.route("/get-articles")
def get_article():
    return jsonify({
        "data": all_articles[0],
        "message": "success"
    }), 200

if __name__ == "__main__":
    app.run()