from app import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique = True)
    password = db.Column(db.String)

    @property
    def is_authenticated(self):
            return True

    @property
    def is_active(self):
            return True

    @property
    def is_anonymos(self):
            return False

    def get_id(self):
        return str(self)

    def __init__(self ,username,  password):
        self.username = username
        self.password = password
   
    def __repr__(self):
         return "<User %r>" % self.username
    
#class Capitao(db.Model):
#    __tablename__ = "capitoes"
#    id = db.Column(db.Integer, primary_key = True)
#    name = db.Column (db.String, unique = True)
#    identificacao = db.Column (db.String, unique = True)
#    email = db.Column(db.String, unique= True)
#
#    def __init__(self ,name,  identificacao, email):
#        self.name = name
#        self.identificacao = identificacao
#        self.email = email
#
#    def __repr__(self):
#         return "<Capitao %r>" % self.name


class Equipe(db.Model):
    __tablename__ = "Equipes"
    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column (db.String, unique = True)
    lastname = db.Column (db.String, unique = True)
    slogan = db.Column(db.String, unique = True)
    email = db.Column(db.String, unique = True)
    site = db.Column(db.String, unique = True)
    país = db.Column(db.String)
    estado = db.Column(db.String)
    cidade = db.Column(db.String)
    instituicao = db.Column(db.String)
    capitao = db.Column(db.String)

    def __init__(self, firstname, lastname,slogan, email, site, país, estado, cidade, instituicao, capitao):
        self.firstname = firstname
        self.lastname = lastname
        self.slogan = slogan
        self.email = email
        self.site = site
        self.país = país
        self.estado = estado
        self.cidade = cidade
        self.instituicao = instituicao
        self.capitao = capitao

    def __repr__(self):
         return "<Equipe %r>" % self.lastname

class Pessoa(db.Model):
    __tablename__ = "Pessoas"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column (db.String, unique = True)
    RG = db.Column(db.String, unique = True)
    CPF = db.Column(db.String, unique = True)
    telefone = db.Column(db.String, unique = True)
    email = db.Column(db.String, unique= True)
    idade = db.Column(db.String)

    def __init__(self ,name,email, RG,CPF, telefone, idade):
        self.name = name
        self.email = email
        self.RG = RG
        self.CPF = CPF
        self.telefone = telefone
        self.idade = idade

    def __repr__(self):
         return "<Pessoa %r>" % self.name

class Robo(db.Model):
    __tablename__ = "Robos"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column (db.String, unique = True)
    categoria = db.Column(db.String)
    peso = db.Column(db.String)
    responsavel = db.Column(db.String)

    def __init__(self ,name, categoria, peso, responsavel):
        self.name = name
        self.categoria = categoria
        self.peso = peso
        self.responsavel = responsavel

    def __repr__(self):
        return "<Robo %r>" % self.name

class Evento(db.Model):
    __tablename__ = "Eventos"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column (db.String, unique = True)
    endereco = db.Column (db.String, unique = True)
    email = db.Column(db.String, unique = True)
    site = db.Column(db.String, unique = True)
    país = db.Column(db.String)
    estado = db.Column(db.String)
    cidade = db.Column(db.String)
    

    def __init__(self, name, endereco, email, site, país, estado, cidade):
        self.name = name
        self.endereco = endereco
        self.email = email
        self.site = site
        self.país = país
        self.estado = estado
        self.cidade = cidade
       

    def __repr__(self):
         return "<Evento %r>" % self.name