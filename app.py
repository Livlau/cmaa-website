from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Director of Programs',
    'location': 'Lowell, MA'
  },
  {
    'id': 2,
    'title': 'Executive Assistant',
    'location': 'Remote',
    'salary': '$40,000 - $50,000'
  },
  {
    'id': 3,
    'title': 'Monorom Assistant',
    'location': 'MA, USA',
    'salary': '$30,000 - $40,000'
  }
]


@app.route("/")
def hello_cmaa():
  return render_template("home.html", jobs=JOBS)


@app.route("/api/jobs")
def jobs_list():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)