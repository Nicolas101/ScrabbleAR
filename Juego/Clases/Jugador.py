class Jugador():

    def __init__(self):
        self._puntaje = 0
        self._cambios_fichas = 3
        self._turnos_pasados = 0
    
    def getPuntaje(self):
        return self._puntaje

    def setPuntaje(self,puntos):
        self._puntaje = puntos

    def getCambiosFichas(self):
        return self._cambios_fichas

    def sumarPuntos(self,puntos_nuevos):
        """suma al puntaje del jugador la cantidad pasada por parametro
        """
        self._puntaje += puntos_nuevos

    def restarCambio(self, window_game):
        """resta un cambio del usuario, si se llega a 0 cambia el boton de cambiar
        por el de pasar turno
        """
        self._cambios_fichas -= 1
        if self._cambios_fichas == 0:
            window_game['Cambiar fichas'].Update('Pasar turno')

    def pasarTurno(self, window_game):
        """pasa el turno, si se llega a 3 pasadas de turno se suma un cambio de fichas
        """
        self._turnos_pasados += 1
        if self._turnos_pasados == 3:
            self._cambios_fichas += 1
            self._turnos_pasados = 0
            window_game['Cambiar fichas'].Update('Cambiar fichas')
        
        