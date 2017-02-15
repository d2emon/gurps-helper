from flask.ext.wtf import Form
#from FlaskForm import Form
from wtforms import TextField
from wtforms.validators import Required, NumberRange


class CharEditForm(Form):
    charname = TextField('charname', validators = [Required()])
    st = TextField('st', validators = [NumberRange()])
    dx = TextField('dx', validators = [NumberRange()])
    iq = TextField('iq', validators = [NumberRange()])
    ht = TextField('ht', validators = [NumberRange()])

    def load_char(self, c):
        self.charname.data = c.charname
        self.st.data = c.st
        self.dx.data = c.dx
        self.iq.data = c.iq
        self.ht.data = c.ht

    def save_char(self, c):
        c.charname = self.charname.data
        c.st = self.st.data
        c.dx = self.dx.data
        c.iq = self.iq.data
        c.ht = self.ht.data
