import sqlite3
import json

def db():

    return sqlite3.connect("mmt.db")


def create_db():
    cur = db().cursor()
    with open("MMT_db.sql", "r") as f:
        sql_script = f.read()
        print(sql_script)
        cur.executescript(sql_script)
    db().commit()

def retrieve_goals():
    con = db()
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    data = cur.execute("SELECT * FROM goal").fetchall()
    r_data = []
    for datum in data:
        r_data.append(dict(datum))
    return json.loads(json.dumps(r_data))

def create_goals(name, desc, end_date):
    con = db()
    cur = con.cursor()
    cur.execute("INSERT INTO goal (goal_name, desc, end_date) VALUES (?, ?, ?);",(name, desc, end_date))
    con.commit()

def retrieve_activity(goal_id):
    con = db()
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    data = cur.execute("SELECT * FROM activity WHERE goal_id = ?", (goal_id,)).fetchall()
    r_data = []
    for datum in data:
        r_data.append(dict(datum))
    return json.loads(json.dumps(r_data))

def create_activity(goal_id, heading, body):
    con = db()
    cur = con.cursor()
    cur.execute("INSERT INTO activity (goal_id, heading, body) VALUES (?, ?, ?);", (goal_id, heading, body))
    con.commit()


def del_goals(id):
    con = db()
    cur = con.cursor()
    cur.execute("DELETE FROM goal WHERE id = ?", (id,))
    con.commit()