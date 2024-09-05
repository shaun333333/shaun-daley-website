from flask import Flask, render_template, jsonify

app = Flask(__name__)

PLAYERS = [
    {
        'id': 1,
        'title': 'Keegan',
        'record': '5-5',
        'location': 'Connecticut'
    },
    {
        'id': 2,
        'title': 'Shaun',
        'record': '5-5',
        'location': 'Cambridge'
    },
    {   
        'id': 3,
        'title': 'Peter',
        'record': '5-5',
        'location': 'Connecticut'
    }
]


@app.route('/')
def hello_world():
    return render_template('home.html', players=PLAYERS )

@app.route("/api/jobs")
def list_jobs():
    return jsonify(PLAYERS)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug = True)