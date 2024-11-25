-- Populate 
-- database -- 
CREATE DATABASE IF NOT EXISTS perfumedb;
USE perfumedb;

-- tables --
CREATE TABLE Users(
  username VARCHAR(45) PRIMARY KEY,
  preferences VARCHAR(45),
  password VARCHAR(45) NOT NULL,
  first_name VARCHAR(45) NOT NULL
);

CREATE TABLE PerfumeLine(
  pline VARCHAR(45) PRIMARY KEY,
  pyear INTEGER
);

CREATE TABLE Fragrance(
  fname VARCHAR(80),
  rating INTEGER,
  username VARCHAR(45) NOT NULL,
  PRIMARY KEY(fname, username)
);

CREATE TABLE Family(
  sfamilyname VARCHAR(45) CHECK (sfamilyname IN ('Floral','Woody', 'Oriental', 'Fresh')),
  characteristic VARCHAR(50),
  PRIMARY KEY (sfamilyname, characteristic)
);

CREATE TABLE F_release_date(
  fname VARCHAR(45) PRIMARY KEY,
  month INTEGER CHECK (month > 0 AND month < 13),
  year INTEGER NOT NULL CHECK (year > 1899),
  FOREIGN KEY (fname) REFERENCES Fragrance(fname)
);

CREATE TABLE Perfume_details(
  fname VARCHAR(45),
  creator VARCHAR(80) NOT NULL,
  fbase VARCHAR(45),
  fline VARCHAR(45),
  subfamily VARCHAR(45),
  FOREIGN KEY (fname) REFERENCES Fragrance(fname),
  FOREIGN KEY (fline) REFERENCES PerfumeLine(pline),
  FOREIGN KEY (subfamily, characteristic) REFERENCES Family(sfamilyname, characteristic),
  PRIMARY KEY (fname, creator)
);

CREATE TABLE Perfumer(
  pfname VARCHAR(80) PRIMARY KEY,
  pcompany VARCHAR(45)
);

-- Add Data -- 

-- sample data c --

INSERT INTO Users(username, password, first_name)
VALUES('miroheiskanen', 'dallasstars', 'Miro'),
('ashley', 'password', 'Ashley'),
('ashleysparents', 'password', 'Names'),
('murdle', 'password000', 'Murdle'),
('tylertoffoli', 'sanjosesharks', 'Tyler'),
('taylorswift', 'folklore', 'Taylor'),
('herculepoirot', 'orientexpress', 'Poirot');

INSERT INTO PerfumeLine(pline, pyear)
Values ('Opium', 1977),
('Juliettehasagun', 2006),
('Good Girl', 2016),
('Bombshell', 2010);


INSERT INTO Fragrance(fname, rating, username)
VALUES('Over Red', 8, 'ashley'),
('Not a perfume', 9, 'ashley'),
('Over Red', 1, 'tylertoffoli'),
('Over Red', 10, 'herculepoirot'),
('Bombshell Paradise', 2, 'tylertoffoli');

INSERT INTO Family(sfamilyname, characteristic)
VALUES('Fresh', 'odors');

INSERT INTO Perfume_details(fname, creator, ftop, fheart, fbase, fline)
VALUES('Over Red', 'YSL', 'water', 'more water', 'cherry', 'Opium'),
('Bombshell Paradise', 'Victorias Secret', 'grass', 'oranges', 'water', 'Bombshell');

INSERT INTO Perfumer(pfname, pcompany)
VALUES('YSL', 'Yves St Laurent'),
('Victorias Secret', 'VS');


