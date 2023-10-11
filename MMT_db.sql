DROP TABLE IF EXISTS goal;
DROP TABLE IF EXISTS activity;

-- Goal success should be Monetary of temporal
CREATE TABLE goal (
    id integer primary key autoincrement, 
    goal_name varchar(255) not null,
    desc text,
    date_created datetime DEFAULT CURRENT_TIMESTAMP,
    end_date varchar(10) not null,
    prog_status char DEFAULT 'P' -- P = on progress, S = success, F = Failed
    );

CREATE TABLE activity (
    id integer primary key autoincrement, 
    goal_id integer, -- FK
    heading varchar(255) not null,
    body text, --success and failure metrics, skills required or developed
    date_created datetime DEFAULT CURRENT_TIMESTAMP,
    duration TIMESTAMP DEFAULT (CURRENT_TIMESTAMP + 31),
    FOREIGN KEY (goal_id) REFERENCES goal (id)
);

INSERT INTO goal (goal_name, desc, end_date) VALUES 
("Web Basic", "Learn HTML, CSS, Javascript, Python (Flask Framework).", "01-09-2021"),
("Web Basic II", "Learn C# (OOP), Computer Networks, Database system, Software development Techniques, Office solutions, computer system.","01-09-2021"),
("Software Shop", "Fix computers and other household devices.", "01-01-2022"),
("Software Shop II", "Learn E-commerce and cybersecurity", "01-01-2023"),
("Real Estate Tycoon", "Buying, investing and managing real estate.", "01-01-2023"),
("Personal Development", "Learn experience, failure tolerance andperseverance.", "01-01-2023"),
("Food Factory", "Storing, distributionand selling raw materials", "01-01-2025"),
("Software Shop III", "Financial services", "01-01-2026"),
("Real Estate Tycoon", "Learn real estate knowledge.", "01-01-2026"),
("Food Factory II", "Farming and marketing.", "01-01-2029"),
("Food Factory III", "Learn large scale distribution and logistic.", "01-01-2029");

INSERT INTO activity (goal_id, heading, body) VALUES 
(1, "Make a website.", "Make a scientific or statistics website"),
(2, "Software development.", "Make a scientific or statistics fullstack software");

























