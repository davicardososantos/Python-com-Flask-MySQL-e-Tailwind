from app import app
from flask import render_template, request, flash, redirect, url_for

from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import DeclarativeBase

db = SQLAlchemy(app)

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    instagram = db.Column(db.String(40))
    email = db.Column(db.String(120), unique=True)
    tel = db.Column(db.String(80))

    def __init__(self, name, instagram, email, tel):
        self.name = name
        self.instagram = instagram
        self.email = email
        self.tel = tel

    def __repr__(self):
        return '<User %r>' % self.name

@app.route('/', defaults={"theme":"dark"})
@app.route('/index', defaults={"theme":"dark"})
@app.route('/index/<theme>')
def index(theme):    
    return render_template('index.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/lista')
def lista():
    clients = Client.query.all()
    print(clients)
    return render_template('lista.html', clients=clients)

@app.route('/save', methods=['POST'])
def save():
    # Se for o methods GET, faça assim: request.args.get('name')
    name = request.form.get('name')
    instagram = request.form.get('instagram')
    email = request.form.get('email')
    tel = request.form.get('tel')    
    db.create_all()    
    hasClient = Client.query.filter_by(email=email).first()
    print(hasClient)
    if(hasClient == None):
        db.session.add(Client(name, instagram, email, tel))
        db.session.commit()
        flash("{} salvo com sucesso".format(name))
        return redirect('/lista')
    else:
        flash("E-mail {} já cadastrado".format(email))
        return redirect('/cadastro')
    
@app.route("/delete/<int:id>")
def delete(id):
    client = Client.query.filter_by(id=id).first()
    print(client)
    db.session.delete(client)   
    db.session.commit() 
    flash("Registro do(a) {} apagado com sucesso".format(client.name))
    return redirect('/lista')

@app.route("/update/<int:id>", methods=['GET', 'POST'])
def atualizar(id):
    client = Client.query.filter_by(id=id).first()

    if request.method == 'POST':
        name = request.form.get("name")
        instagram = request.form.get("instagram")
        email = request.form.get("email")
        tel = request.form.get("tel")
        client.name = name
        client.instagram = instagram
        client.email = email
        client.tel = tel
        db.session.commit()
        flash("{} atualizado com sucesso".format(name))
        return redirect(url_for("lista"))

    return render_template("atualizar.html", client=client)