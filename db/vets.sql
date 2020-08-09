DROP TABLE IF EXISTS records;
DROP TABLE IF EXISTS animals;
DROP TABLE IF EXISTS owners;
DROP TABLE IF EXISTS addresses;
DROP TABLE IF EXISTS vets;

CREATE TABLE vets (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255)
);

CREATE TABLE addresses (
    id SERIAL PRIMARY KEY,
    num VARCHAR(255),
    street VARCHAR(255),
    city VARCHAR(255),
    postcode VARCHAR(12)
);

CREATE TABLE owners (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    address_id INT REFERENCES addresses(id) ON DELETE CASCADE,
    tel VARCHAR(255),
    email VARCHAR(255)
);

CREATE TABLE animals (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    dob VARCHAR(255),
    species VARCHAR(255),
    owner_id INT REFERENCES owners(id),
    vet_id INT REFERENCES vets(id),
    date_admitted VARCHAR(255),
    checked_in BOOLEAN
);

CREATE TABLE records (
    id SERIAL PRIMARY KEY,
    date VARCHAR(255),
    entry TEXT,
    animal_id INT REFERENCES animals(id) ON DELETE CASCADE
);

INSERT INTO addresses (num, street, city, postcode) VALUES ('17', 'Main Street', 'Edinburgh', 'AB1 2CD');
INSERT INTO addresses (num, street, city, postcode) VALUES ('887', 'Big Road', 'London', 'W8 5TT');
INSERT INTO addresses (num, street, city, postcode) VALUES ('5', 'Side Road', 'Manchester', 'DC2 1BA');

INSERT INTO owners (first_name, last_name, address_id, tel, email) VALUES ('Kevin', 'Jones', 1, '07676 767676', 'kevin@email.com');
INSERT INTO owners (first_name, last_name, address_id, tel, email) VALUES ('Steve', 'Baker', 2, '07762 919382', 'steve@email.com');
INSERT INTO owners (first_name, last_name, address_id, tel, email) VALUES ('Michael', 'Martin', 3, '07626 172497', 'jeremy@email.com');

INSERT INTO vets (first_name, last_name) VALUES ('John', 'Smith');
INSERT INTO vets (first_name, last_name) VALUES ('Linda', 'Bridges');
INSERT INTO vets (first_name, last_name) VALUES ('Sarah', 'Jackson');
INSERT INTO vets (first_name, last_name) VALUES ('Hugh', 'Polson');
INSERT INTO vets (first_name, last_name) VALUES ('James', 'Anderson');

INSERT INTO animals (name, dob, species, owner_id, vet_id, date_admitted, checked_in) VALUES ('Fluff', '14-04-2018', 'Cat', 1, 1, '06-08-2020', true);
INSERT INTO animals (name, dob, species, owner_id, vet_id, date_admitted, checked_in) VALUES ('Floof', '23-07-2017', 'Dog', 2, 2, '06-08-2020', true);
INSERT INTO animals (name, dob, species, owner_id, vet_id, date_admitted, checked_in) VALUES ('Adrian', '01-06-2010', 'Chameleon', 1, 2, '05-08-2020', true);
INSERT INTO animals (name, dob, species, owner_id, vet_id, date_admitted, checked_in) VALUES ('Sticky', '19-08-2016', 'Stick Insect', 3, 4, '05-08-2020', true);

INSERT INTO records (date, entry, animal_id) VALUES ('07-08-2020', 'Cat is sick', 1);
INSERT INTO records (date, entry, animal_id) VALUES ('08-08-2020', 'Cat is still sick', 1);
INSERT INTO records (date, entry, animal_id) VALUES ('07-08-2020', 'Dog is ill', 2);
INSERT INTO records (date, entry, animal_id) VALUES ('07-08-2020', 'Chameleon can''t change colour', 3);
INSERT INTO records (date, entry, animal_id) VALUES ('03-08-2020', 'Something is wrong with Sticky, he''s been right off his food and he''s hardly moving at all', 4);
INSERT INTO records (date, entry, animal_id) VALUES ('07-08-2020', 'Further tests show that Sticky is in fact a stick and we''ve all made a terrible mistake', 4);
