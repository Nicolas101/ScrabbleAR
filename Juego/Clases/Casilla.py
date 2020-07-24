import PySimpleGUI as sg 
import random

# {---------------------------------------------------------------------------------}
# {------------------------------ CLASE CASILLA ------------------------------------}
# {---------------------------------------------------------------------------------}

class Casilla():
    """Esta clase se utiliza para crear todos los botones de la matriz del tablero y de la fila de fichas\n
    Parámetros:\n
    tamaño: tamaño del boton\n
    clave: key para acceder al elemento\n
    contenido: contenido de la ficha\n
    color: color de la casilla\n
    deshabilitada: indica si se puede clickear o no en la casilla\n
    ocupada: indica si hay una ficha en la casilla\n
    especial: indica si la casilla es "especial" --> tupla(True/False, contenido, color) 
    """
    def __init__(self, tamaño, clave, contenido='', color=('black','#FFFFFF'), deshabilitada=False, ocupada=False, especial=(False,None,None)):
        self._tamaño = tamaño
        self._key = clave
        if not especial[0]:
            self._contenido = contenido
            self._color = color
        else:
            self._contenido = especial[1]
            self._color = especial[2]
        self._deshabilitada = deshabilitada
        self._ocupada = ocupada
        self._especial = especial 
        # layout para PySimpleGUI:
        self._layout = sg.Button(self._contenido,key=self._key, pad=(0,0), size=self._tamaño, button_color=self._color, disabled_button_color=self._color, disabled=self._deshabilitada) 

    def getKey(self):
        return self._key

    def getContenido(self):
        return self._contenido  

    def setContenido(self,dato):
        self._contenido = dato     

    def getColor(self):
        return self._color

    def setColor(self,color):
        self._color = color

    def getLayout(self):
        return self._layout

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