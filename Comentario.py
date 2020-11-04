class Comentario:
    def __init__ (self,cadena,UserName,fecha):
        self.cadena = cadena
        self.UserName = UserName
        self.fecha = fecha
    
    def dump(self):

        return{
            'cadena': self.cadena,
            'nameUser': self.UserName,
            'fecha': self.fecha            
        }