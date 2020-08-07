class Jugador():
    """Esta clase permite definir un Jugador con:\n
    -Puntaje\n
    -Cantidad de cambios de fichas permitido\n
    -Contar de turnos pasados
    """

    def __init__(self):
        self._puntaje = 0 #Puntos del jugador
        self._cambios_fichas = 3 #cantidad de cambio de fichas máximo para el jugador
        self._turnos_pasados = 0 #Cantidad de turnos pasados
        self._palabras = []
    
    def getPuntaje(self):
        """Retorna el puntaje del jugador
        """
        return self._puntaje

    def getCambiosFichas(self):
        """Retorna la cantidad de cambios de fichas que posee actualmente el jugador
        """
        return self._cambios_fichas

    def getTurnosPasados(self):
        """Retorna la cantidad de turnos que paso el jugador hasta el momento
        """
        return self._turnos_pasados

    def getPalabras(self):
        return self._palabras

    def setPuntaje(self,puntos):
        """Setea el puntaje del jugador con el valor pasador por parámetro
        """
        self._puntaje = puntos

    def restarCambio(self):
        """Resta un cambio de fichas al jugador
        """
        self._cambios_fichas -= 1

    def pasarTurno(self):
        """Aumenta en 1 la cantidad de turnos pasados del jugador.
        """
        self._turnos_pasados += 1

    def verificarTurnosPasados(self):
        """Si llega a 3 turnos pasados, se le agrega un cambio de fichas al jugador
        """
        if self._turnos_pasados == 3:
            self._cambios_fichas += 1
            self._turnos_pasados = 0

    def ingresarPalabra(self,palabra,puntaje):
        """Suma al puntaje del jugador el puntaje pasado por parámetro y 
        agrega la palabra pasada por parámetro a la lista de palabras ingresadas por el jugador
        """
        self._puntaje += puntaje
        self._palabras.append(palabra+" - "+str(puntaje))

            
        