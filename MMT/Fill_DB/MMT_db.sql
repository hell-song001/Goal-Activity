DROP TABLE IF EXISTS goal;
DROP TABLE IF EXISTS activity;

-- Goal success should be Monetary of temporal
CREATE TABLE goal (
    id integer primary key autoincrement, 
    goal_name varchar(255) not null,
    date_created datetime DEFAULT CURRENT_TIMESTAMP,
    end_date varchar(10) not null,
    amount float(30) not null,
    interest float(30) not null,
    prog_status char DEFAULT 'P' -- P = on progress, S = success, F = Failed
    );

-- TO DO: Add activity summary
CREATE TABLE activity (
    id integer primary key autoincrement, 
    goal_id integer,
    act_name varchar(255) not null,
    summary text not null,
    rvn_type varchar(3), --PFT = trading profit, RYL = Royalties, CGS = Capital gains, DVD = dividend, RNT = rent, JOB, INT = interest
    date_created datetime DEFAULT CURRENT_TIMESTAMP,
    capital float(30),
    ROC float(30),
    FOREIGN KEY (goal_id) REFERENCES goal (id)
);