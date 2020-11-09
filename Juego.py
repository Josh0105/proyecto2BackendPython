from Comentario import Comentario
import unicodedata
import json

#DEFINIMOS LA CLASE JUEGO
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
    def agregar_Comentario(self,cadena,UserName,fecha):
        self.comentarios.append(Comentario(cadena,UserName,fecha))
    
    #devuelve el id del juego si coincide alguna categoria
    def comprobar_categoria(self,valor):
        if unicodedata.normalize('NFKD', self.categoria1).encode('ASCII', 'ignore').strip().lower() == unicodedata.normalize('NFKD', valor).encode('ASCII', 'ignore').strip().lower():
            if self.categoria1 != "":
                return self.id
        if unicodedata.normalize('NFKD', self.categoria2).encode('ASCII', 'ignore').strip().lower() == unicodedata.normalize('NFKD', valor).encode('ASCII', 'ignore').strip().lower():
            if self.categoria2 != "":
                return self.id
        if unicodedata.normalize('NFKD', self.categoria3).encode('ASCII', 'ignore').strip().lower() == unicodedata.normalize('NFKD', valor).encode('ASCII', 'ignore').strip().lower():
            if self.categoria3 != "":
                return self.id
        return False

    #devuelve TODOS los comentarios de un juego en formato json
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