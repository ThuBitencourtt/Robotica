from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user
from app import app, db, lm

from app.models.tables import User, Equipe,Pessoa,Robo,Evento
from app.models.forms import LoginForm, CadastroForm,EquipeForm,PessoaForm,RoboForm,EventoForm

@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login", methods=["GET","POST"])
def login():
    form =  LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash("Login in")
            return redirect(url_for("index"))
        else:
            flash("Invalid Login")
    return render_template('login.html',
                            form=form)

@app.route("/logout")
def logout():
    logout_user()
    flash ("Logged out")
    return redirect(url_for("login"))

@app.route("/cadastro", methods=["GET","POST"])
@app.route("/")
def cadastro():
    form = CadastroForm()
    if request.form:
        user = User(username=request.form.get("username"),password=request.form.get("password"))
        db.session.add(user)
        db.session.commit()
    return render_template('cadastro.html',
                            form=form)

@app.route("/cadastro_equipe", methods=["GET","POST"])
@app.route("/")
def cadastro_equipe():
    form = EquipeForm()
    if request.form:
        equipe = Equipe(firstname=request.form.get("firstname"), lastname=request.form.get("lastname"),slogan=request.form.get("slogan"),email=request.form.get("email"),
        site=request.form.get("site"),país=request.form.get("país"),estado=request.form.get("estado"),
        cidade=request.form.get("cidade"),instituicao=request.form.get("instituicao"),capitao=request.form.get("capitao"))
        db.session.add(equipe)
        db.session.commit()
    return render_template('cadastro_equipe.html',
                            form=form)                        

@app.route("/cadastro_pessoa", methods=["GET","POST"])
@app.route("/")
def cadastro_pessoa():
    form = PessoaForm()
    if request.form:
        pessoa = Pessoa(name=request.form.get("name"),email=request.form.get("email"),
        RG=request.form.get("RG"),CPF=request.form.get("CPF"),telefone=request.form.get("telefone"),
        idade=request.form.get("idade"))
        db.session.add(pessoa)
        db.session.commit()
    return render_template('cadastro_pessoa.html',
                            form=form)  

@app.route("/cadastro_robo", methods=["GET","POST"])
@app.route("/")
def cadastro_robo():
    form = RoboForm()
    if request.form:
        robo = Robo(name=request.form.get("name"),email=request.form.get("categoria"),
        RG=request.form.get("peso"),CPF=request.form.get("responsavel"))
        db.session.add(robo)
        db.session.commit()
    return render_template('cadastro_robo.html',
                            form=form) 

@app.route("/cadastro_evento", methods=["GET","POST"])
@app.route("/")
def cadastro_evento():
    form = EventoForm()
    if request.form:
        evento = Evento(name=request.form.get("name"), endereco=request.form.get("endereco"),email=request.form.get("email"),
        site=request.form.get("site"),país=request.form.get("país"),estado=request.form.get("estado"),
        cidade=request.form.get("cidade"))
        db.session.add(evento)
        db.session.commit()
    return render_template('cadastro_evento.html',
                            form=form)   
