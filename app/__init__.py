from flask import Flask
from flask import render_template, request, flash, redirect, url_for

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

app = Flask(__name__)
app.config['SECRET_KEY'] = "key"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root@localhost/test"


# class Funcionario(db.Model):
#     __tablename__='funcionario'

#     _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     nome = db.Column(db.String(50))
#     email = db.Column(db.String(100))

#     def __init__(self, nome, email):
#         self.nome = nome
#         self.email = email

# db.create_all()

# f = Funcionario("nome", "email")
# db.session.add(f)
# db.session.commit()


from app import routes
