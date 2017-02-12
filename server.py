#! /usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    from flask import render_template
    return render_template("index.html")


@app.route("/encounter", methods=['GET', 'POST'])
def encounter():
    wilderness = [
        {"title": "Пустынная", "chance": 5},
        {"title": "Дикая", "chance": 8},
        {"title": "Обитаемая", "chance": 10},
        {"title": "Густонаселенная", "chance": 12},
    ]

    from flask import request, render_template
    if request.method == 'POST':
        try:
            hours = int(request.form["hours"])
        except ValueError:
            hours = 0
            pass
    else:
        hours = -1000
    return render_template("encounter.html", hours=hours, wilderness=wilderness)


if __name__ == "__main__":
    app.run(debug=True)
