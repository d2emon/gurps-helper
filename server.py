#! /usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    from flask import render_template
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)