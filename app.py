from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from Usuario import Usuario
from CRUD_Usuarios import CRUD_Usuarios
from CRUD_VideoJuego import CRUD_VidoJuego
import os
from werkzeug.utils import secure_filename

var_Usuarios = CRUD_Usuarios()
var_Juegos = CRUD_VidoJuego()
var_Juegos.cargaMasiva("C:\\Users\\Jonathan Calo\\Desktop\\datosJuegos1.csv")
var_Juegos.listar_Juegos()

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = './instance'
#uploads_dir = os.path.join(app.instance_path, 'uploads')
#try:
#    os.makedirs(uploads_dir)
#except OSError:
#    if not os.path.isdir(uploads_dir):
#        raise



@app.route("/upload", methods=['POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['archivo']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return "<h1>Archivo subido exitosamente</h1>"

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

@app.route('/registro', methods =["POST"])
def registro():
    if request.method == 'POST':

        response = {}

        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        userName = request.form.get('user_name')
        contrasena = request.form.get('contrasena')
        contrasena2 = request.form.get('contrasena2')

        estadoCreacion = var_Usuarios.crear_Usuario(nombre,apellido,userName,contrasena,contrasena2)

        response['estado_creacion'] = estadoCreacion
        return response

@app.route('/recuperar',methods =["POST"])
def recuperar():
    if request.method == 'POST':
        response = {}

        userName = request.form.get('user_name')

        usuarioRecuperar = var_Usuarios.recuperar_Contrasena(userName)

        if usuarioRecuperar is not False:
            response['contrasena'] = usuarioRecuperar.contrasena
            response['estado'] = 1
            return response
        response['estado'] = 0
        return response

@app.route('/obtener-todos-juegos')
def obtenerTododosJuegos():
    return var_Juegos.devolver_Juegos()

@app.route("/")
def index():
    return "<h1>Bienvenido</h1>"

if __name__ == "__main__":
    app.run(threaded=True, port=5000, debug=True)