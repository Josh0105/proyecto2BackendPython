from flask import Flask, request, jsonify
from flask_cors import CORS
from Usuario import Usuario
from CRUD_Usuarios import CRUD_Usuarios
from CRUD_VideoJuego import CRUD_VidoJuego

var_Usuarios = CRUD_Usuarios()

app = Flask(__name__)
CORS(app)

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':

        response = {}

        nombre = request.form.get('nombre_usuario')
        passw = request.form.get('passw_usuario')

        usuario = var_Usuarios.autenticar_Usuario(nombre,passw)

        if usuario is not False:
            response['id'] = usuario.id
            response['usuario'] = usuario.nombre
            response['estado'] = 1

            return response
        
        response['estado'] = 0
        return response


@app.route("/")
def index():
    return "<h1>Bienvenido</h1>"

if __name__ == "__main__":
    app.run(threaded=True, port=5000, debug=True)