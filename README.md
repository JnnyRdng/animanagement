# Brief

The brief is to create software to help a vet surgery manage their vets and animals. This is a full-stack web app built with flask that uses RESTful routes and CRUD actions.

---

### Build notes

#### Dependencies: Flask, psycopg2, postgres

In Terminal:

```zsh
> git clone git@github.com:JnnyRdng/vet_management_project.git
```

Create the postgres database:
```zsh
> cd flask_web_app
> createdb vet_management
```

Create database tables:
```zsh
> psql -d vet_management -f /db/vets.sql
```

Seed database:
```zsh
> python3 console.py
```

Start server:
```zsh
> flask run
```

Open [localhost:5000](http://localhost:5000) in your web browser


