from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from Usuario import Usuario
from CRUD_Usuarios import CRUD_Usuarios
from CRUD_VideoJuego import CRUD_VidoJuego
import os
from werkzeug.utils import secure_filename

var_Usuarios = CRUD_Usuarios()
var_Juegos = CRUD_VidoJuego()
var_Juegos.crearJuego("Grand Theft Auto V","2012","150.90","","","","https://tecnogaming.com/wp-content/uploads/2013/04/GTA-V-portada.jpg","https://samwallbutton.files.wordpress.com/2014/10/gta-v-banner.png","Grand Theft Auto V es un videojuego de acción-aventura de mundo abierto desarrollado por el estudio Rockstar North y distribuido por Rockstar Games. Fue lanzado el 17 de septiembre de 2013 para las consolas PlayStation 3 y Xbox 360")
var_Juegos.crearJuego("Uncharted: The Nathan Drake Collection","2016","300.90","acción","Aventura","","https://i1.wp.com/regionps.com/wp-content/uploads/2018/11/El-arte-de-uncharted-portada.jpg?ssl=1","https://i1.wp.com/reliveandplay.com/wp-content/uploads/uncharted-4-banner.jpg","Uncharted: The Nathan Drake Collection es una colección remasterizada de los juegos creados por el estudio de desarrollo norteamericano Naughty Dog, Uncharted: El tesoro de Drake, Uncharted 2: El reino de los ladrones y Uncharted 3: La traición de Drake. El juego, en su lanzamiento, incluía un código para la beta multijugador de Uncharted 4: El desenlace del ladrón, juego que llegó en exclusiva a PlayStation 4 el 10 de mayo de 2016. La beta estuvo disponible para los usuarios del 4 al 13 de diciembre de 2015.")
var_Juegos.crearJuego("The Last of Us","2013","140.00","Multijugador","","C3","https://media.playstation.com/is/image/SCEA/the-last-of-us-remastered-two-column-02-ps4-us?$TwoColumn_Image$","https://cdn.gamecloud.net.au/wp-content/uploads/2013/12/the-last-of-us-special-banner.jpg","The Last of Us es un videojuego de acción-aventura y horror de supervivencia desarrollado por la compañía estadounidense Naughty Dog y distribuido por Sony Computer Entertainment para la consola PlayStation 3 en 2013. La trama describe las vivencias de Joel y Ellie, un par de supervivientes de una pandemia en Estados Unidos que provoca la mutación de los seres humanos en criaturas caníbales.")
var_Juegos.crearJuego("The Last of Us Part II","2020","600.00","Un jugador","Aventura","","https://s3.gaming-cdn.com/images/products/6215/orig/the-last-of-us-part-ii-cover.jpg","https://i.redd.it/yolzhibhvvfy.jpg","The Last of Us Part II es un videojuego de acción-aventura y horror de supervivencia desarrollado por Naughty Dog, publicado por Sony en exclusiva para la PlayStation 4 el 19 de junio de 2020.")
var_Juegos.crearJuego("Juego 5","2012","150.90","Acción","Aventura","C3","https://tecnogaming.com/wp-content/uploads/2013/04/GTA-V-portada.jpg","https://samwallbutton.files.wordpress.com/2014/10/gta-v-banner.png","Grand Theft Auto V es un videojuego de acción-aventura de mundo abierto desarrollado por el estudio Rockstar North y distribuido por Rockstar Games. Fue lanzado el 17 de septiembre de 2013 para las consolas PlayStation 3 y Xbox 360")
#var_Usuarios.agregarABiblioteca(0,2)
#var_Usuarios.agregarABiblioteca(0,3)
#var_Usuarios.agregarABiblioteca(0,5)
#var_Juegos.buscar_Juegos("a")
#var_Juegos.buscar_Juegos("Accion")
#var_Juegos.buscar_Juegos("AcciÓn")
#var_Juegos.buscar_Juegos("Accion ")
#var_Juegos.buscar_Juegos(" ")
#var_Juegos.devolver_Juegos_Lista(var_Usuarios.misUsuarios[0].biblioteca)
#var_Juegos.nuevoComentario("CADENA1","admin","HOY",1)
#var_Juegos.nuevoComentario("CADENA2","admin","HOY",1)
#var_Juegos.nuevoComentario("CADENA3","admin","HOY",1)

#var_Juegos.cargaMasiva("C:\\Users\\Jonathan Calo\\Desktop\\datosJuegos1.csv")
var_Juegos.listar_Juegos()

app = Flask(__name__)
CORS(app)
#app.config['UPLOAD_FOLDER'] = './instance'
#uploads_dir = os.path.join(app.instance_path, 'uploads')
#try:
#    os.makedirs(uploads_dir)
#except OSError:
#    if not os.path.isdir(uploads_dir):
#        raise

#@app.route("/upload", methods=['POST'])
#def uploader():
#    if request.method == 'POST':
#        f = request.files['archivo']
#        filename = secure_filename(f.filename)
#        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#        return "<h1>Archivo subido exitosamente</h1>"

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

@app.route('/agregar-comentario', methods = ["POST"])
def agregarComent():
    if request.method == "POST":
        response = {}

        idUser = int(request.form.get('id_usuario'))
        nombreUsuario = var_Usuarios.devolver_nombre_usuario(idUser)
        idJuego = int(request.form.get('id_juego'))
        comentario = request.form.get('comentario')
        fecha = request.form.get('fecha')

        estadoAgregado = var_Juegos.nuevoComentario(comentario,nombreUsuario,fecha,idJuego)
        
        response['comentario_agregado'] = estadoAgregado
        return response

@app.route('/agregar-a-biblioteca', methods = ["POST"])
def agregarABiblioteca():
    if request.method == "POST":
        response = {}

        idUser = int(request.form.get('id_usuario'))
        idJuego = int(request.form.get('id_juego'))

        estadoAgregado = var_Usuarios.agregarABiblioteca(idUser,idJuego)
        
        response['estado_agregado'] = estadoAgregado
        return response

@app.route('/modificar-usuario', methods =["POST"])
def modificarUsuario():
    if request.method == 'POST':

        response = {}

        id = int(request.form.get('id_usuario'))
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        userName = request.form.get('user_name')
        contrasena = request.form.get('contrasena')
        contrasena2 = request.form.get('contrasena2')

        estadoCreacion = var_Usuarios.modificar_Usuario(id,nombre,apellido,userName,contrasena,contrasena2)

        response['estado_creacion'] = estadoCreacion
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

@app.route('/buscar',methods =["POST"])
def buscar():
    if request.method == 'POST':
        response = {}

        valor = request.form.get('valor')

        resultadoBusqueda = var_Juegos.buscar_Juegos(valor)
        response['resultados'] = resultadoBusqueda
        return response

@app.route('/obtener-resultado-busqueda')
def obtenerResultadoBusqueda():
    return var_Juegos.devolver_Juegos_Lista(var_Juegos.resultadoBusqueda)


@app.route('/obtener-datos-usuario')
def obtenerDatosUser():
    id = int(request.args.get('id',None))
    print("se obtubo id")
    return var_Usuarios.devolver_datos_usuario(id)

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

@app.route('/obtener-mi-biblioteca')
def obtenerMiBiblioteca():
    id = int(request.args.get('id',None))
    print("se obtubo id")
    return var_Juegos.devolver_Juegos_Lista(var_Usuarios.misUsuarios[id].biblioteca)

@app.route('/obtener-todos-comentarios')
def obtenerTododosComentarios():
    id = int(request.args.get('id',None))
    print("se obtubo id")
    coments = var_Juegos.devolver_ComentariosJuego(id)
    
    if coments is not False:
        return coments


@app.route('/obtener-juego')
def obtener_juego():
    id = int(request.args.get('id',None))
    print("se mandó id")
    game = var_Juegos.devolver_Juego(id)

    if game is not None:
        return{
            'estado': 1,
            'data' : game
        }


@app.route("/")
def index():
    return "<h1>Bienvenido</h1>"

if __name__ == "__main__":
    app.run(threaded=True, port=5000, debug=True)