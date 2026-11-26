from datetime import date
from flask import Flask, render_template, request, redirect, url_for

from repository import CardRepository
from interval import LeitnerScheduler
from session import ReviewSession

app = Flask(__name__)
repo = CardRepository("test.db")
scheduler = LeitnerScheduler()


def new_session() -> ReviewSession:
    return ReviewSession(repo, scheduler, date.today())


@app.route("/")
def index():
    nb = len(repo.get_due(date.today()))
    return render_template("index.html", nb=nb)


@app.route("/review", methods=["GET", "POST"])
def review():
    session = new_session()

    if request.method == "POST":
        session.answer(request.form["correct"] == "1")
        return redirect(url_for("review"))

    if session.is_finished():
        return render_template("finished.html")

    reveal = request.args.get("reveal") == "1"
    return render_template("review.html", card=session.current_card(), reveal=reveal)

@app.route("/boxes")
def boxes():
    today = date.today()
    cards = repo.get_all()
    boxes_data = []
    for num, interval in scheduler.INTERVALS.items():
        in_box = sorted((c for c in cards if c.box == num), key=lambda c: c.next_review)
        boxes_data.append({"num": num, "interval": interval, "cards": in_box})
    return render_template("boxes.html", boxes=boxes_data, today=today)


if __name__ == "__main__":
    app.run(debug=True)