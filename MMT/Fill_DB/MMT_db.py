import sqlite3
from datetime import date
from monthly_interest import MoneyTree

con = sqlite3.connect("temp/mmt.db")
cur = con.cursor()

with open("Fill_DB/MMT_db.sql", "r") as f:
    sql_script = f.read()
    print(sql_script)
    cur.executescript(sql_script)
con.commit()

def add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = 15
    return date(year, month, day)


MMT = MoneyTree()
data = []
first_date = date(2023, 6, 15)


for i in range(0, len(MMT.PROFITS)):
    result = tuple([first_date, MMT.AMOUNTS[i], MMT.PROFITS[i]])
    data.append(result)
    first_date = add_months(first_date, 1)


cur.executemany("INSERT INTO goal (end_date, amount, interest) VALUES(?, ?, ?)", data)
con.commit()