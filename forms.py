from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField

from wtforms import validators, ValidationError

class ContactForm(Form):
    name = TextField("学生姓名",[validators.Required("Please enter your name.")])
    Gender = RadioField('性别', choices = [('M','Male'),('F','Female')])
    Address = TextAreaField("地址")

    email = TextField("Email",[validators.Required("Please enter your email address."),
      validators.Email("Please enter your email address.")])

    Age = IntegerField("年龄")
    language = SelectField('语言', choices = [('cpp', 'C++'), ('py', 'Python')])
    submit = SubmitField("提交")

