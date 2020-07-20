import PySimpleGUI as sg 
import random
try:
    from Juego.Clases.Casilla import Casilla
except ModuleNotFoundError:
    from Clases.Casilla import Casilla

class FilaFichas():
    """ Esta clase se utiliza para crear el "atril" de fichas para el jugador y para la computadora.\n
    Parámetros:\n
    key_add: es un string adicional que se le agrega a la key de cada ficha, con el fin de diferenciar
    distintas filas de fichas.\n
    letras: es una lista que contiene las letras a colocar en las fichas.\n
    """
    def __init__(self, key_add, letras):
        self._key_add = key_add
        self._letras = letras
        self._ficha_selected = [False,None] # [True/False,key de la ficha seleccionada]
        self._casillas = [] # lista de objetos casilla de la fila
        self._layout = self._armar() # layout para PySimpleGUI
        
    def getLayout(self):
        return self._layout

    def _armar(self):
        """ Este método arma una lista para la interfaz gráfica que contiene 7 objetos "Casilla".
        """
        layout = []
        for i in range(1,8):
            key = self._key_add +'-'+ str(i)
            if (self._key_add == 'FJ'):
                casilla = Casilla((11,2), key, contenido=self._letras[i-1], ocupada=True) # fichas del jugador
            else:
                casilla = Casilla((11,2), key, deshabilitada=True) # fichas de la maquina
            self._casillas.append(casilla)
            layout.append(casilla.getLayout())     
        return [layout]

    def click(self, event):
        """Este método retorna True si el evento fue en una de las casillas de la fila de fichas, False en caso contrario
        """
        for casilla in self._casillas:
            if event == casilla.getKey():
                return True
        return False

    def marcarFichaSelected(self,pantalla,key):
        self._ficha_selected[0] = True
        self._ficha_selected[1] = key 
        aux = key.split("-")
        self._casillas[int(aux[1])-1].setColor(('black',"#5fefaa"))   
        pantalla[key].update(button_color=('black',"#5fefaa"))

    def desmarcarFichaSelected(self,pantalla):
        self._ficha_selected[0] = False
        aux = self._ficha_selected[1].split("-")
        self._casillas[int(aux[1])-1].setColor(('black','white'))
        pantalla[self._ficha_selected[1]].update(button_color=('black','white'))

    def hayFichaSelected(self):
        return self._ficha_selected[0]

    def getFichaSelected(self):
        return self._ficha_selected[1]

    def sacarFicha(self,pantalla):
        self._ficha_selected[0] = False
        aux = self._ficha_selected[1].split("-")
        self._casillas[int(aux[1])-1].desocupar()
        self._casillas[int(aux[1])-1].setContenido("")
        self._casillas[int(aux[1])-1].setColor(('black',"#CCCCCC"))
        self._casillas[int(aux[1])-1].deshabilitar()
        pantalla[self._ficha_selected[1]].update("",button_color=('black',"#CCCCCC"),disabled=True)

    def insertarFichas(self,pantalla_juego,fichas):
        for casilla in self._casillas:
            if casilla.getContenido()=='':
                ficha=fichas.pop()
                casilla.setContenido(ficha)
                pantalla_juego[casilla.getKey()].Update(ficha, disabled=False, button_color=('black','white'))
                
def crearFilaFichas(bolsa_fichas, genero):
    fila_fichas = FilaFichas(key_add= genero, letras=bolsa_fichas.letras_random(7))
    return fila_fichas