from flask import Flask, render_template, request, redirect, url_for
from helper import retrieve_goals, create_goals, retrieve_activity, create_activity, del_goals

app = Flask(__name__)

@app.route("/")
def home():
    data = retrieve_goals()
    return render_template("index.html", data=data)

@app.route("/goals/", methods=['GET', 'POST'])
def goals():
    if request.method == 'POST':

        goal_name = request.form['goal-name']
        desc = request.form['desc']
        end_date = request.form['end-date']

        create_goals(goal_name, desc, end_date)
        return redirect(url_for("home"))
    return render_template("create_goal.html")

@app.route("/activity/<int:id>", methods=['GET', 'POST'])
def activity(id):
    if request.method == "POST":
        heading = request.form['heading']
        body = request.form['body']

        create_activity(id, heading, body)
        return redirect(url_for("activity", id=id))
    return render_template("create_activity.html", id=id)


@app.route("/get_activity/<int:id>", methods=['GET', 'POST'])
def get_activity(id):
    data = retrieve_activity(id)
    return render_template("activity.html", data=data)


@app.route("/del_goal/<int:id>", methods=['GET', 'POST'])
def del_goal(id):
    del_goals(id)
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)