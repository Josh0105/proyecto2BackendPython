from Juego import Juego
import json
import csv

class CRUD_VidoJuego:
    #CONSTRUCTOR CRUD
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
    
    #Elimina un juego
    def eliminarJuego(self,id):
        self.conteoLista = 0
        for juego in self.listaJuegos:
            if juego.id == id:
                self.listaJuegos.pop(self.conteoLista)
            self.conteoLista += 1
        return False
    
    #método para carga masiva de juegos
    def cargaMasiva(self,ruta):
        try:
            #abrimos la ruta
            with open (ruta,newline="") as File:
                reader = csv.reader(File)
                #contador de lineas
                self.conteoLineas = 0
                #para cada una de las lineas
                for row in reader:
                    #el if es para no tomar en cuenta la primera linea
                    if self.conteoLineas > 0: 
                        print(row)
                        #ESTA LINEA CREA EL JUEGO
                        self.crearJuego(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
                    self.conteoLineas +=1
        except Exception as e:
            print(e)
            print("no se pudo realizar la lectura")
            return False
    
    #lista los juegos en consola
    def listar_Juegos(self):
        for juego in self.listaJuegos:
            print("index" + str(self.listaJuegos.index(juego)) + "\tid:" + str(juego.id) + "\t" + juego.nombre + "\t" + str(juego.anio) + "\t" + str(juego.precio) + "\t" + juego.categoria1 + "\t" + juego.categoria2 + "\t" + juego.categoria3 + "\t" + juego.foto + "\t" + juego.banner + "\t" +juego.descripcion)
    
    def devolver_Juego(self,id):
        for juego in self.listaJuegos:
            if juego.id==id:
                return juego.dump()
        return False

    #construlle un arreglo con los id's de una categoria buscada
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

    #devuelve los juegos en formato json
    def devolver_Juegos(self):
        return json.dumps([juego.dump() for juego in self.listaJuegos])

    #devuelve los comentarios de un juego en formato json
    def devolver_ComentariosJuego(self,id):
        for juego in self.listaJuegos:
            if juego.id == id:
                return juego.devolver_comentarios()
        return False

#pruebaJuegoCRUD = CRUD_VidoJuego()
#pruebaJuegoCRUD.cargaMasiva("C:\\Users\\Jonathan Calo\\Desktop\\datosJuegos.csv")
#pruebaJuegoCRUD.devolver_Juego(1)
#pruebaJuegoCRUD.listar_Juegos()