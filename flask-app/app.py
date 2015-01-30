from flask import Flask, render_template, request, redirect, url_for, flash
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager, login_user, logout_user, current_user, login_required
from flask.ext.wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import Required
from enums import *
import hashlib

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Testando'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:mysql@localhost[:3306]/gerenciador_de_tarefas'

db = SQLAlchemy(app)

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

class Tarefa:
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

class Usuario:
    contador_de_codigos = 1

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


class LoginForm(Form):
    user = TextField('user', validators=[Required()])
    key = PasswordField('key', validators=[Required()])

@app.route("/")
def home():
    return "Main Page"

@app.route("/register/")
def register():
    return "Registro"

@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = form.get_user()
        if not user:
            flash('Invalid User or Key.')
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

app.run(debug=True)