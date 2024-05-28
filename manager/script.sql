DROP TABLE IF EXISTS Contact;
DROP TABLE IF EXISTS Address;
DROP TABLE IF EXISTS TelephoneNumber;

CREATE TABLE Contact(
id INTEGER NOT NULL,
firstname VARCHAR(32) NOT NULL,
lastname VARCHAR(32),
PRIMARY KEY(id autoincrement)
);

CREATE TABLE Address(
id INTEGER NOT NULL,
contact_id INTEGER NOT NULL,
address VARCHAR(32),
PRIMARY KEY(id autoincrement)
);

CREATE TABLE TelephoneNumber(
id INTEGER NOT NULL,
contact_id INTEGER NOT NULL,
telephone_number VARCHAR(32) NOT NULL,
PRIMARY KEY(id autoincrement)
);