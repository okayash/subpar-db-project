-- Populate 
-- database -- 
CREATE database perfumedb;

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

CREATE TABLE Perfume(
    pname VARCHAR(45),
    oilper INTEGER,
    sillage INTEGER,
    FOREIGN KEY (pname) REFERENCES Fragrance(fname),
    PRIMARY KEY (pname, oilper)
);

CREATE TABLE Cologne(
  cname VARCHAR(45),
  oilper INTEGER,
  time_reapplication INTEGER,
  FOREIGN KEY (cname) REFERENCES Fragrance(fname),
  PRIMARY KEY (cname, oilper)
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
  ftop VARCHAR(45),
  fheart VARCHAR(45),
  fbase VARCHAR(45),
  fline VARCHAR(45),
  subfamily VARCHAR(45),
  characteristic VARCHAR(45),
  FOREIGN KEY (fname) REFERENCES Fragrance(fname),
  FOREIGN KEY (fline) REFERENCES PerfumeLine(pline),
  FOREIGN KEY (subfamily, characteristic) REFERENCES Family(sfamilyname, characteristic),
  PRIMARY KEY (fname, creator)
);

CREATE TABLE Perfumer(
  pfname VARCHAR(80) PRIMARY KEY,
  pcompany VARCHAR(45),
);

-- Add Data -- 
