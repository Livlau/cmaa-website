from flask import Flask, render_template, jsonify
from database import jobs_from_db


app = Flask(__name__)


@app.route("/")
def hello_cmaa():
  jobs = jobs_from_db()
  return render_template("home.html", jobs=jobs)


@app.route("/about")
def about_us():
  return render_template("about.html")


@app.route("/programs")
def programs_services():
  return render_template("programs.html")


@app.route("/civic-engagement")
def civic_engagement():
  return render_template("civic-engagement.html")


@app.route("/api/jobs")
def jobs_list():
  jobs = jobs_from_db()
  return jsonify(jobs)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)