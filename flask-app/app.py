from flask import Flask, render_template, request, redirect, url_for, flash
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager, login_user, logout_user, current_user, login_required
# from wtforms import TextField, PasswordField
# from enums import *

import hashlib

# Adicionado
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms.fields import TextField, StringField, SubmitField, PasswordField
from wtforms.validators import Required
<<<<<<< HEAD
=======
from enums import *
import MySQLdb
import hashlib
>>>>>>> 769115b72b813cb085a6441ba38381899891b765

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Testando'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:mysql@localhost:3306/gerenciador_de_tarefas'

Bootstrap(app)

db = SQLAlchemy(app)

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

class Usuario(db.Model):
    contador_de_codigos = 1

    __tablename__ = 'usuario'
    codigo = db.Column('codigo',db.Integer, primary_key=True, autoincrement=True)
    login = db.Column('login',db.String)
    senha = db.Column('senha',db.String)
    email = db.Column('email',db.String)

    def __init__(self,login,senha,email):
        self._cod = contador_de_codigos
        self._login = login
        self._senha = senha
        self._email = email
        self._tarefas = []

        contador_de_codigos += 1

    def __str__(self):
        return self._login + " (" + self._email + ")"

    @property
    def cod(self):
        return self._cod

    @property
    def tarefas(self):
        return self._tarefas

    @property
    def login(self):
        return self._login
    @login.setter
    def login(self, value):
        self._login = value

    @property
    def senha(self):
        return self._senha
    @senha.setter
    def senha(self, value):
        self._senha = value

    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, value):
        self._email = value


class Tarefa(db.Model):
    __tablename__ = 'tarefa'
    codigo = db.Column('codigo',db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column('titulo',db.String)
    descricao = db.Column('descricao',db.String)
    data_limite = db.Column('data_limite',db.Date)
    status = db.Column('status',db.Integer)
    prioridade = db.Column('prioridade',db.Integer)
    usuario_codigo = db.Column('usuario_codigo',db.Integer,db.ForeignKey('usuario.codigo'))

    def __init__(self,titulo,descricao,data_limite,prioridade=Prioridade.baixa):
        self._titulo = titulo
        self._descricao = descricao
        self._data_limite = data_limite
        self._status = Status.pendente
        self._prioridade = prioridade

    def __str__(self):
        return self._titulo + " (" + self._prioridade + ")"

    @property
    def titulo(self):
        return self._titulo
    @titulo.setter
    def titulo(self, value):
        self._titulo = value

    @property
    def descricao(self):
        return self._descricao
    @descricao.setter
    def descricao(self, value):
        self._descricao = value

    @property
    def data_limite(self):
        return self._data_limite
    @data_limite.setter
    def data_limite(self, value):
        self._data_limite = value

    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, value):
        self._status = value

    @property
    def prioridade(self):
        return self._prioridade
    @prioridade.setter
    def prioridade(self, value):
        self._prioridade = value

class LoginForm(Form):
    # user = TextField('user', validators=[Required()])
    user = StringField('Usuario', validators=[Required()])
    key = PasswordField('Senha', validators=[Required()])
    submit = SubmitField('Login')

class RegisterForm(Form):
    user = TextField('Usuario', validators=[Required()])
    email = TextField('Email', validators=[Required()])
    key = PasswordField('Senha', validators=[Required()])
    key_confirm = PasswordField('Confirmacao', validators=[Required()])
    submit = SubmitField('Registrar')

@app.route("/register/")
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # user = db.session.query(User).filter_by(user=form.user.data.lower()).first()
        if user:
            flash('Usuario ja existe.')
        else:
            user = User(form.user.data.lower(), form.key.data, form.email.data)
            # db.session.add(user)
            # db.session.commit()

            login_user(user)

    if current_user.is_authenticated and not current_user.is_anonymous():
        return redirect( url_for('home') )

    return render_template('register.html', form=form, title='Register')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = form.get_user()
        if not user:
            flash('Usuario ou senha invalidos.')
        else:
            login_user(user)

    if current_user.is_authenticated():
        return redirect(url_for('home'))

    return render_template('login.html', form=form, title='Login')

@app.route("/logout/")
@login_required
def logout():
    logout_user()
    return redirect( url_for('login') )

@app.route("/")
@login_required
def home():
    return "Main Page"

@app.route("/tarefas/")
@login_required
def tarefas():
    return "Lista de tarefas"

@app.route("/tarefa/nova")
@login_required
def nova_tarefa():
    return "Nova tarefa"

@app.route("/tarefa/salvar/<tarefa>")
@login_required
def salvar_tarefa(tarefa):
    return "Salvar tarefa"

@app.route("/tarefa/remover/<id>")
@login_required
def remover_tarefa(id):
    return "Remover tarefa"

@app.route("/tarefa/<id>")
@login_required
def detalhar_tarefa(id):
    return "Detalhar tarefa"

@app.route("/tarefa/editar/<id>")
@login_required
def editar_tarefa(id):
    return "Editar tarefa"

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
