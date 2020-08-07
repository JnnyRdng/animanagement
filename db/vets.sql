DROP TABLE IF EXISTS records;
DROP TABLE IF EXISTS animals;
DROP TABLE IF EXISTS owners;
DROP TABLE IF EXISTS vets;

CREATE TABLE vets (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255)
);

CREATE TABLE owners (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
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

-- INSERT INTO vets (first_name, last_name) VALUES ('John', 'Smith');
-- INSERT INTO vets (first_name, last_name) VALUES ('Linda', 'Bridges');

-- INSERT INTO owners (first_name, last_name, tel, email) VALUES ('Kevin', 'Jones', '07676 767676', 'kevin@email.com');
-- INSERT INTO owners (first_name, last_name, tel, email) VALUES ('Steve', 'Baker', '07762 919382', 'steve@email.com');

-- INSERT INTO animals (name, dob, species, owner_id, vet_id, date_admitted, checked_in) VALUES ('Fluff', '14-04-2018', 'Cat', 1, 1, '06-08-2020', true);
-- INSERT INTO animals (name, dob, species, owner_id, vet_id, date_admitted, checked_in) VALUES ('Floof', '23-07-2017', 'Dog', 2, 2, '06-08-2020', true);
-- INSERT INTO animals (name, dob, species, owner_id, vet_id, date_admitted, checked_in) VALUES ('Adrian', '01-06-2010', 'Chameleon', 1, 2, '05-08-2020', true);

-- INSERT INTO records (date, entry, animal_id) VALUES ('07-08-2020', 'Cat is sick', 1);
-- INSERT INTO records (date, entry, animal_id) VALUES ('08-08-2020', 'Cat is still sick', 1);
-- INSERT INTO records (date, entry, animal_id) VALUES ('07-08-2020', 'Dog is ill', 2);
-- INSERT INTO records (date, entry, animal_id) VALUES ('07-08-2020', 'Chameleon can''t change colour', 3);

