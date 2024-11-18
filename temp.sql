
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
VALUES('wonderful scent family', 'odors');

INSERT INTO Perfume_details(fname, creator, ftop, fheart, fbase, fline)
VALUES('Over Red', 'YSL', 'water', 'more water', 'cherry', 'Opium'),
('Bombshell Paradise', 'Victorias Secret', 'grass', 'oranges', 'water', 'Bombshell');

INSERT INTO Perfumer(pfname, pcompany)
VALUES('YSL', 'Yves St Laurent'),
('Victorias Secret', 'VS');
