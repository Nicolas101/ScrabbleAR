import PySimpleGUI as sg 
import random

# {---------------------------------------------------------------------------------}
# {------------------------------ CLASE CASILLA ------------------------------------}
# {---------------------------------------------------------------------------------}

class Casilla():
    """Esta clase se utiliza para crear todos los botones de la matriz del tablero y de la fila de fichas\n
    Parámetros:\n
    key: String para acceder al elemento\n
    tipo: String de la casilla/ficha\n
    deshabilitada: booleano que indica si se puede clickear o no en la casilla\n
    ocupada: booleano que indica si hay una ficha en la casilla\n
    especial: tupla que indica si la casilla es "especial"  
    """
    def __init__(self, imagen, key=None,deshabilitada=False, ocupada=False, especial=(False,None), ficha=None,background=None):
        self._imagen = imagen
        self._key = key
        self._deshabilitada = deshabilitada
        self._ocupada = ocupada
        self._ficha = ficha
        self._especial = especial
        self._background = background

    def getKey(self):
        """Devuelve la key de la casilla
        """
        return self._key     

    def getLayout(self):
        """Devuelve el layout de la casilla(para PySimpleGUI)
        """
        return sg.Button("",image_filename=self._imagen,key=self._key,pad=(0,0),button_color=(self._background,self._background),border_width=0)

    def getFicha(self):
        """Devuelve el contenido de la casilla
        """
        return self._ficha

    def setFicha(self,ficha):
        """la variable self._ficha pasa a valer el valor pasado por parámetro
        """
        self._ficha = ficha

    def getImagen(self):
        """Devuelve la imagen de la casilla
        """
        return self._imagen

    def setImagen(self,imagen):
        """La imagen de la casilla pasa a ser la pasada por parámetro
        """
        self._imagen = imagen

    def ocupar(self):
        """Pone la variable ocupada en True
        """
        self._ocupada = True

    def desocupar(self):
        """Pone la variable ocupada en False
        """
        self._ocupada = False

    def estaOcupada(self):
        """Devuelve True si la casilla esta ocupada, False si no
        """
        return self._ocupada    

    def habilitar(self):
        """Habilita la casilla
        """
        self._deshabilitada = False

    def deshabilitar(self):
        """Deshabilita la casilla
        """
        self._deshabilitada = True

    def estaDeshabilitada(self):
        """Devuelve True si la casilla esta deshabilitada, False si no
        """
        return self._deshabilitada

    def esEspecial(self):
        """Devuelve True si la casilla es especial, False si no
        """
        return self._especial[0]

    def getEspecial(self):
        """Devuelve el tipo de especial que es la casilla
        """
        return self._especial[1]

