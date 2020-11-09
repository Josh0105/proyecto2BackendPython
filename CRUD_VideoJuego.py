from Juego import Juego
import json

#DEFINIMOS LA CLASE CRUD_VidoJuego
class CRUD_VidoJuego:
    #CONSTRUCTOR CRUD_VidoJuego
    #Se define una lista de la clase juegos
    #una lista de busqueda y un contador de juegos
    def __init__(self):
        self.listaJuegos = []
        self.resultadoBusqueda = []
        self.contador = 0
    
    #Agregua un nuevo comentario
    def nuevoComentario(self,cadena,UserName,fecha,id):
        for juego in self.listaJuegos:
            if juego.id == id:
                juego.agregar_Comentario(cadena,UserName,fecha)
                print("comentario agregado correctamente")
                return 1
        print("error al agregar comentario")
        return 0

    #Crea cada uno de los juegos
    def crearJuego(self,nombre,anio,precio,categoria1,categoria2,categoria3,foto,banner,descripcion):
        try:
            self.contador += 1
            self.listaJuegos.append(Juego(self.contador,nombre,anio,precio,categoria1,categoria2,categoria3,foto,banner,descripcion))
            return True
        except:
            return False
    
    #Modifica un juego
    def modificarJuego(self,id,nombre,anio,precio,categoria1,categoria2,categoria3,foto,banner,descripcion):
        try:
            for juego in self.listaJuegos:
                if juego.id == id:
                    juego.modificar_Juego(nombre,anio,precio,categoria1,categoria2,categoria3,foto,banner,descripcion)
                    return True
            return False
        except:
            return False
    
    #Elimina un juego según su id
    def eliminarJuego(self,id):
        #si el id coincide con el id de la lista se elimina
        for juego in self.listaJuegos:
            if juego.id == id:
                self.listaJuegos.remove(juego)
                return True
            #self.contadorPosicion += 1
        return False
    
    #Recibe un id de juego y devuelve los datos en formato Json
    def devolver_Juego(self,id):
        for juego in self.listaJuegos:
            if juego.id==id:
                return juego.dump()
        return False

    #construlle y retorna un arreglo con los id's de una categoria buscada
    def buscar_Juegos(self,valor):
        try:
            self.resultadoBusqueda = []
            for juego in self.listaJuegos:
                identificador = juego.comprobar_categoria(valor)
                if identificador is not False:
                    self.resultadoBusqueda.append(identificador)
            for elemento in self.resultadoBusqueda:
                print(elemento)
            print(self.resultadoBusqueda.__len__())
            return self.resultadoBusqueda.__len__()
        except:
            print("error en la busqueda")
    
    #devuelve los juegos de una lista de id's en formato json
    def devolver_Juegos_Lista(self,listado):
        try:
            listadojuegos=[]
            for dato in listado:
                for juego in self.listaJuegos:
                    if juego.id == dato:
                        listadojuegos.append(juego)
            print("listado creado exitosamente")
            return json.dumps([juego.dump() for juego in listadojuegos])
        except:
            print("error en la lectura de la biblioteca")

    #devuelve todos juegos en formato json
    def devolver_Juegos(self):
        return json.dumps([juego.dump() for juego in self.listaJuegos])

    #devuelve los comentarios de un juego en formato json
    def devolver_ComentariosJuego(self,id):
        for juego in self.listaJuegos:
            if juego.id == id:
                return juego.devolver_comentarios()
        return False