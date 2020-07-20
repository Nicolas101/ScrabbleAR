class Jugador():

    def _init_(self):
        self._puntaje = 0
    
    def getPuntaje(self):
        return self._puntaje

    def setPuntaje(self,puntos):
        self._puntaje = puntos

    def sumarPuntos(self,puntos_nuevos):
        self._puntaje += puntos_nuevos
        
        