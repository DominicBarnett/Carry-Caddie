from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, SelectField, SubmitField, SelectMultipleField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, NumberRange

class CarryYardageForm(FlaskForm):
    """Form for adding/updating Carry Yardages"""
    PWedge = IntegerField('Pitching Wedge')
    Nine_Iron = IntegerField('Nine Iron')
    Eight_Iron = IntegerField('Eight Iron')
    Seven_Iron = IntegerField('Seven Iron')
    Six_Iron = IntegerField('Six Iron')
    Five_Iron = IntegerField('Five Iron')
    Four_Iron = IntegerField('Four Iron')
    Three_Iron = IntegerField('Three Iron')
    Hybrid = IntegerField('Hybrid')
    Five_Wood = IntegerField('Five wood')
    Three_Wood = IntegerField('Three wood')
    Driver = IntegerField('Driver')
    submit = SubmitField('Submit')

 
