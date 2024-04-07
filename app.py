from flask import Flask, render_template ,jsonify

app = Flask(__name__)

stupid_person_collection = [
    {
        'id': 1,
        'Name': 'Gan Xin Yi',
        'Problem': 'Brain',
        'Stupid index': '60%',
    },
    {
        'id': 2,
        'Name': 'Amelia',
        'Problem': 'Hand',
        'Stupid index': '75%',
    },
    {
        'id': 3,
        'Name': 'Bonjour__',
        'Problem': 'body interupt',
        'Stupid index': '80%',
    },
    {
        'id': 4,
        'Name': 'Gan Gan',
        'Problem': 'face problem',
        'Stupid index': '100%',
    }
]

@app.route("/")
def hello_world():
    return render_template('home.html', persons=stupid_person_collection)

@app.route("/person")
def list_job():
    return jsonify(stupid_person_collection)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
