#! /usr/bin/env python
# -*- coding:utf-8 -*-
from web import app, db
from flask import flash, render_template, redirect, url_for


@app.route("/fraction")
def fraction():
    from web.models import Fraction
    fractions = Fraction.query.all()

    return render_template("fraction_list.html", chars=fractions)


@app.route("/fraction/new", methods=['GET', 'POST'])
def new_fraction():
    from web.models import Fraction
    from web.forms import FractionEditForm
    f = Fraction()

    form = FractionEditForm()

    if form.validate_on_submit():
        form.save_char(f)
        db.session.add(f)
        db.session.commit()
        flash('Your changes have been saved')
        return redirect(url_for('character'))
    else:
        form.load_fraction(f)
    return render_template("fraction_edit.html", c=f, form=form)


@app.route("/fraction/id-<int:fraction_id>", methods=['GET', 'POST'])
def edit_fraction(fraction_id):
    from web.models import Fraction
    from web.forms import FractionEditForm
    f = Fraction.query.get(fraction_id)
    if f is None:
        return redirect(url_for('fraction'))

    form = FractionEditForm()

    if form.validate_on_submit():
        form.save_char(f)
        db.session.add(f)
        db.session.commit()
        flash('Your changes have been saved')
        return redirect(url_for('character'))
    else:
        form.load_fraction(f)
    return render_template("fraction_edit.html", c=f, form=form)
