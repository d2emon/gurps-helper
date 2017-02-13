#! /usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask
app = Flask(__name__)


wilderness = [
    {"id": 0, "title": "Пустынная", "chance": 5},
    {"id": 1, "title": "Дикая", "chance": 8},
    {"id": 2, "title": "Обитаемая", "chance": 10},
    {"id": 3, "title": "Густонаселенная", "chance": 12},
]


@app.route("/")
def hello():
    from flask import render_template
    return render_template("index.html")


@app.route("/encounter")
def encounter():
    from flask import render_template
    global wilderness
    return render_template("encounter.html", wilderness=wilderness)


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
    place = wilderness[wild]
    i = 0
    for i in range(0, hours):
        c = dice.d(1, 100)
        if c <= place["chance"]:
            break

    return render_template("encounter_place.html", hours=hours, eh=i, place=place)


if __name__ == "__main__":
    app.run(debug=True)
