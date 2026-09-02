#FLASK - REST API con SQLite y SQLAlchemy

from flask import Flask
from Models import db, Streamers


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

@app.route("/api/streamers")
def getStreamers():
    streamers = Streamers.query.all()
    print(streamers)
    return "<h1>Success</h1>"

if __name__ == "__main__":
    app.run(debug=True, port=4000)

    