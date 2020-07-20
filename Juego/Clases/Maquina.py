try:
    from Juego.Clases.Jugador import Jugador
except ModuleNotFoundError:
    from Clases.Jugador import Jugador

class Maquina(Jugador):

    def cambiarFichas(self,fichas,bolsa_fichas):
        #a implentar
        pass
    
    def armarPalabra(self,fichas,bolsa_fichas):
        #a implementar
        #intenta armar una palabra, si no puede llamaria a cambiarFichas
        #si arma la palabra llama a insertar palabra
        pass
