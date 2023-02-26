from flask import Flask, render_template, jsonify
from database import jobs_from_db


app = Flask(__name__)


@app.route("/")
def home():
  return render_template("home.html")


@app.route("/about/our-story")
def about_us():
  return render_template("about.html")

@app.route("/about/our-team")
def our_team():
  return render_template("about/our-team.html")


@app.route("/about/board-of-directors")
def board_of_directors():
  return render_template("about/board-of-directors.html")


@app.route("/about/careers")
def careers():
  jobs = jobs_from_db()
  return render_template("about/careers.html", jobs=jobs)


@app.route("/about/financials")
def financials():
  return render_template("about/financials.html")


@app.route("/about/our-partners")
def our_partners():
  return render_template("about/our-partners.html")


@app.route("/about/contact")
def contact():
  return render_template("about/contact.html")


@app.route("/programs-services")
def programs_services():
  return render_template("programs.html")


@app.route("/programs-services/civic-engagement")
def civic_engagement():
  return render_template("civic-engagement.html")


@app.route("/programs-services/esol-class")
def esol():
  return render_template("esol.html")


@app.route("/programs-services/khmer-class")
def khmer_class():
  return render_template("khmer-class.html")


@app.route("/programs-services/monorom-program")
def monorom_program():
  return render_template("monorom-program.html")


@app.route("/programs-services/translation-services")
def translation_services():
  return render_template("translation-services.html")


@app.route("/programs-services/walk-in-services")
def walk_in_services():
  return render_template("programs-services/walk-in-services/walk-in-services.html") 


@app.route("/programs-services/walk-in-services/citizenship-class")
def walk_in_services_citizenship_class():
  return render_template("programs-services/walk-in-services/us-citizenship-class.html") 


@app.route("/programs-services/walk-in-services/first-time-home-buyer-training")
def walk_in_services_fthb_training():
  return render_template("programs-services/walk-in-services/first-time-home-buyer-training.html")


@app.route("/programs-services/walk-in-services/covid-19-resources")
def walk_in_services_covid_19_resources():
  return render_template("programs-services/walk-in-services/covid-19-resources.html")

@app.route("/programs-services/walk-in-services/other-services")
def walk_in_services_other_services():
  return render_template("programs-services/walk-in-services/other-services.html")


@app.route("/programs-services/youth-programs")
def youth_programs():
  return render_template("programs-services/youth-programs/youth-programs.html")

@app.route("/programs-services/youth-programs/cambodian-after-school")
def youth_programs_cambodian_after_school():
  return render_template("programs-services/youth-programs/cambodian-after-school.html")


@app.route("/programs-services/youth-programs/rising-stars-summer-program")
def youth_programs_rising_stars_summer_program():
  return render_template("programs-services/youth-programs/rising-stars-summer-program.html")


@app.route("/programs-services/youth-programs/young-professional-leadership-program")
def youth_programs_young_professional_leadership_program():
  return render_template("programs-services/youth-programs/young-professional-leadership-program.html")


@app.route("/news-events/news")
def news():
  return render_template("news-events/news.html")


@app.route("/news-events/events")
def events():
  return render_template("news-events/events.html")


@app.route("/news-events/social-media-pages")
def social_media_pages():
  return render_template("news-events/social-media-pages.html")


@app.route("/get-involved/corporate-sponsors")
def corporate_sponsors():
  return render_template("get-involved/corporate-sponsors.html")


@app.route("/get-involved/donate")
def get_involved_donate():
  return render_template("get-involved/donate.html")


@app.route("/get-involved/volunteer")
def volunteers():
  return render_template("get-involved/volunteer.html")


@app.route("/api/jobs")
def jobs_list():
  jobs = jobs_from_db()
  return jsonify(jobs)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)