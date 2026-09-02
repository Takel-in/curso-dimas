# Aqui replicamos el modelo a la base de datos 
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Streamers(db.Model):  #Definimo una clase con el nombre de una tabla y le indicamo que ba a se de tipo modelo.
    #Generamos atributos de la clase con el mismo nombre de la columnas de la tabla.
    rowid = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200), unique = True, nullable=False) #200 es el límite de caracteres que onemos al campo
    subs = db.Column(db.Integer)
    followers = db.Column(db.Integer)