from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,BooleanField
from wtforms.validators import DataRequired, Email  

class LoginForm(FlaskForm):
    username = StringField("username ", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    remember_me = BooleanField("remember_me")

class CadastroForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])

#class Capitao(FlaskForm):
#    username = StringField("username", validators=[DataRequired()])
#    identificacao = StringField("indetificacao", validators=[DataRequired()])
#    email = StringField("email",validators=[Email()])

class EquipeForm(FlaskForm):
    firstname = StringField("firstname", validators=[DataRequired()])
    lastname = StringField("lastname", validators=[DataRequired()])
    slogan = StringField("slogan", validators=[DataRequired()])
    email = StringField("email",validators=[DataRequired()])
    site = StringField("site",validators=[DataRequired()])
    país = StringField("país", validators=[DataRequired()])
    estado = StringField("estado", validators=[DataRequired()])
    cidade = StringField("cidade", validators=[DataRequired()])
    instituicao = StringField("instituicao", validators=[DataRequired()]) 
    capitao = StringField("capitao",validators=[DataRequired()])   

class PessoaForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    email = StringField("email", validators=[Email()])
    RG = StringField("RG", validators=[DataRequired])
    CPF = StringField("CPF", validators=[DataRequired])
    telefone = StringField("telefone", validators=[DataRequired])
    idade = StringField("idade", validators=[DataRequired()])

class RoboForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    categoria = StringField("categoria", validators=[DataRequired()])
    peso = StringField("peso", validators=[DataRequired()])
    responsavel = StringField("responsavel", validators=[DataRequired()])

class EventoForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    endereco = StringField("endereco", validators=[DataRequired()])
    email = StringField("email",validators=[DataRequired()])
    site = StringField("site",validators=[DataRequired()])
    país = StringField("país", validators=[DataRequired()])
    estado = StringField("estado", validators=[DataRequired()])
    cidade = StringField("cidade", validators=[DataRequired()])



