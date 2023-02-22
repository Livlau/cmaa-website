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

@app.route("/about/our-team")
def our_team():
  return render_template("about/our-team.html")


@app.route("/about/board-of-directors")
def board_of_directors():
  return render_template("about/board-of-directors.html")



@app.route("/programs")
def programs_services():
  return render_template("programs.html")


@app.route("/civic-engagement")
def civic_engagement():
  return render_template("civic-engagement.html")


@app.route("/esol")
def esol():
  return render_template("esol.html")


@app.route("/khmer-class")
def khmer_class():
  return render_template("khmer-class.html")


@app.route("/monorom-program")
def monorom_program():
  return render_template("monorom-program.html")


@app.route("/translation-services")
def translation_services():
  return render_template("translation-services.html")


@app.route("/walk-in-services")
def walk_in_services():
  return render_template("walk-in-services.html") 


@app.route("/walk-in-services/citizenship-class")
def walk_in_services_citizenship_class():
  return render_template("walk-in-services/us-citizenship-class.html") 


@app.route("/walk-in-services/first-time-home-buyer-training")
def walk_in_services_fthb_training():
  return render_template("walk-in-services/first-time-home-buyer-training.html")


@app.route("/walk-in-services/covid-19-resources")
def walk_in_services_covid_19_resources():
  return render_template("walk-in-services/covid-19-resources.html")

@app.route("/walk-in-services/other-services")
def walk_in_services_other_services():
  return render_template("walk-in-services/other-services.html")


@app.route("/youth-programs")
def youth_programs():
  return render_template("youth-programs.html")

@app.route("/youth-programs/cambodian-after-school")
def youth_programs_cambodian_after_school():
  return render_template("youth-programs/cambodian-after-school.html")


@app.route("/youth-programs/rising-stars-summer-program")
def youth_programs_rising_stars_summer_program():
  return render_template("youth-programs/rising-stars-summer-program.html")


@app.route("/youth-programs/young-professional-leadership-program")
def youth_programs_young_professional_leadership_program():
  return render_template("youth-programs/young-professional-leadership-program.html")


@app.route("/api/jobs")
def jobs_list():
  jobs = jobs_from_db()
  return jsonify(jobs)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)