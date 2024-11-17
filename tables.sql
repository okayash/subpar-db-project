-- database -- 
CREATE database perfumedb;

-- tables
CREATE TABLE Fragrance (
  fname VARCHAR(80) PRIMARY KEY,
  rating INT,
  creator VARCHAR(80) NOT NULL,
  ftop VARCHAR(45),
  fheart VARCHAR(45),
  fbase VARCHAR(45),
  fline VARCHAR(45),

  FOREIGN KEY (fline) REFERENCES PerfumeLine(pline) 

);

CREATE TABLE Scentfamily (
  sname VARHCHAR (45) PRIMARY KEY
);

CREATE TABLE Subfamily (
  
);

CREATE TABLE PerfumeLine (
  pline VARCHAR(45) PRIMARY KEY,
  pyear int
);

CREATE TABLE Users (
  username VARCHAR(45) PRIMARY KEY,
  preferences VARCHAR(45),
  password VARCHAR(45)
);

CREATE TABLE Perfume (
    pname VARCHAR(45) PRIMARY KEY,

    FOREIGN KEY (pname) REFERENCES Fragrance(fname)
  
);

CREATE TABLE Perfumer (
    pfname VARCHAR(45) PRIMARY KEY,
    pcompany VARCHAR(45)
);

CREATE TABLE Cologne (
  
);

CREATE TABLE Concentration (
  
);

CREATE TABLE F_release_date(

);
