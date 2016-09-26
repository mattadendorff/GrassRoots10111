from flask_wtf import Form
from wtforms.fields import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired, Optional


class LoginForm(Form):
    """Accepts a name, location and a room (service)."""
    name = StringField('Name', validators=[DataRequired()])
    loc = StringField('Location', validators=[DataRequired()])
    room = StringField('Service', validators=[DataRequired()])
    submit = SubmitField('Submit SOS')


class GeoForm(Form):
    """Accepts a name, location and a room (service)."""
    name = StringField('Name', validators=[DataRequired()])
    lat = HiddenField('Latitude', validators=[Optional()])
    lon = HiddenField('Longitude', validators=[Optional()])
    w3w1 = StringField('What3Words: ', validators=[Optional()])
    w3w2 = StringField('What3Words - Word 2', validators=[Optional()])
    w3w3 = StringField('What3Words - Word 3', validators=[Optional()])
    room = StringField('Service', validators=[DataRequired()])
    submit = SubmitField('Submit SOS')

    def validate(self):
        if not super(GeoForm, self).validate():
            return False
        if not self.lat.data and not (self.w3w1.data and self.w3w2.data and self.w3w3.data):
            msg = 'You must either GeoLocate yourself or supply all three What3Words'
            self.lat.errors.append(msg)
            self.w3w1.errors.append(msg)
            return False
        return True


class AdminForm(Form):
    """Accepts a name and a room (service)."""
    name = StringField('Name', validators=[DataRequired()])
    room = StringField('Service', validators=[DataRequired()])
    submit = SubmitField('Monitor Requests')
