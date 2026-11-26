import random
from datetime import date
from flask import Flask, render_template, request, redirect, url_for

from repository import CardRepository
from interval import LeitnerScheduler
from session import ReviewSession, PracticeSession

app = Flask(__name__)
repo = CardRepository("test.db")
scheduler = LeitnerScheduler()


def new_session() -> ReviewSession:
    return ReviewSession(repo, scheduler, date.today())


def prochaine_revision() -> dict | None:
    """Date de la prochaine révision (utile quand plus aucune carte n'est due)."""
    cards = repo.get_all()
    if not cards:
        return None
    d = min(c.next_review for c in cards)
    return {
        "date": d,
        "jours": (d - date.today()).days,
        "nb": sum(1 for c in cards if c.next_review == d),
    }


@app.route("/")
def index():
    nb = len(repo.get_due(date.today()))
    return render_template("index.html", nb=nb, total=len(repo.get_all()), prochaine=prochaine_revision())


@app.route("/review")
def review():
    card = new_session().random_card()
    if card is None:
        return render_template("finished.html", prochaine=prochaine_revision())
    return redirect(url_for("review_card", card_id=card.id))


@app.route("/review/<int:card_id>", methods=["GET", "POST"])
def review_card(card_id):
    session = new_session()

    if request.method == "POST":
        session.answer(card_id, request.form["correct"] == "1")
        return redirect(url_for("review"))

    card = session.get_card(card_id)
    if card is None:          # carte déjà révisée ou inexistante : on en tire une autre
        return redirect(url_for("review"))

    reveal = request.args.get("reveal") == "1"
    return render_template("review.html", card=card, reveal=reveal)


@app.route("/practice")
def practice():
    """Relancer : revoir toutes les cartes (ordre aléatoire) sans toucher aux boîtes ni aux dates."""
    seed = request.args.get("seed", type=int)
    if seed is None:          # nouveau tour : on choisit une graine, donc un nouvel ordre
        return redirect(url_for("practice", seed=random.randrange(1_000_000)))

    session = PracticeSession(repo, seed)
    i = request.args.get("i", 0, type=int)
    card = session.card_at(i)
    if card is None:
        return render_template("practice.html", card=None, total=session.total())
    reveal = request.args.get("reveal") == "1"
    return render_template("practice.html", card=card, i=i, seed=seed, total=session.total(), reveal=reveal)


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