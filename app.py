from datetime import date
from flask import Flask, render_template, request, redirect, url_for

from repository import CardRepository
from interval import LeitnerScheduler
from session import ReviewSession

app = Flask(__name__)
repo = CardRepository("test.db")
scheduler = LeitnerScheduler()


def new_session() -> ReviewSession:
    
    
    # crée une ReviewSession avec repo, scheduler, date.today()


@app.route("/")
def index(): ...

@app.route("/review", methods=["GET", "POST"])
def review(): ...


if __name__ == "__main__":
    app.run(debug=True)