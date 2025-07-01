from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_job_from_db

app = Flask(__name__)

# JOBS = [{
#     'id': 1,
#     'title': 'Data Analyst',
#     'location': 'Pune, India',
#     'salary': 'Rs. 15,00,000'
# },
# {
#     'id': 2,
#     'title': 'Mechanical Design Engineer',
#     'location': 'Pune, India',
#     'salary': 'Rs. 15,00,000'
# }, {
#     'id': 3,
#     'title': 'Frontend Engineer',
#     'location': 'Remote',
#     'salary': 'Rs. 12,00,000'
# }, {
#     'id': 4,
#     'title': 'Backend Engineer',
#     'location': 'San Francisco, USA',
#     'salary': '$120,000'
# }]



@app.route("/")
def hello():
    jobs = load_jobs_from_db()
    return render_template("home.html", 
                         jobs=jobs
                        )

@app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)

@app.route("/job/<id>")
def show_job(id):
   job = load_job_from_db(id)
   if not job:
      return "Not Found", 404
   
   return render_template('jobpage.html', job = job)



if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
