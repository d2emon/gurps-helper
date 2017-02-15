from flask.ext.wtf import Form
from wtforms import TextField
from wtforms.validators import Required


class CharEditForm(Form):
    charname = TextField('charname', validators = [Required()])
