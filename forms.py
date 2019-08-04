from flask_wtf import Form
from wtforms.fields import *
from wtforms.validators import *
from wtforms import validators

# Contact Form for us to get user's info
class ContactForm(Form):
    name = TextField(u"称呼", validators=[Required()])
    email = TextField(u"Email")   # 因为感觉部分人不用邮件，所以不是必填项目
    wechat = TextField(u"微信")
    goodatfields = SelectMultipleField(u'擅长领域 ',
                                      choices = [(u'networds', u' 网络词汇'),
                                                 (u'computer', u'计算机'),
                                                 (u'dialect', u'方言'),
                                                 (u'plants', u'植物'),
                                                 (u'folklore', u'民俗'),
                                                 (u'other', u'其他')])
    comment = TextAreaField(u"留言")
    submit = SubmitField(u"提交")

# word edit form for users, most important form, set to index page
class WordEditForm(Form):
    word = TextField(u'词汇', validators=[Required()])
    # TODO: set default value, but disappear when user click to edit
    # TODO: add Markdown support
    meaning = TextAreaField(u'意义（编辑关于这个词汇的信息）', validators=[Required()])
    classify = SelectMultipleField(u'分类',
                         choices=[(u'networds', u' 网络词汇'),
                                  (u'computer', u'计算机'),
                                  (u'dialect', u'方言'),
                                  (u'plants', u'植物'),
                                  (u'folklore', u'民俗'),
                                  (u'other', u'其他')],
                         validators=[Required()])
    submit = SubmitField(u'提交')





'''
class SignupForm(Form):
    name = TextField(u'Your name', validators=[Required()])
    password = TextField(u'Your favorite password', validators=[Required()])
    email = TextField(u'Your email address', validators=[Email()])
    birthday = DateField(u'Your birthday')

    a_float = FloatField(u'A floating point number')
    a_decimal = DecimalField(u'Another floating point number')
    a_integer = IntegerField(u'An integer')

    now = DateTimeField(u'Current time',
                        description='...for no particular reason')
    sample_file = FileField(u'Your favorite file')
    eula = BooleanField(u'I did not read the terms and conditions',
                        validators=[Required('You must agree to not agree!')])

    submit = SubmitField(u'Signup')
'''
