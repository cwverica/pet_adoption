from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, AnyOf, NumberRange

class AddPetForm(FlaskForm):
    '''form for adding pets'''

    name = StringField('Pet\'s Name', validators=[InputRequired(message="The pet must have a name.")])
    species = StringField('Pet\'s Species', validators=[InputRequired(message="The pet must have a species."), AnyOf(['Cat', 'Dog', 'Porcupine'], message="The clinic only accepts cats, dogs, and porcupines.")])
    photo_url = StringField('Photo of Pet (if available)', validators=[Optional(), URL(message="Must be a valid URL")])
    age = IntegerField('Age (if known)', validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField('Notes (optional)', validators=[Optional()])
    available = BooleanField('Is Pet Available?', id="avail")
