from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

@app.route("/")                              # accueil : nb de cartes à réviser
@app.route("/review", methods=["GET", "POST"])   # afficher carte / recevoir réponse
@app.route("/import", methods=["GET", "POST"])   # upload Excel