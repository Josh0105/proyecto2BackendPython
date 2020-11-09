from flask import Flask, request, jsonify
from flask_cors import CORS
from Usuario import Usuario
from CRUD_Usuarios import CRUD_Usuarios
from CRUD_VideoJuego import CRUD_VidoJuego

#CREAMOS EL CRUD DE USUARIOS Y DE VIDEO JUEGOS
var_Usuarios = CRUD_Usuarios()
var_Juegos = CRUD_VidoJuego()

app = Flask(__name__)
CORS(app)

#ENDPOINT DE LOGIN
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
            response['admin'] = usuario.admin
            return response
        response['estado'] = 0
        return response

#ENDPOINT DE AGREGAR COMENTARIO
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

#ENDPOINT DE AGREGAR JUEGO A BIBLIOTECA
@app.route('/agregar-a-biblioteca', methods = ["POST"])
def agregarABiblioteca():
    if request.method == "POST":
        response = {}

        idUser = int(request.form.get('id_usuario'))
        idJuego = int(request.form.get('id_juego'))

        estadoAgregado = var_Usuarios.agregarABiblioteca(idUser,idJuego)
        
        response['estado_agregado'] = estadoAgregado
        return response

#ENDPOINT DE MODIFICAR USUARIO
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

#ENDPOINT DE MODIFICAR LOS DATOS DE UN JUEGO
@app.route('/modificar-juego', methods =["POST"])
def modificarJuego():
    if request.method == 'POST':

        response = {}

        id = int(request.form.get('id_juego'))
        nombreJuego = request.form.get('nombre_juego')
        anio = request.form.get('anio')
        precio = request.form.get('precio')
        cat1 = request.form.get('categoria_1')
        cat2 = request.form.get('categoria_2')
        cat3 = request.form.get('categoria_3')
        foto = request.form.get('foto')
        banner = request.form.get('banner')
        descripcion = request.form.get('descripcion')

        estadoCreacion = var_Juegos.modificarJuego(id,nombreJuego,anio,precio,cat1,cat2,cat3,foto,banner,descripcion)

        response['estado_creacion'] = estadoCreacion
        return response

#ENDPOINT PARA CREACION DE UN JUEGO NUEVO
@app.route('/nuevo-juego', methods =["POST"])
def nuevoJuego():
    if request.method == 'POST':

        response = {}

        nombreJuego = request.form.get('nombre_juego')
        anio = request.form.get('anio')
        precio = request.form.get('precio')
        cat1 = request.form.get('categoria_1')
        cat2 = request.form.get('categoria_2')
        cat3 = request.form.get('categoria_3')
        foto = request.form.get('foto')
        banner = request.form.get('banner')
        descripcion = request.form.get('descripcion')

        estadoCreacion = var_Juegos.crearJuego(nombreJuego,anio,precio,cat1,cat2,cat3,foto,banner,descripcion)

        response['estado_creacion'] = estadoCreacion
        return response

#ENDPOINT PARA REGISTRO DE UN USUARIO CLIENTE
@app.route('/registro', methods =["POST"])
def registro():
    if request.method == 'POST':

        response = {}

        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        userName = request.form.get('user_name')
        contrasena = request.form.get('contrasena')
        contrasena2 = request.form.get('contrasena2')

        estadoCreacion = var_Usuarios.crear_Usuario(nombre,apellido,userName,contrasena,contrasena2,False)

        response['estado_creacion'] = estadoCreacion
        return response

#ENDPOINT PARA REGISTRO DE UN USUARIO ADMINISTRADOR
@app.route('/registro-admin', methods =["POST"])
def registroAdmin():
    if request.method == 'POST':

        response = {}

        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        userName = request.form.get('user_name')
        contrasena = request.form.get('contrasena')
        contrasena2 = request.form.get('contrasena2')

        estadoCreacion = var_Usuarios.crear_Usuario(nombre,apellido,userName,contrasena,contrasena2,True)

        response['estado_creacion'] = estadoCreacion
        return response

#ENDPOINT PARA ELIMINAR UN JUEGO DE LA LISTA
@app.route('/eliminar-juego', methods =["POST"])
def eliminar_Juego():
    if request.method == 'POST':

        response = {}

        id = int(request.form.get('id_juego'))

        estadoCreacion = var_Juegos.eliminarJuego(id)

        response['estado_creacion'] = estadoCreacion
        return response

#ENDPOINT PARA BUSCAR UN JUEGO POR CATEGORIA
@app.route('/buscar',methods =["POST"])
def buscar():
    if request.method == 'POST':

        response = {}

        valor = request.form.get('valor')

        resultadoBusqueda = var_Juegos.buscar_Juegos(valor)
        
        response['resultados'] = resultadoBusqueda
        return response

#ENDPOINT PARA OBTENER LOS RESULTADOS DE UNA BUSQUEDA POR CATEGORIA
@app.route('/obtener-resultado-busqueda')
def obtenerResultadoBusqueda():
    return var_Juegos.devolver_Juegos_Lista(var_Juegos.resultadoBusqueda)

#ENDPOINT PARA OBTENER TODOS LOS DATOS DE UN USUARIO
@app.route('/obtener-datos-usuario')
def obtenerDatosUser():
    id = int(request.args.get('id',None))
    print("se obtubo id")
    return var_Usuarios.devolver_datos_usuario(id)

#ENDPOINT PARA RECUPERAR CONTRASEÑA
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

#ENDPOINT PARA OBTENER LOS DATOS DE TODOS LOS JUEGOS
@app.route('/obtener-todos-juegos')
def obtenerTododosJuegos():
    return var_Juegos.devolver_Juegos()

#ENDPOINT PARA OBTENER LOS DATOS DE TODOS LOS USUARIOS
@app.route('/obtener-todos-usuarios')
def obtenerTododosUsuarios():
    return var_Usuarios.devolver_Usuarios()

#ENDPOINT PARA OBTENER LOS JUEGOS DE LA BIBLIOTECA DE UN USUARIO
@app.route('/obtener-mi-biblioteca')
def obtenerMiBiblioteca():
    id = int(request.args.get('id',None))
    print("se obtubo id")
    return var_Juegos.devolver_Juegos_Lista(var_Usuarios.misUsuarios[id].biblioteca)

#ENDPOINT PARA OBTENER TODOS LOS COMENTARIOS DE UN JUEGO
@app.route('/obtener-todos-comentarios')
def obtenerTododosComentarios():
    id = int(request.args.get('id',None))
    print("se obtubo id")
    coments = var_Juegos.devolver_ComentariosJuego(id)
    
    if coments is not False:
        return coments

#ENDPOINT PARA OBTENER LOS DATOS DE UN JUEGO
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

#ENDPOINT DEFAULT
@app.route("/")
def index():
    return "<h1>Bienvenido</h1>"

if __name__ == "__main__":
    app.run(threaded=True, port=5000, debug=True)