#DEFINIMOS LA CLASE USUARIO
class Usuario:
    #int id, String nombre,apellido,userName,contrasena, boolean admin
    def __init__(self,id,nombre,apellido,userName,contrasena,admin):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.userName = userName
        self.contrasena = contrasena
        self.admin = admin
        self.biblioteca = []

    #agrega un id a la lista de juegos a la biblioteca
    def agregarIDJuego(self,id):
        for idJuego in self.biblioteca:
            if idJuego == id:
                print("El juego ya está en tu biblioteca")
                return False
        self.biblioteca.append(id)
        print("Juego agregado exitosamente")
        return True

    #recibe un usuario y contraseña y valida si es correcto
    def autenticar(self,userName,contrasena):
        if self.userName == userName and self.contrasena == contrasena:
            #retorna verdadero si el nombre de usuario y contraseña es correcto
            return True
        #retorna falso si el nombre o contraseña no coinciden
        return False
    
    #modifica los datos del usuario
    def modificarDatos(self,id,nombre,apellido,userName,contrasena,admin):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.userName = userName
        self.contrasena = contrasena
        self.admin = admin

    #devuelve datos del usuario en formato json
    def dump(self):
        return{
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'userName': self.userName,
            'contrasena': self.contrasena,
            'administrador': self.admin
        }