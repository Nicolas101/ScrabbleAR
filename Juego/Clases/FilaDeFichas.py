import PySimpleGUI as sg 
import random
try:
    from Juego.Clases.Casilla import Casilla
except ModuleNotFoundError:
    from Clases.Casilla import Casilla

# {---------------------------------------------------------------------------------}
# {--------------------------- CLASE FILA DE FICHAS --------------------------------}
# {---------------------------------------------------------------------------------}

class FilaFichas():
    """Esta clase se utiliza para crear el "atril" de fichas para el jugador y para la computadora.\n
    Parámetros:\n
    key_add: es un string adicional que se le agrega a la key de cada ficha, con el fin de diferenciar distintas filas de fichas.\n
    letras: es una lista que contiene las letras iniciales a colocar en las fichas.\n
    """
    def __init__(self, key_add, letras):
        self._key_add = key_add
        self._letras = letras
        self._ficha_selected = [False,None] # [True/False,key de la ficha seleccionada]
        self._casillas = [] # lista de objetos casilla de la fila
        self._layout = self._armar() # layout para PySimpleGUI
        self._fichas_a_cambiar = [] # lista de keys de las fichas a cambiar
        
    def getLayout(self):
        """Retorna el layout para la GUI
        """
        return self._layout

    def _armar(self):
        """Arma una lista para la GUI que contiene tantos objetos "Casilla" como letras iniciales antes pasadas
        """
        layout = []
        for i in range(1,len(self._letras)+1):
            key = self._key_add +'-'+ str(i)
            if (self._key_add == 'FJ'):
                casilla = Casilla((11,2), key, contenido=self._letras[i-1], ocupada=True) # fichas del jugador
            else:
                casilla = Casilla((11,2), key, deshabilitada=True) # fichas de la maquina
            self._casillas.append(casilla)
            layout.append(casilla.getLayout())     
        return [layout]

    def click(self, event):
        """Retorna True si el evento fue en una de las casillas de la fila de fichas, False en caso contrario
        """
        for casilla in self._casillas:
            if event == casilla.getKey():
                return True
        return False

    def marcarFichaSelected(self,window,key):
        """Setea los parámetros necesarios de la casilla clickeada para marcarla como "seleccionada"
        """
        self._ficha_selected[0] = True
        self._ficha_selected[1] = key 
        aux = key.split("-")
        self._casillas[int(aux[1])-1].setColor(('black',"#5fefaa"))   
        window[key].update(button_color=('black',"#5fefaa"))

    def desmarcarFichaSelected(self,window):
        """Setea los parámetros necesarios para marcar la casilla seleccionada como normal
        """
        self._ficha_selected[0] = False
        aux = self._ficha_selected[1].split("-")
        self._casillas[int(aux[1])-1].setColor(('black','white'))
        window[self._ficha_selected[1]].update(button_color=('black','white'))

    def hayFichaSelected(self):
        """Retorna True si hay una ficha seleccionada, False en caso contrario
        """
        return self._ficha_selected[0]

    def getFichaSelected(self):
        """Retorna la ficha seleccionada actualmente
        """
        return self._ficha_selected[1]

    def sacarFicha(self,window):
        """Setea los parámetros de la casilla especificada para marcar que no hay una ficha(letra)
        """
        self._ficha_selected[0] = False
        aux = self._ficha_selected[1].split("-")
        self._casillas[int(aux[1])-1].desocupar()
        self._casillas[int(aux[1])-1].setContenido("")
        self._casillas[int(aux[1])-1].setColor(('black',"#CCCCCC"))
        self._casillas[int(aux[1])-1].deshabilitar()
        window[self._ficha_selected[1]].update("",button_color=('black',"#CCCCCC"),disabled=True)

    def insertarFichas(self,window,fichas):
        """Agrega las fichas pasadas por parámetro a la fila./n
        Se utiliza cuando el jugador pide cambiar las fichas, o cuando se hace un cambio de turno
        """
        for casilla in self._casillas:
            if casilla.getContenido()=='':
                ficha=fichas.pop()
                casilla.setContenido(ficha)
                self._letras.append(ficha)
                window[casilla.getKey()].Update(ficha, disabled=False, button_color=('black','white'))
    
    def getLetras(self):
        """Retorna una lista con las letras que posee la fila actualmente
        """
        return self._letras[:]

    def agregarFichaACambiar (self, key, window):
        """Cuando esta seleccionado el boton cambiar fichas,
        si se toca una ficha la agrega a fichas a cambiar y si ya esta agregada la quita
        """
        if (key not in self._fichas_a_cambiar):
            self._fichas_a_cambiar.append(key)
            aux = key.split("-")
            self._casillas[int(aux[1])-1].setColor(('black',"#5fefaa"))   
            window[key].update(button_color=('black',"#5fefaa"))
        else:
            self._fichas_a_cambiar.remove(key)
            aux = key.split("-")
            self._casillas[int(aux[1])-1].setColor(('black',"white"))   
            window[key].update(button_color=('black',"white"))
    
    def cambiarFichas(self, window, bolsa_fichas):
        """Cambia las fichas seleccionadas por otras, elegidas por la bolsa de fichas.\n
        Retorna True si se realizo correctamente, False en caso contrario
        """
        if (self._fichas_a_cambiar != []): #si hay fichas seleccionadas para cambiar
            letras_viejas = []
            
            #pongo las casillas que voy a cambiar en blanco y guardo su contenido anterior
            for key in self._fichas_a_cambiar:  
                aux = key.split("-")
                letras_viejas.append(self._casillas[int(aux[1])-1].getContenido())
                self._casillas[int(aux[1])-1].setColor(('black',"#5fefaa"))
                self._casillas[int(aux[1])-1].setContenido('')  
                window[key].Update('')
            cant_letras_a_cambiar = len(self._fichas_a_cambiar)

            #traigo nuevas letras de la bolsa de fichas (si no hay mas letras devuelve lista vacia)
            lis_nuevas_letras = bolsa_fichas.letras_random(cant_letras_a_cambiar) 
            if (lis_nuevas_letras == []):
                return False
            else:
                bolsa_fichas.devolverLetras(letras_viejas) #devuelvo las letras viejas a la bolsa
                self.insertarFichas(window, lis_nuevas_letras) #inserto las nuevas en la fila de fichas
                self._fichas_a_cambiar = []
                return True
        else: 
            return True
    
    def eliminarLetras(self, palabra):
        """Elimina de la variable _letras las letras del string pasado por parametro
        """
        for letra in palabra:
            self._letras.remove(letra)
        
    def eliminarTodasLasLetras(self):
        """Deja la variable _letras vacia(se usa cuando la maquina tiene que cambiar letras)
        """
        self._letras = []

    def agregarLetra(self,letra):
        """Agrega una letra a la variable _letras
        """
        self._letras.append(letra)

    def cancelarCambioDeFichas(self, window):
        """Setea los parámetros necesarios para desmarcar las fichas seleccionadas a cambiar
        """
        if self._fichas_a_cambiar != []:
            for key in self._fichas_a_cambiar:
                aux = key.split("-")
                self._casillas[int(aux[1])-1].setColor(('black',"white"))   
                window[key].update(button_color=('black',"white"))
            self._fichas_a_cambiar = []


# {---------------------------------------------------------------------------------}
# {--------------------------- CREACIÓN DEL OBJETO ---------------------------------}
# {---------------------------------------------------------------------------------}

def crear_fila_fichas(bolsa_fichas, genero):
    fila_fichas = FilaFichas(key_add= genero, letras=bolsa_fichas.letras_random(7))
    return fila_fichas