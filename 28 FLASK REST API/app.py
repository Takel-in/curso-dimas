#FLASK - REST API con SQLite y SQLAlchemy

from flask import Flask, jsonify, request
from Models import db, Streamers
from logging import exception

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "streamers.db"



app = Flask(__name__) #__name__ es el fichero actual.
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database\\streamers.db"
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_PATH.as_posix()}"


app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] =False


db.init_app(app) #Con esto sabe a que base de datos se debe conectar que lo hemos echo en Models.py

print("CONFIG:", app.config["SQLALCHEMY_DATABASE_URI"])
print("INSTANCE:", app.instance_path)
with app.app_context():
    print("DATABASE:", db.engine.url.database)

#Aqui empiezan las rutas.
@app.route("/")  #Indica donde se tiene que ejecutar la función que en este caso es en la raiz de la aplicación 
def home():
    return "<h1>Welcome Home</h1>"

@app.route("/api/streamers", methods=["GET"])
def getStreamers():
    try:        
        streamers = Streamers.query.all()
        # El bucle for funciona como siemre y lo que hace es recorre el resultado obtenido en streamers.
        # Lo que hace es con cada objeto se llama a serialize que lo que hacía eera devolver la lista en formato diccionario
        # por lo tanto toreturn será un lista de 5 diccionarios.
        toreturn =  [streamer.serialize() for streamer in streamers ]
        #La líenea anterior sería equivalente a realizar.
             #for streamer in streamers:
             #toReturn.append(streamer.serialize)
        return jsonify(toreturn), 200
#        for streamer in streamers:
#            print(streamer)

    except Exception:
        print ("[SERVER]: error")
        exception("[SERVER]: error -> ")
        return jsonify ({"msg": "Ha ocurrido un error"}), 500

    #return "<h1>Success</h1>"

@app.route("/api/streamer", methods=["GET"])
def getStreamerByName():
    #Pasamos el valor que queremos en la ruta con clave=valor en este caso name=alexelcapo   - Sa separación entre ruta y valores con un ?
    try:  
        nameStreamer = request.args["name"] #Esto nos ventra de la URL.
        streamer = Streamers.query.filter_by(name=nameStreamer).first()
        if not streamer:
             return jsonify ({"msg": "Este strimer no existe"}), 200
        else:
            return jsonify(streamer.serialize()), 200

    except Exception:
        print ("[SERVER]: error")
        exception("[SERVER]: error -> ")
        return jsonify ({"msg": "Ha ocurrido un error"}), 500


@app.route("/api/findstreamer", methods=["GET"])
def getStreamer():
    #Pasamos el valor que queremos en la ruta con clave=valor en este caso name=alexelcapo   - Sa separación entre ruta y valores con un ?
    try:  
        fields = {} 
        if "name" in request.args:
            fields["name"] = request.args["name"]

        if "subs" in request.args:
            fields["subs"] = request.args["subs"]

        if "followers" in request.args:
            fields["followers"] = request.args["followers"]

        ##Recordar que el ** desempaqueta el diccionario 
        streamer = Streamers.query.filter_by(**fields).first()
        if not streamer:
             return jsonify ({"msg": "Este strimer no existe"}), 200
        else:
            return jsonify(streamer.serialize()), 200

    except Exception:
        print ("[SERVER]: error")
        exception("[SERVER]: error -> ")
        return jsonify ({"msg": "Ha ocurrido un error"}), 500

    #return "<h1>Success</h1>"





if __name__ == "__main__":
    app.run(debug=True, port=4000)

    