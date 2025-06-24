from flask import Blueprint, render_template, jsonify, request, session, flash, url_for, redirect
import random
from .models import Subject, Match, Feedback
from .elo import eloUpdate
from . import db
from app.forms import LoginForm
main_bp = Blueprint('main', __name__)
from datetime import datetime
import os


@main_bp.route("/rankings")
def rankings():
    subjects = Subject.query.order_by(Subject.rating.desc()).all()
    totalVotes = Match.query.count()
    return render_template("rankings.html", subjects=subjects, session=session, totalVotes=totalVotes)


@main_bp.route("/match")
def match():
    subjects = Subject.query.all()
    left, right = random.sample(subjects, 2)
    pair = [
        {"id": left.id, "name": left.name, "rating": left.rating},
        {"id": right.id, "name": right.name, "rating": right.rating}
    ]
    return jsonify({"pair": pair})

@main_bp.route("/vote", methods = ["POST"])
def vote():
    data = request.get_json()
    winner = Subject.query.get(data["winner_id"])
    loser = Subject.query.get(data["loser_id"])

    w_new, l_new = eloUpdate(winner.rating, loser.rating)
    winner.rating, loser.rating = w_new, l_new

    m = Match(
    winner_id = data["winner_id"],
    )
    db.session.add(m)
    db.session.commit()

    return jsonify({
      "winner": {"id": winner.id, "rating": winner.rating},
      "loser":  {"id": loser.id,  "rating": loser.rating}
    })

@main_bp.route("/feedback", methods=["POST"])
def feedback():
    name = request.form['name']
    content = request.form['feedback']

    fb = Feedback(name=name, content=content)
    db.session.add(fb)
    db.session.commit()
    
    return redirect(url_for('main.rankings')) 

@main_bp.route('/view-feedback')
def view_feedback():
    feedbacks = Feedback.query.all()
    return render_template('view_feedback.html', feedbacks=feedbacks)


@main_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form.get("username", "").strip()
        if not name:
            flash("Please enter a name.", "error")
        else:
           
            session['username'] = name
            
            session['rounds_completed'] = 0
            return redirect(url_for('main.index'))
    
    return render_template("login.html")

@main_bp.route("/")
def index():
    if 'username' not in session:
        return redirect(url_for('main.login'))
    return render_template("index.html", username=session['username'])