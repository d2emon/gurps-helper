#! /usr/bin/env python
# -*- coding:utf-8 -*-
from app import db


class GameCharacter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    charname = db.Column(db.String, index=True, default="Персонаж")

    def __repr__(self):
        return '<Char {}>'.format(self.charname)

    def avatar(self, size=32):
        from hashlib import md5
        charname = self.charname
        if charname is None:
            import random
            charname = repr(random.getrandbits(128))
        return "http://www.gravatar.com/avatar/" + md5(charname.encode("utf-8")).hexdigest() + "?d=monsterid&s=" + str(size)
