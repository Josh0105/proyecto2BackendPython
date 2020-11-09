from Usuario import Usuario
import json

#DEFINIMOS LA CLASE CRUD_USUARIOS
class CRUD_Usuarios:
    #constructor del CRUD usuarios
    def __init__(self):
        self.misUsuarios = []
        self.contador = 0
        #Aqui se créa el usuario mestro
        self.misUsuarios.append(Usuario(0,"Usuario","Maestro","admin","admin",True))

    #método para creación de usuarios cliente
    #retornos: 1: creado, 2:UserName no empieza con letra, 3: userName no es alfanumerica,
    # 4: userName ya existe, 5:contraseñas no coinciden, 6:existen espacios vacios
    def crear_Usuario(self,nombre,apellido,userName,contrasena,contrasena2,admin):
        #Si existe algún espacio vacío
        if nombre== "" or apellido== "" or userName == "" or contrasena =="" or contrasena2 == "":
            print("Existen espacion vacios")
            return 6
        #Si el primer caracter de userName no es letra
        if userName[0].isalpha() == False:
            print("UserName no empieza con una letra")
            return 2
        #Si la cadena userName no es alfanumerica
        elif userName.isalnum() == False:
            print("UserName no contiene solo números o letras")
            return 3
        #Este for revisa si el userName ya existe
        for user in self.misUsuarios:
            if user.userName == userName:
                print("Este UserName ya existe")
                return 4
        #Este if evalua si las contraseñas coinciden
        if contrasena != contrasena2:
            print("Las contraseñas no coinciden")
            return 5
        #Si todo está correcto aumentamos el contador y creamos el usuario
        self.contador += 1
        self.misUsuarios.append(Usuario(self.contador,nombre,apellido,userName,contrasena,admin))
        print("se creó un usuario con exito")
        return 1

    #recive un ID y devuelve el nombre del usuario
    def devolver_nombre_usuario(self,id):
        for user in self.misUsuarios:
            if user.id == id:
                return user.userName
        return ""

    #devuelve un usuario en formato json
    def devolver_datos_usuario(self,id):
        for user in self.misUsuarios:
            if user.id == id:
                return user.dump()
        return False

    #devuelve todos los usuarios en formato json
    def devolver_Usuarios(self):
        return json.dumps([user.dump() for user in self.misUsuarios])

    #devuelve el usuario si el user y la contraseña son correctos
    def autenticar_Usuario(self,userName,contrasena):
        for user in self.misUsuarios:
            if user.autenticar(userName,contrasena) == True:
                print("usuario y contraseña correcta")
                return user
        return False

    #devuelve la contraseña del usuario si existe el usuario
    def recuperar_Contrasena(self,userName):
        for user in self.misUsuarios:
            if user.userName == userName:
                print("la contraseña es: " + user.contrasena)
                return user
        return False
    
    #método para la modificación de un usuario
    #retornos: 1: creado, 2:UserName no empieza con letra, 3: userName no es alfanumerica,
    # 4: userName ya existe, 5:contraseñas no coinciden, 6: espacios vacios
    def modificar_Usuario(self,id,nombre,apellido,userName,contrasena,contrasena2):
        #Si existe algún espacio vacío
        if nombre== "" or apellido== "" or userName == "" or contrasena =="" or contrasena2 == "":
            print("Existen espacion vacios")
            return 6
        #Si el primer caracter de userName no es letra
        if userName[0].isalpha() == False:
            print("UserName no empieza con una letra")
            return 2
        #Si la cadena userName no es alfanumerica
        elif userName.isalnum() == False:
            print("UserName no contiene solo números o letras")
            return 3
        #Este for revisa si el userName ya existe en otros id diferentes de este
        for user in self.misUsuarios:
            if user.id != id:
                if user.userName == userName:
                    print("El nuevo UserName ya existe en otro usuario")
                    return 4
        #Este if evalua si las contraseñas coinciden
        if contrasena != contrasena2:
            print("Las contraseñas no coinciden")
            return 5
        #Si todo está correcto modificamos el usuario
        if self.misUsuarios[id].admin == True:
            self.misUsuarios[id].modificarDatos(id,nombre,apellido,userName,contrasena,True)
            print("se modificó un usuario administrador con exito")
            return 1
        else:
            self.misUsuarios[id].modificarDatos(id,nombre,apellido,userName,contrasena,False)
            print("se modificó un usuario normal con exito")
            return 1

    #Agrega un juego a la biblioteca del usuario retorna 1 si se agrega, 
    # #0 si ya se encontraba y 2 si no existe existe el usuario
    def agregarABiblioteca(self,idUsuario,idJuego):
        for user in self.misUsuarios:
            if user.id == idUsuario:
                if(user.agregarIDJuego(idJuego)==True):
                    return 1
                else:
                    return 0
        print("usuario no existe")
        return 2