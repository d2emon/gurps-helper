#! /usr/bin/env python
# -*- coding:utf-8 -*-
from app import app, db
from flask import flash, render_template, redirect, url_for


wilderness1 = [
    {"id": 0, "title": "Пустынная", "chance": 5},
    {"id": 1, "title": "Дикая", "chance": 8},
    {"id": 2, "title": "Обитаемая", "chance": 10},
    {"id": 3, "title": "Густонаселенная", "chance": 12},
]


@app.route("/")
def hello():
    from flask import render_template
    return render_template("index.html")


@app.route("/settings/land")
@app.route("/settings/land/<int:id>")
def setLand(id=None):
    import db
    e, s = db.connect(False)

    from encounter.wilderness import Wilderness
    from encounter.biome import Biome
    wild = s.query(Wilderness).all()
    print(wild)

    from flask import render_template
    if id is not None:
        w = s.query(Wilderness).get(id)
        print(w)

        biome = s.query(Biome).get(1)
        # biome.wilderness = w
        s.add(biome)
        s.commit()
        print(biome)

    return render_template("set_land.html", wilderness=wild)


@app.route("/char")
def character():
    from app.models import GameCharacter
    chars = GameCharacter.query.all()

    return render_template("char_list.html", chars=chars)


@app.route("/char/new", methods=['GET', 'POST'])
def new_character():
    from app.models import GameCharacter
    from app.forms import CharEditForm
    c = GameCharacter()
    form = CharEditForm()

    if form.validate_on_submit():
        c.charname = form.charname.data
        db.session.add(c)
        db.session.commit()
        flash('Your changes have been saved')
        return redirect(url_for('character'))
    else:
        form.charname.data = c.charname
    return render_template("char_edit.html", c=c, form=form)


@app.route("/char/id-<int:char_id>", methods=['GET', 'POST'])
def edit_character(char_id):
    from app.models import GameCharacter
    from app.forms import CharEditForm
    c = GameCharacter.query.get(char_id)
    if c is None:
        return redirect(url_for('character'))

    form = CharEditForm()

    if form.validate_on_submit():
        c.charname = form.charname.data
        db.session.add(c)
        db.session.commit()
        flash('Your changes have been saved')
        return redirect(url_for('character'))
    else:
        form.charname.data = c.charname
    return render_template("char_edit.html", c=c, form=form)


@app.route("/encounter")
def encounter():
    import db
    e, s = db.connect(False)

    from encounter.wilderness import Wilderness
    wild = s.query(Wilderness).all()
    print(wild)

    from flask import render_template
    return render_template("encounter.html", wilderness=wild)


@app.route("/encounter/<int:wild>", methods=['GET', 'POST'])
def encounterPlace(wild):
    from flask import request, render_template
    if request.method == 'POST':
        try:
            hours = int(request.form["hours"])
        except ValueError:
            hours = 0
            pass
    else:
        hours = -1000

    import dice
    place = wilderness1[wild]
    i = 0
    for i in range(0, hours):
        c = dice.d(1, 100)
        if c <= place["chance"]:
            break

    return render_template("encounter_place.html", hours=hours, eh=i, place=place)
