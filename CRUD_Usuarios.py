from Usuario import Usuario
import json

class CRUD_Usuarios:
    #constructor del CRUD usuarios
    def __init__(self):
        self.misUsuarios = []
        self.contador = 0
        #Aqui se créa el usuario mestro
        self.misUsuarios.append(Usuario(0,"Usuario","Maestro","admin","admin",True))

    #método para creación de usuarios propios
    def crear_Usuario(self,nombre,apellido,userName,contrasena,contrasena2):
        #Si el primer caracter de userName no es mayúscula
        if userName[0].isupper() == False:
            print("UserName no empieza con Mayúscula")
            return False
        #Si la cadena userName no es alfanumerica
        elif userName.isalnum() == False:
            print("UserName no contiene solo números o letras")
            return False
        #Este for revisa si el userName ya existe
        for user in self.misUsuarios:
            if user.userName == userName:
                print("Este UserName ya existe")
                return False
        #Este if evalua si las contraseñas coinciden
        if contrasena != contrasena2:
            print("Las contraseñas no coinciden")
            return False
        #Si todo está correcto aumentamos el contador y creamos el usuario
        self.contador += 1
        self.misUsuarios.append(Usuario(self.contador,nombre,apellido,userName,contrasena,False))
        print("se creó un usuario con exito")
        return True

    def crear_Usuario_Admin(self,nombre,apellido,userName,contrasena,contrasena2):
        #Si el primer caracter de userName no es mayúscula
        if userName[0].isupper() == False:
            print("UserName no empieza con Mayúscula")
            return False
        #Si la cadena userName no es alfanumerica
        elif userName.isalnum() == False:
            print("UserName no contiene solo números o letras")
            return False
        #Este for revisa si el userName ya existe
        for user in self.misUsuarios:
            if user.userName == userName:
                print("Este UserName ya existe")
                return False
        #Este if evalua si las contraseñas coinciden
        if contrasena != contrasena2:
            print("Las contraseñas no coinciden")
            return False
        #Si todo está correcto aumentamos el contador y creamos el usuario
        self.contador += 1
        self.misUsuarios.append(Usuario(self.contador,nombre,apellido,userName,contrasena,True))
        print("se creó un usuario administrador con exito")
        return True

    #lista los usuarios en consola
    def listar_Usuarios(self):
        for user in self.misUsuarios:
            print("id:\t"+ str(user.id) + "\tnombre:\t" + user.nombre + "\t\tuser:\t" + user.userName+ "\t\tadmin:\t" + str(user.admin))
    
    #devuelve los usuarios en formato json
    def devolver_Usuarios(self):
        return json.dumps([user.dump() for user in self.misUsuarios])

    #devuelve el usuario si el user y la contraseña son correctos
    def autenticar_Usuario(self,userName,contrasena):
        for user in self.misUsuarios:
            if user.autenticar(userName,contrasena) == True:
                print("usuario y contraseña correcta")
                return user
        return False

    #devuelve la contraseña del usuario si existe
    def recuperar_Contrasena(self,userName):
        for user in self.misUsuarios:
            if user.userName == userName:
                print("la contraseña es: " + user.contrasena)
                return user
        return False
    
    #Recibe un id y cambia los atributos de ese usuario
    def modificar_Usuario(self,id,nombre,apellido,userName,contrasena,contrasena2):
        #Si el primer caracter de userName no es mayúscula
        if userName[0].isupper() == False:
            print("UserName no empieza con Mayúscula")
            return False
        #Si la cadena userName no es alfanumerica
        elif userName.isalnum() == False:
            print("UserName no contiene solo números o letras")
            return False
        #Este for revisa si el userName ya existe en otros id diferentes de este
        for user in self.misUsuarios:
            if user.id != id:
                if user.userName == userName:
                    print("El nuevo UserName ya existe en otro usuario")
                    return False
        #Este if evalua si las contraseñas coinciden
        if contrasena != contrasena2:
            print("Las contraseñas no coinciden")
            return False
        #Si todo está correcto modificamos el usuario
        if self.misUsuarios[id].admin == True:
            self.misUsuarios[id] = Usuario(id,nombre,apellido,userName,contrasena,True)
        else:
            self.misUsuarios[id] = Usuario(id,nombre,apellido,userName,contrasena,False)
            print("se modificó un usuario con exito")
            return True


#var_Usuarios = CRUD_Usuarios()
#var_Usuarios.crear_Usuario("nombre1","apellido1","Prueba1","contra1","contra1")
#var_Usuarios.crear_Usuario("nombre2","apellido2","Prueba2","contra2","contra2")
#var_Usuarios.crear_Usuario("nombre3","apellido3","Prueba3","contra3","contra3")
#var_Usuarios.listar_Usuarios()
#var_Usuarios.devolver_Usuarios()
#var_Usuarios.autenticar_Usuario("Admin","admin")
#var_Usuarios.recuperar_Contrasena("Admin")
#var_Usuarios.recuperar_Contrasena("Prueba2")
#var_Usuarios.modificar_Usuario(2,"nombre10","apellido10","Prueba2","contra10","contra10")
#var_Usuarios.modificar_Usuario(0,"SSSS","SSSS","Adm","contra10","contra10")
#var_Usuarios.crear_Usuario_Admin("Admin2","Admin2","Admin2","contra50","contra50")
#var_Usuarios.listar_Usuarios()
#var_Usuarios.recuperar_Contrasena("Prueba2")