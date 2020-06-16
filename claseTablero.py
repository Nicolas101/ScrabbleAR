import PySimpleGUI as sg 
import random


class Casilla():
    def __init__(self, contenido='', tamaño=(3,1), color='#FFFFFF', clave=None, estado='libre'):
        self._contenido = contenido
        self._tamaño = tamaño
        self._color = color
        self._key = clave
        self._estado = estado
        self._diseño = sg.Button(self._contenido,key=self._key, pad=(0,0), size=self._tamaño, button_color=('black',self._color),disabled_button_color=('black',self._color))

    def getKey(self):
        return self._key

    def getDiseño(self):
        return self._diseño



class Tablero:
    def __init__(self,filas=0,columnas=0,casilas_especiales=None):
        self._cant_filas = filas
        self._cant_columnas = columnas
        self._casillas_especiales = casilas_especiales
        self._key_casillas = []
        self._diseño = self.armar()
        
    def getDiseño(self):
        return self._diseño

    def getKeys(self):
        return self._key_casillas

    def armar(self):
        layout = [] 
        for i in range(1, self._cant_filas + 1):
            fila_casillas = []
            for j in range(1, self._cant_columnas + 1):
                especial = False
                key = str(i)+"-"+str(j)
                for clave in self._casillas_especiales:
                    if(key in self._casillas_especiales[clave][0]):
                        casilla = Casilla(clave=key, contenido=clave, color=self._casillas_especiales[clave][1]) #casilla especial
                        especial = True
                if not especial:
                    casilla = Casilla(clave=key) #casilla normal
                fila_casillas.append(casilla.getDiseño()) 
                self._key_casillas.append(key) 
            layout.append(fila_casillas)
        return layout

    def habilitar(self, pantalla_juego):
        for i in range(1,self._cant_filas + 1):
            for j in range(1,self._cant_filas + 1):
                key = str(i)+"-"+str(j)
                pantalla_juego[key].Update(disabled=False)
    
    def deshabilitar(self, pantalla_juego):
        for i in range(1,self._cant_filas + 1):
            for j in range(1,self._cant_filas + 1):
                key = str(i)+"-"+str(j)
                pantalla_juego[key].Update(disabled=True)


# PRUEBA 
def main():
    num_random = random.randint(1,3)

    casillas_especiales1 = {
        "+2":(("2-6","2-10","6-2","6-14","7-7","7-9","9-7","9-9","10-2","10-14","14-6","14-10",), "#2283BB"),
        "+3":(("1-4","1-12","3-7","3-9","4-1","4-8","4-15","7-3","7-13","8-4","8-12","9-3","9-13","12-1","12-15","12-8","13-7","13-9","15-4"), "#45BB22"),
        "-3":(("1-1","1-8","1-15","8-1","8-15","15-1","15-8","15-15"), '#F02121'),
        "-2":(("2-2","2-14","3-3","3-13","13-3","13-13","14-2","14-14"), '#F06C21'),
        "-1":(("4-4","4-12","5-5","5-11","6-6","6-10","10-6","10-10","11-5","11-11","12-4","12-12"), '#F0B121')
    }
    casillas_especiales2 = {}
    casillas_especiales3 = {}

    if num_random == 1:
        tablero = Tablero(15,15,casillas_especiales1)
    elif num_random == 2:
        tablero = Tablero(20,20,casillas_especiales1)#2
    else:
        tablero = Tablero(25,25,casillas_especiales1)#3    
        


if __name__ == "__main__":
    main()