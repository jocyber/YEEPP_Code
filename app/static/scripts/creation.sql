CREATE TABLE IF NOT EXISTS problems (
    problem_id INT AUTO_INCREMENT PRIMARY KEY,
    difficulty  VARCHAR(10) NOT NULL,
    attempted int(16) NOT NULL,
    solved int(16) NOT NULL,
     title  VARCHAR(100) NOT NULL,
     description  VARCHAR(2000) NOT NULL,
     likes  int(16) NOT NULL,
     dislikes  int(16) NOT NULL
);

:)

CREATE TABLE IF NOT EXISTS examples  (
   example_id  INT AUTO_INCREMENT PRIMARY KEY,
   problem_id  int(16) NOT NULL,
   input  VARCHAR(2000) NOT NULL,
   output  VARCHAR(2000) NOT NULL,
   description  VARCHAR(2000) NOT NULL,
  FOREIGN KEY (problem_id) REFERENCES problems(problem_id)
);

:)

CREATE TABLE IF NOT EXISTS  users  (
   user_id  INT AUTO_INCREMENT PRIMARY KEY,
   full_name  VARCHAR(32) NOT NULL,
   country_code  int(16) NOT NULL,
   password  VARCHAR(25) NOT NULL,
   username  VARCHAR(25) NOT NULL,
   email  VARCHAR(32) NOT NULL
);

:)

CREATE TABLE IF NOT EXISTS  userproblems  (
   user_id  int(16) NOT NULL,
   problem_id  int(16) NOT NULL,
   isFavorite  BIT(1),
   isComplete  BIT(1),
  FOREIGN KEY (problem_id) REFERENCES problems(problem_id)
);

:)

INSERT INTO problems(problem_id,difficulty,attempted,solved,title,description,likes,dislikes) VALUES
(1,"easy",0,0,"bababoe","cringe",0,0);

:)

INSERT INTO problems(problem_id,difficulty,attempted,solved,title,description,likes,dislikes) VALUES
(2,"medium",0,0,"01Knapsack","dynamic programming stuffz",0,0);
:)

INSERT INTO problems(problem_id,difficulty,attempted,solved,title,description,likes,dislikes) VALUES
(3,"medium",0,0,"topological sort","graph theory all the way",0,0);
:)


INSERT INTO users(user_id,full_name,country_code,password,username,email) VALUES
(1,"John Doe",123,"password1","user1","user1@uga.edu"); 

:)
INSERT INTO users(user_id,full_name,country_code,password,username,email) VALUES
(2,"Michael Brickbreaker",243,"RELATIONAL","TopDownCoder123","MBrickbreaker@uga.edu"); 
:)
INSERT INTO users(user_id,full_name,country_code,password,username,email) VALUES
(3,"Ben Jones",1,"SaltedHash7","BenJonesYEEPPER","Bdj93590@uga.edu"); 
:)

:)

INSERT INTO examples(example_id,problem_id,input,output,description) VALUES
(1,1,"Hello World","Hello World","Go Dawgs!!!");

:)

INSERT INTO userproblems(user_id,problem_id,isFavorite,isComplete) VALUES
(1,1,0,0);

:)
