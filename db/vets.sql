DROP TABLE IF EXISTS records;
DROP TABLE IF EXISTS animals;
DROP TABLE IF EXISTS owners;
DROP TABLE IF EXISTS addresses;
DROP TABLE IF EXISTS vets;

CREATE TABLE vets (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    max_animals INT
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
    dob TIMESTAMP,
    species VARCHAR(255),
    breed VARCHAR(255),
    owner_id INT REFERENCES owners(id),
    vet_id INT REFERENCES vets(id),
    date_registered TIMESTAMP,
    checked_in BOOLEAN
);

CREATE TABLE records (
    id SERIAL PRIMARY KEY,
    date TIMESTAMP,
    entry TEXT,
    animal_id INT REFERENCES animals(id) ON DELETE CASCADE
);

INSERT INTO addresses (num, street, city, postcode) VALUES ('17', 'Main Street', 'Edinburgh', 'AB1 2CD');
INSERT INTO addresses (num, street, city, postcode) VALUES ('887', 'Big Road', 'London', 'W8 5TT');
INSERT INTO addresses (num, street, city, postcode) VALUES ('5', 'Side Road', 'Manchester', 'DC2 1BA');

INSERT INTO owners (first_name, last_name, address_id, tel, email) VALUES ('Kevin', 'Jones', 1, '07676 767676', 'kevin@email.com');
INSERT INTO owners (first_name, last_name, address_id, tel, email) VALUES ('Steve', 'Baker', 2, '07762 919382', 'steve@email.com');
INSERT INTO owners (first_name, last_name, address_id, tel, email) VALUES ('Michael', 'Martin', 3, '07626 172497', 'jeremy@email.com');

INSERT INTO vets (first_name, last_name, max_animals) VALUES ('John', 'Smith', 3);
INSERT INTO vets (first_name, last_name, max_animals) VALUES ('Linda', 'Bridges', 2);
INSERT INTO vets (first_name, last_name, max_animals) VALUES ('Sarah', 'Jackson', 5);
INSERT INTO vets (first_name, last_name, max_animals) VALUES ('Hugh', 'Polson', 4);
INSERT INTO vets (first_name, last_name, max_animals) VALUES ('James', 'Anderson', 4);

INSERT INTO animals (name, dob, species, breed, owner_id, vet_id, date_registered, checked_in) VALUES ('Fluff', '2018-04-14', 'Cat', 'Maine Coon', 1, 1, '2020-08-06 11:42', false);
INSERT INTO animals (name, dob, species, breed, owner_id, vet_id, date_registered, checked_in) VALUES ('Floof', '2017-07-23', 'Dog', 'Spaniel', 2, 2, '2020-08-06 14:13', true);
INSERT INTO animals (name, dob, species, breed, owner_id, vet_id, date_registered, checked_in) VALUES ('Adrian', '1990-10-23', 'Chameleon', 'Veiled Chameleon', 1, 2, '2020-08-05 "12:01', true);
INSERT INTO animals (name, dob, species, breed, owner_id, vet_id, date_registered, checked_in) VALUES ('Sticky', '2019-11-28', 'Stick Insect', 'Common', 3, 4, '2020-08-05 16:48', true);
INSERT INTO animals (name, dob, species, breed, owner_id, vet_id, date_registered, checked_in) VALUES ('Howard', '1965-01-12', 'Tortoise', 'Galapagos', 3, 3, '07-08-2020 10:14', true);
INSERT INTO animals (name, dob, species, breed, owner_id, vet_id, date_registered, checked_in) VALUES ('Harambe', '1999-05-27', 'Gorilla', 'Western Lowland', 2, 5, '2016-05-28 08:58', false);

INSERT INTO records (date, entry, animal_id) VALUES ('2020-08-07 10:29:50', 'Cat is sick', 1);
INSERT INTO records (date, entry, animal_id) VALUES ('2020-08-08 14:11:01', 'Cat is still sick', 1);
INSERT INTO records (date, entry, animal_id) VALUES ('2020-08-07 15:34:11', 'Dog is ill', 2);
INSERT INTO records (date, entry, animal_id) VALUES ('2020-08-07 16:11:40', 'Chameleon can''t change colour', 3);
INSERT INTO records (date, entry, animal_id) VALUES ('2020-08-03 11:21:37', 'We''ve had Sticky in for a few days now and something is wrong, he''s been right off his food and he''s hardly moving at all. Further tests are definitely needed but this could be serious.', 4);
INSERT INTO records (date, entry, animal_id) VALUES ('2020-08-07 17:54:28', 'Further tests show that Sticky is in fact a stick and we''ve all made a terrible mistake', 4);
INSERT INTO records (date, entry, animal_id) VALUES ('2020-08-07 17:58:22', 'Poked him with a stick (haha). He''s definitely a stick.', 4);
INSERT INTO records (date, entry, animal_id) VALUES ('2016-05-28 18:09:44', 'Harambe got shot and we''re all very sad about it', 5);
