CREATE TABLE IF NOT EXISTS problems (
    problem_id INTEGER PRIMARY KEY AUTOINCREMENT ,
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
   example_id  INTEGER  PRIMARY KEY AUTOINCREMENT,
   problem_id  INTEGER NOT NULL,
   input  VARCHAR(2000) NOT NULL,
   output  VARCHAR(2000) NOT NULL,
   description  VARCHAR(2000) NOT NULL,
    methodHeader VARCHAR(2000) NOT NULL,
  FOREIGN KEY (problem_id) REFERENCES problems(problem_id)
);

:)

CREATE TABLE IF NOT EXISTS  users  (
   user_id  INTEGER  PRIMARY KEY AUTOINCREMENT,
   full_name  VARCHAR(32) NOT NULL,
   country_code INT(16) NOT NULL,
   salt  VARCHAR(32),
   password  VARCHAR(40) NOT NULL,
   username  VARCHAR(25) NOT NULL,
   email  VARCHAR(32) NOT NULL
);

:)

CREATE TABLE IF NOT EXISTS  userproblems  (
   user_id  INTEGER NOT NULL,
   problem_id  INTEGER NOT NULL,
   isFavorite  BIT(1),
   isComplete  BIT(1),
   isLike INT NULL,
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

INSERT INTO problems(problem_id,difficulty,attempted,solved,title,description,likes,dislikes) VALUES
(4,"easy",0,0,"Worth half semester grade","Given a professor and a question return true if a question is worth half the semester grade and false otherwise. A question is worth half a semester grade if professor is equal to ‘Dr.Mario’",0,0);

:)

INSERT INTO problems(problem_id,difficulty,attempted,solved,title,description,likes,dislikes) VALUES
(5,"easy",0,0,"Python lover","Given an array of Strings return string Python is my love if Python is found in the array and :( otherwise
",0,0);

:)

INSERT INTO problems(problem_id,difficulty,attempted,solved,title,description,likes,dislikes) VALUES
(6,"easy",0,0,"Will the flight land","Given a pilot and a destination return true if the plane will land and false otherwise.  Plane will Land if it is flown by Daniel or if the destination is Galapagos Islands and false otherwise. However If plane is flown by Daniel'' and the destination is Galapagos Islands the plane will not land.
",0,0);

:)

INSERT INTO problems(problem_id,difficulty,attempted,solved,title,description,likes,dislikes) VALUES
(7,"easy",0,0,"Funny Jokes","Given a joke, return LOL if it is funny and Do better otherwise. A joke is funny if it contains the phrase Knock Knock or Your Mom",0,0);

:)

INSERT INTO problems(problem_id,difficulty,attempted,solved,title,description,likes,dislikes) VALUES
(8,"easy",0,0,"Boring math","Given an Array of integers, subtract the average of all the integers from each integer in the array and then sort from least to greatest and then return the array.",0,0);

:)

INSERT INTO problems(problem_id,difficulty,attempted,solved,title,description,likes,dislikes) VALUES
(9,"easy",0,0,"Sum is odd or even","
Given an integer return true if the sum of the digits is even and false if odd.
",0,0);

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

INSERT INTO examples(example_id,problem_id,input,output,description, methodHeader) VALUES
(1,1,"Hello World","Hello World","Go Dawgs!!!", "location");

:)

INSERT INTO examples(example_id,problem_id,input,output,description,methodHeader) VALUES
(2,2,"FIX BASED ON WHO CREATED PROBLEM","Hello World","Go Dawgs!!!","location");

:)

INSERT INTO examples(example_id,problem_id,input,output,description,methodHeader) VALUES
(3,3,"Hello World","Hello World","Go Dawgs!!!","location");

:)

INSERT INTO userproblems(user_id,problem_id,isFavorite,isComplete) VALUES
(1,1,0,0);
