from flask import Flask, render_template

from controllers.vet_controller import vet_blueprint

app = Flask(__name__)

app.register_blueprint(vet_blueprint)


@app.route("/")
def homepage():
    return render_template("index.html", title="Home")


if __name__ == "__main__":
    app.run()
