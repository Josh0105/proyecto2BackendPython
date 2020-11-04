from Comentario import Comentario
import json

class Juego:
    #CONSTRUCTOR DE JUEGO
    def __init__ (self,id,nombre,anio,precio,categoria1,categoria2,categoria3,foto,banner,descripcion):
        self.id = id
        self.nombre = nombre
        self.anio = anio
        self.precio = precio
        self.categoria1 = categoria1
        self.categoria2 = categoria2
        self.categoria3 = categoria3
        self.foto = foto
        self.banner = banner
        self.descripcion = descripcion
        self.comentarios = []
    
    #modifica los datos del juego, excepto comentarios
    def modificar_Juego(self,nombre,anio,precio,categoria1,categoria2,categoria3,foto,banner,descripcion):
        self.nombre = nombre
        self.anio = anio
        self.precio = precio
        self.categoria1 = categoria1
        self.categoria2 = categoria2
        self.categoria3 = categoria3
        self.foto = foto
        self.banner = banner
        self.descripcion = descripcion
    
    #agrega un comentario a la lista de comentarios
    def agregar_Comentario(self,cadena,idUser,fecha):
        self.comentarios.append(Comentario(cadena,idUser,fecha))

    #devuelve los comentarios en formato json
    def devolver_comentarios(self):
        return json.dumps([comentario.dump() for comentario in self.comentarios])

    #muestra el usuario en formato json
    def dump(self):

        return{
            'id': self.id,
            'nombre': self.nombre,
            'año': self.anio,
            'precio': self.precio,
            'categoria1': self.categoria1,
            'categoria2': self.categoria2,
            'categoria3': self.categoria3,
            'foto' : self.foto,
            'banner' : self.banner,
            'descripcion' : self.descripcion
        }

    #muestra los datos del juego en consola
    def mostrar(self):

        print("id: " + str(self.id))
        print("nombre: " + self.nombre)
        print("año: " + str(self.anio))
        print("precio: " + str(self.precio))
        print("categoria1: " + self.categoria1)
        print("categoria1: " + self.categoria2)
        print("categoria1: " + self.categoria3)
        print("foto; " + self.foto)
        print("banner; " + self.banner)
        print("descripcion; " + self.descripcion)