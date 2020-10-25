class Usuario:
    #int id, String nombre,apellido,userName,contrasena, boolean admin
    def __init__(self,id,nombre,apellido,userName,contrasena,admin):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.userName = userName
        self.contrasena = contrasena
        self.admin = admin

    #recibe un usuario y contraseña y valida si es correcto
    def autenticar(self,userName,contrasena):
        if self.userName == userName and self.contrasena == contrasena:
            #retorna verdadero si el nombre de usuario y contraseña es correcto
            return True
        #retorna falso si el nombre o contraseña no coinciden
        return False
    
    #modifica los datos del usuario, excepto boolean admin
    def modificarDatos(self,id,nombre,apellido,userName,contrasena,admin):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.userName = userName
        self.contrasena = contrasena

    #muestra el usuario en formato json
    def dump(self):

        return{
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'userName': self.userName,
            'administrador': self.admin
        }

    #muestra los datos del usuario en consola
    def mostrar(self):

        print("id: " + str(self.id))
        print("nombre: " + self.nombre)
        print("apellido: " + self.apellido)
        print("userName: " + self.userName)
        print("contreaseña: " + self.contrasena)
        print("admin; " + str(self.admin))

#usuario1 = Usuario(0,"nombre1","apellido1","admin","admin",True)
#print("usuario1 creado")
#usuario2 = Usuario(1,"prueba","prueba1","prueba1_1","usario1",False)
#usuario1.mostrar()
#usuario2.mostrar()