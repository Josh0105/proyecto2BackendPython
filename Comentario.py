#SE DEFINE LA CLASE COMENTARIO
class Comentario:
    #Constructor de comentario
    def __init__ (self,cadena,UserName,fecha):
        self.cadena = cadena
        self.UserName = UserName
        self.fecha = fecha
    
    #Devuelve el comentario en formato Json
    def dump(self):
        return{
            'cadena': self.cadena,
            'nameUser': self.UserName,
            'fecha': self.fecha            
        }