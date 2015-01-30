from flask import Flask, render_template, request, redirect, url_for, flash
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager, login_user, logout_user, current_user, login_required
from flask.ext.wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import Required
import hashlib

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Testando'

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

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