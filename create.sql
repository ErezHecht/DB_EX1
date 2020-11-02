/*create table olympics(
  id varchar,
  name varchar,
  sex varchar,
  age varchar,
  height varchar,
  weight varchar,
  team varchar,
  noc varchar,
  games varchar,
  year varchar,
  season varchar,
  city varchar,
  sport varchar,
  event varchar,
  medal varchar
);*/


create table athlete(
id INTEGER PRIMARY KEY,
name VARCHAR(100)
sex CHAR(1) CHECK(sex='M' or sex='F'),
height INTEGER,
weight INTEGER
);

create table team(
name varchar(100),
noc varchar(3),
PRIMARY KEY (name, noc)
);

create table participation(
FOREIGN KEY teamname varchar(100) REFERENCES team(name) ON DELETE CASCADE,
FOREIGN KEY noc varchar(3)REFERENCES team(noc) ON DELETE CASCADE,
FOREIGN KEY athleteid INTEGER REFERENCES athlete(id) ON DELETE CASCADE,
FOREIGN KEY eventname varchar(100) REFERENCES event(name) ON DELETE CASCADE,
FOREIGN KEY year INTEGER REFERENCES games(year) ON DELETE CASCADE,
FOREIGN KEY season varchar(100) REFERENCES games(season) ON DELETE CASCADE,
age INTEGER CHECK(age > 0),
/*medal varchar(100),*/
/*PRIMARY KEY (teamname, noc, athleteid, eventname, year, season)*/
);

create table medal( /*TODO: This is not needed*/
type PRIMARY KEY varchar(100)
);

create table event(
name PRIMARY KEY varchar(100),
sport varchar(100)
);


create table games(
year INTEGER ,
season varchar(100) CHECK(season='Summer' or season="Winter"),
city varchar(100),
PRIMARY KEY (year, season)
);










