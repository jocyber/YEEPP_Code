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
   username  VARCHAR(25) NOT NULL UNIQUE,
   email  VARCHAR(32) NOT NULL UNIQUE
);

:)

CREATE TABLE IF NOT EXISTS  userproblems  (
   user_id  INTEGER NOT NULL,
   problem_id  INTEGER NOT NULL,
   isFavorite  BIT(1),
   isComplete  BIT(1),
   isLike INT NULL,
  FOREIGN KEY (problem_id) REFERENCES problems(problem_id),
  FOREIGN KEY (user_id) REFERENCES users(user_id)
);

:)

CREATE TRIGGER increment_complete AFTER UPDATE OF isComplete ON userproblems
    BEGIN
        UPDATE problems SET solved = solved + 1 WHERE problem_id = old.problem_id;
    END;

:)

CREATE TRIGGER increment_attempted AFTER INSERT ON userproblems
    BEGIN
        UPDATE problems SET attempted = attempted + 1 WHERE problem_id = new.problem_id;
    END;

:)

CREATE TRIGGER increment_new_like AFTER UPDATE OF isLike ON userproblems
    WHEN old.isLike IS NULL AND new.isLike = 1
    BEGIN
        UPDATE problems SET likes = likes + 1 WHERE new.problem_id = problems.problem_id;
    END;

:)

CREATE TRIGGER increment_old_like AFTER UPDATE OF isLike ON userproblems
    WHEN old.isLike = 0 AND new.isLike = 1
    BEGIN
        UPDATE problems SET likes = likes + 1 WHERE old.problem_id = problems.problem_id;
        UPDATE problems SET dislikes = dislikes -1 WHERE old.problem_id = problems.problem_id;
    END;

:)

CREATE TRIGGER increment_new_dislike AFTER UPDATE OF isLike ON userproblems
    WHEN old.isLike IS NULL AND new.isLike = 0
    BEGIN
        UPDATE problems SET dislikes = dislikes + 1 WHERE old.problem_id = problems.problem_id;
    END;

:)

CREATE TRIGGER increment_old_dislike AFTER UPDATE OF isLike ON userproblems
    WHEN old.isLike = 1 AND new.isLike = 0
    BEGIN
        UPDATE problems SET dislikes = dislikes + 1 WHERE old.problem_id = problems.problem_id;
        UPDATE problems SET likes = likes -1 WHERE old.problem_id = problems.problem_id;
    END;

:)

INSERT INTO problems(problem_id,difficulty,attempted,solved,title,description,likes,dislikes) VALUES
(1,"easy",0,0,"Worth half semester grade","Given a professor name as a String return true as a string if a question is \'worth half the semester grade\' and false as a string otherwise.
 * A question is worth half a semester grade if  the professor is equal to \'Dr.Mario\' (case sensitive)
",0,0);

:)

INSERT INTO problems(problem_id,difficulty,attempted,solved,title,description,likes,dislikes) VALUES
(2,"easy",0,0,"Python lover","Given a string return the string \'Python is my love\' if the string \'Python\' (case insensitive) can be parsed from the input string and \':(\' otherwise
",0,0);

:)

INSERT INTO problems(problem_id,difficulty,attempted,solved,title,description,likes,dislikes) VALUES
(3,"easy",0,0,"Will the flight land","Given a pilot as a string, return true as a string if the \'plane will land\' and false as a string otherwise.  *Plane will Land if it is flown by \'Daniel\'.",0,0);

:)

INSERT INTO problems(problem_id,difficulty,attempted,solved,title,description,likes,dislikes) VALUES
(4,"easy",0,0,"Funny Jokes","Given a joke as a string, return \'LOL\' if it \'is funny and \'Do better\' otherwise. *A joke is funny if it contains the phrase \'Knock Knock\'(case insensitive) or \'Your Mom\' (case insensitive)",0,0);

:)

INSERT INTO problems(problem_id,difficulty,attempted,solved,title,description,likes,dislikes) VALUES
(5,"easy",0,0,"Boring math","Given an integer as a string, subtract the number of digits from the given integer and return the new number as a string",0,0);

:)

INSERT INTO problems(problem_id,difficulty,attempted,solved,title,description,likes,dislikes) VALUES
(6,"easy",0,0,"Sum is odd or even","
Given an integer as a string return \'even\' as a string if the sum of the digits is even and \'odd\' as as string if odd.
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

INSERT INTO examples(example_id,problem_id,input,output,description,methodHeader) VALUES
(1,1,"Dr.Mario","True","","isHalfSemesterGrade");

:)

INSERT INTO examples(example_id,problem_id,input,output,description,methodHeader) VALUES
(2,1,"Prof.Coder","False","","isHalfSemesterGrade");

:)

INSERT INTO examples(example_id,problem_id,input,output,description,methodHeader) VALUES
(3,2,"JAVAISAWESOME",":(","","lovePython");

:)

INSERT INTO examples(example_id,problem_id,input,output,description,methodHeader) VALUES
(4,2,"HTMLCSSPYTHONJAVASWIFT","Python is my love","","lovePython");

:)

INSERT INTO examples(example_id,problem_id,input,output,description,methodHeader) VALUES
(5,3,"Daniel","true","","willPlaneLand");

:)

INSERT INTO examples(example_id,problem_id,input,output,description,methodHeader) VALUES
(6,3,"Dwight","false","","willPlaneLand");

:)

INSERT INTO examples(example_id,problem_id,input,output,description,methodHeader) VALUES
(7,4,"Big brown bears eat big black bugs, surfboard, so funny,     your mom","LOL","","isFunny");

:)

INSERT INTO examples(example_id,problem_id,input,output,description,methodHeader) VALUES
(8,4,"why did the chicken cross the road","Do better","","isFunny");

:)

INSERT INTO examples(example_id,problem_id,input,output,description,methodHeader) VALUES
(9,5,"123","120","","subtractDigits");

:)

INSERT INTO examples(example_id,problem_id,input,output,description,methodHeader) VALUES
(10,5,"1000","996","","subtractDigits");

:)

INSERT INTO examples(example_id,problem_id,input,output,description,methodHeader) VALUES
(11,6,"123","even","","digitsOddOrEven");

:)

INSERT INTO examples(example_id,problem_id,input,output,description,methodHeader) VALUES
(12,6,"999999999","odd","","digitsOddOrEven");

:)

INSERT INTO userproblems(user_id,problem_id,isFavorite,isComplete) VALUES
(1,1,0,0);
