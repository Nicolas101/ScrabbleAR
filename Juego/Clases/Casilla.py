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
        # layout para PySimpleGUI:
        self._layout = sg.Button("",image_filename=self._imagen,key=self._key,pad=(0,0),button_color=(background,background),border_width=0) 

    def getKey(self):
        return self._key     

    def getLayout(self):
        return self._layout

    def getFicha(self):
        return self._ficha

    def setFicha(self,ficha):
        self._ficha = ficha

    def getImagen(self):
        return self._imagen

    def setImagen(self,imagen):
        self._imagen = imagen

    def ocupar(self):
        self._ocupada = True

    def desocupar(self):
        self._ocupada = False

    def estaOcupada(self):
        return self._ocupada    

    def habilitar(self):
        self._deshabilitada = False

    def deshabilitar(self):
        self._deshabilitada = True

    def estaDeshabilitada(self): 
        return self._deshabilitada

    def esEspecial(self):
        return self._especial[0]

    def getEspecial(self):
        return self._especial[1]

