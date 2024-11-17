-- database -- 
CREATE database perfumedb;

-- tables --
CREATE TABLE PerfumeLine (
  pline VARCHAR(45) PRIMARY KEY,
  pyear int
);

CREATE TABLE Fragrance (
  fname VARCHAR(80) PRIMARY KEY,
  rating INT,
  creator VARCHAR(80) NOT NULL,
  ftop VARCHAR(45),
  fheart VARCHAR(45),
  fbase VARCHAR(45),
  fline VARCHAR(45),
  username VARCHAR(45),

  FOREIGN KEY (fline) REFERENCES PerfumeLine(pline),
  FOREIGN KEY username REFERENCES Users(username)

);

CREATE TABLE Scentfamily (
  sname VARCHAR (45) PRIMARY KEY
);

CREATE TABLE Subfamily (
  sfamilyname VARCHAR(45),
  characteristic VARCHAR(50),
  
  FOREIGN KEY (sfamilyname) REFERENCES Scentfamily(sname),

  PRIMARY KEY (sfamilyname, characteristic)

);

CREATE TABLE Users (
  username VARCHAR(45) PRIMARY KEY,
  preferences VARCHAR(45),
  password VARCHAR(45)

);

CREATE TABLE Perfume (
    pname VARCHAR(45),
    oilper INT,
    sillage INT,

    FOREIGN KEY (pname) REFERENCES Fragrance(fname),
    PRIMARY KEY (pname, oilper)
);

CREATE TABLE Perfumer (
    pfname VARCHAR(45) PRIMARY KEY,
    pcompany VARCHAR(45)
);

CREATE TABLE Cologne (
  cname VARCHAR(45),
  oilper INT,
  timetoreapply FLOAT(10), 
  
  FOREIGN KEY (cname) REFERENCES Fragrance(fname),
  PRIMARY KEY (cname, oilper)
);

CREATE TABLE Freleasedate(
  fname VARCHAR(45) PRIMARY KEY,
  month INT,
  year INT,
  FOREIGN KEY (fname) REFERENCES Fragarance(fname)
);
