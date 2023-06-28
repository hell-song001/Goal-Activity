import sqlite3

#  Goal is updated through changing of activites or collapse of it's time
#  Activity delete after a goal time collapses

def db_conn():   
    return sqlite3.connect("temp/mmt.db")

def create_activity(goal_id, act_name, rvn_type, capital, ROC):

    if rvn_type not in ["PFT", "RYL", "CGS", "DVD", "RNT", "JOB", "INT"]:
        return "Incorrect type of revenue."
    
    try:
        goal_id = int(goal_id)
        capital = float(capital)
        ROC = float(ROC)
    except Exception as e:
        return  e
    
    con = db_conn()
    cur = con.cursor()
    cur.execute("INSERT INTO activity (goal_id, act_name, rvn_type, capital, ROC) VALUES (?, ?, ?, ?, ?)", (goal_id, act_name, rvn_type, capital, ROC))
    con.commit()

def update_activity(activity_id, *args):
    act_name, rvn_type, capital, ROC = args
    
    pass


def create_goal():
    pass

def delete_goal(id):
    con = db_conn()
    cur = con.cursor()
    cur.execute("DELETE FROM goal WHERE id = ?", (id,))
    con.commit()

def retrieve_goals():
    con = db_conn()
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    data = cur.execute("SELECT * FROM goal").fetchall()
    for i in data:
        print(dict(i))

def retrieve_acts():
    con = db_conn()
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    data = cur.execute("SELECT * FROM activity").fetchall()
    for i in data:
        print(dict(i))

#  create_activity(1, "Jasmine Shop", "PFT", 60000, 10000)
retrieve_acts()