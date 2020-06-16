import PySimpleGUI as sg 


class Casilla():
    def __init__(self, tamaño=(3,1), color='#FFFFFF', clave=None, estado='libre', especial=False):
        self._tamaño = tamaño
        self._color = color
        self._key = clave
        self._estado = estado
        self._especial = especial
        self._diseño = sg.Button('',key=self._key, pad=(0,0), size=self._tamaño, button_color=('black','#F02121'))

    def getKey(self):
        return self._key

    def getDiseño(self):
        return self._diseño



class Tablero:
    def __init__(self,filas=0,columnas=0):
        self._cant_filas = filas
        self._cant_columnas = columnas
        valores = self.armar()
        self._key_casillas = valores[0]
        self._diseño = valores[1]
    
    def getDiseño(self):
        return self._diseño

    def armar(self):

        layout = keys = [] 
        for i in range(0,self._cant_filas):

            fila_casillas = fila_keys = []
            for j in range(0,self._cant_columnas):

                casilla = Casilla(clave=str(i)+"-"+str(j))
                fila_casillas.append(casilla.getDiseño())  
                fila_keys.append(str(i)+"-"+str(j))

            layout.append(fila_casillas)
            keys.append(fila_keys)

        return (keys,layout)




def main():
    tablero = Tablero(5,5)
    layout = tablero.getDiseño()
    window = sg.Window("Prueba",layout)

    while True:
        event, values = window.read()
        if event is None:
            break
    window.close()


if __name__ == "__main__":
    main()