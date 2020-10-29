from Juego import Juego
import json
import csv

class CRUD_VidoJuego:
    #CONSTRUCTOR CRUD
    def __init__(self):
        self.listaJuegos = []
        self.contador = 0

    #Crea cada uno de los juegos
    def crearJuego(self,nombre,anio,precio,categoria1,categoria2,categoria3,foto,banner,descripcion):
        self.contador += 1
        self.listaJuegos.append(Juego(self.contador,nombre,anio,precio,categoria1,categoria2,categoria3,foto,banner,descripcion))
    
    #Modifica un juego
    def modificarJuego(self,id,nombre,anio,precio,categoria1,categoria2,categoria3,foto,banner,descripcion):
        for juego in self.listaJuegos:
            if juego.id == id:
                juego.modificar_Juego(nombre,anio,precio,categoria1,categoria2,categoria3,foto,banner,descripcion)
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
                return juego.dumps()
        return False

    #devuelve los juegos en formato json
    def devolver_Juegos(self):
        return json.dumps([juego.dump() for juego in self.listaJuegos])

#pruebaJuegoCRUD = CRUD_VidoJuego()
#pruebaJuegoCRUD.cargaMasiva("C:\\Users\\Jonathan Calo\\Desktop\\datosJuegos.csv")
#pruebaJuegoCRUD.devolver_Juego(1)
#pruebaJuegoCRUD.listar_Juegos()