class Comentario:
    def __init__ (self,cadena,idUser,fecha):
        self.cadena = cadena
        self.idUser = idUser
        self.fecha = fecha
    
    def dump(self):

        return{
            'cadena': self.cadena,
            'nameUser': self.idUser,
            'fecha': self.fecha            
        }