# Aqui replicamos el modelo a la base de datos 
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Streamers(db.Model):  #Definimo una clase con el nombre de una tabla y le indicamo que ba a se de tipo modelo.
    #Generamos atributos de la clase con el mismo nombre de la columnas de la tabla.
    rowid = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200), unique = True, nullable=False) #200 es el límite de caracteres que onemos al campo
    subs = db.Column(db.Integer)
    followers = db.Column(db.Integer)

    def __init__(self, name, subs, followers):
        super().__init__()
        self.name = name
        self.subs = subs
        self.followers = followers

    #Sobreescribimo el método str que imprime los datos.
    def __str__(self):
        return "\nNombre: {}. Subs: {}. Followers: {}".format(
            self.name,
            self.subs,
            self.followers
        )

    # REtorna el conenido de la tabla en formato diccionario.
    def serialize(self):  
        return {
            "rowid": self.rowid,
            "name": self.name,
            "subs": self.subs,
            "followers": self.followers
        }

    