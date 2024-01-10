from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.fields import StringField, IntegerField, SubmitField, PasswordField
from wtforms.validators import DataRequired, length, equal_to

class AddProductForm(FlaskForm):
    name = StringField("მასალა", validators=[DataRequired(message="Material Valley Important")])
    price = IntegerField("ფასი", validators=[DataRequired(message="Price Valley Important")])
    img = FileField("სურათი", validators=[FileRequired(), FileAllowed(["jpg", "png", "jpeg"])])
    length = IntegerField("სიგრძე", validators=[DataRequired(message="Length Valley Important")])
    color = StringField("ფერი", validators=[DataRequired(message="Color Valley Important")])

    submit = SubmitField("დამატება")
class EditProductForm(FlaskForm):
    name = StringField("მასალა", validators=[DataRequired(message="Material Valley Important")])
    price = IntegerField("ფასი", validators=[DataRequired(message="Price Valley Important")])
    img = FileField("სურათი", validators=[FileAllowed(["jpg", "png", "jpeg"])])
    length = IntegerField("სიგრძე", validators=[DataRequired(message="Length Valley Important")])
    color = StringField("ფერი", validators=[DataRequired(message="Color Valley Important")])

    submit = SubmitField("დამატება")


class RegistrationForm(FlaskForm):
    username = StringField()
    email = StringField()
    password = PasswordField(validators=[length(min=8, max=64)])
    confirm_password = PasswordField(validators=[equal_to("password")])

    register = SubmitField()

class LoginForm(FlaskForm):
    username = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired(), length(min=8, max=64)])

    login = SubmitField()