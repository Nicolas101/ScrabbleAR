import PySimpleGUI as sg 
import random
from Juego.Clases.Casilla import Casilla


# {---------------------------------------------------------------------------------}
# {--------------------------- CLASE FILA DE FICHAS --------------------------------}
# {---------------------------------------------------------------------------------}

class FilaFichas():
    """Esta clase se utiliza para crear el "atril" de fichas para el jugador y para la computadora.\n
    Parámetros:\n
    key_add: es un string adicional que se le agrega a la key de cada ficha, con el fin de diferenciar distintas filas de fichas.\n
    letras: es una lista que contiene las letras que posee la fila de fichas.\n
    """
    def __init__(self, letras, fichas_cpu):
        self._letras = letras
        self._fichas_cpu = fichas_cpu 
        self._casillas = [] # lista de objetos casilla de la fila
        self._ficha_selected = [False,None] # [True/False,key de la ficha seleccionada]   
        self._fichas_a_cambiar = [] # lista de keys de las fichas a cambiar
        #self._layout = self._armar() # layout para PySimpleGUI
        self._habilitada = True
        
    def getLayout(self):
        """Retorna el layout para la GUI
        """
        return self._armar()

    def _armar(self):
        """Arma una lista para PySimpleGUI que contiene tantas casillas como letras tenga la fila de fichas
        """
        lis_fichas = []
        if self._fichas_cpu :
            #Arma las fichas de la maquina:
            for i in range(1,len(self._letras)+1):
                casilla = Casilla(r"Data\Images\Juego\Fichas\Ficha-simple.png",deshabilitada=True,background="#6AB2E5")
                self._casillas.append(casilla)
                lis_fichas.append(casilla.getLayout())
        else:
            #Arma las fichas del jugador:
            for i in range(1,len(self._letras)+1):
                key = 'FICHA-'+ str(i)
                casilla = Casilla(r"Data\Images\Juego\Fichas\letra-"+self._letras[i-1].upper()+".png",key,ocupada=True,ficha=self._letras[i-1],background="#6AB2E5")
                self._casillas.append(casilla)
                lis_fichas.append(casilla.getLayout())
        
        return [lis_fichas]

    def getLayoutActualizado(self):
        lis_fichas = []
        for casilla in self._casillas:
            lis_fichas.append(casilla.getLayout())
        return [lis_fichas]

    def click(self, event):
        """Retorna True si el evento fue en una de las casillas de la fila de fichas, False en caso contrario
        """
        for casilla in self._casillas:
            if event == casilla.getKey() and not casilla.estaDeshabilitada():
                return True
        return False

    def estaHabilitada(self):
        return self._habilitada

    def habilitar(self):
        self._habilitada = True
    
    def deshabilitar(self):
        self._habilitada = False

    def marcarFichaSelected(self,window,key):
        """Setea la imagen de la ficha para indicar que esta seleccionada
        """
        self._ficha_selected[0] = True
        self._ficha_selected[1] = key 
        aux = key.split("-") #Se desarma la key para conseguir la posicion en la lista
        self._casillas[int(aux[1])-1].setImagen(r"Data\Images\Juego\Fichas\letra-seleccionada-"+self._casillas[int(aux[1])-1].getFicha().upper()+".png")  
        window[key].update(image_filename=self._casillas[int(aux[1])-1].getImagen())

    def desmarcarFichaSelected(self,window):
        """Setea la imagen de la ficha para indicar que no esta selecccionada
        """
        self._ficha_selected[0] = False
        aux = self._ficha_selected[1].split("-") #Se desarma la key para conseguir la posicion en la lista
        self._casillas[int(aux[1])-1].setImagen(r"Data\Images\Juego\Fichas\letra-"+self._casillas[int(aux[1])-1].getFicha().upper()+".png")
        window[self._ficha_selected[1]].update(image_filename=self._casillas[int(aux[1])-1].getImagen())

    def hayFichaSelected(self):
        """Retorna True si hay una ficha seleccionada, False en caso contrario
        """
        return self._ficha_selected[0]

    def getFichaSelected(self):
        """Retorna la ficha seleccionada actualmente
        """
        return self._ficha_selected[1]

    def sacarFicha(self,window):
        """Setea los parámetros de la casilla especificada para indicar que no hay una ficha(letra)
        """
        self._ficha_selected[0] = False
        aux = self._ficha_selected[1].split("-") #Se desarma la key para conseguir la posicion en la lista
        self._casillas[int(aux[1])-1].desocupar()
        self._casillas[int(aux[1])-1].setImagen(r"Data\Images\Juego\Fichas\Ficha-simple.png")
        self._casillas[int(aux[1])-1].deshabilitar()
        self._letras.remove(self._casillas[int(aux[1])-1].getFicha())#sin esta linea no se borran las letras ya usadas 
        window[self._ficha_selected[1]].update(image_filename=self._casillas[int(aux[1])-1].getImagen())

        return self._casillas[int(aux[1])-1].getFicha()

    def insertarFichas(self,window,fichas):
        """Agrega las fichas pasadas por parámetro en los lugares desocupados./n
        Se utiliza cuando el jugador pide cambiar las fichas, o cuando se hace un cambio de turno
        """
        for casilla in self._casillas:
            if not casilla.estaOcupada():
                letra = fichas.pop()
                casilla.setImagen(r"Data\Images\Juego\Fichas\letra-"+letra.upper()+".png")
                casilla.setFicha(letra)
                casilla.ocupar()
                casilla.habilitar()
                self._letras.append(letra)
                window[casilla.getKey()].Update(image_filename=casilla.getImagen())
    
    def getLetras(self):
        """Retorna una lista con las letras que posee la fila actualmente
        """
        return self._letras[:]

    def agregarFichaACambiar (self, key, window):
        """Agrega la ficha seleccionada a las fichas para cambiar.\n
        Si esta ya esta agregada, la quita
        """
        if (key not in self._fichas_a_cambiar): #Si la key no esta agregada:
            self._fichas_a_cambiar.append(key)
            aux = key.split("-") #Se desarma la key para conseguir la posicion en la lista
            self._casillas[int(aux[1])-1].setImagen(r"Data\Images\Juego\Fichas\letra-seleccionada-"+self._casillas[int(aux[1])-1].getFicha().upper()+".png")  
            window[key].update(image_filename=self._casillas[int(aux[1])-1].getImagen())

        else: #Si la key estaba agregada:
            self._fichas_a_cambiar.remove(key)
            aux = key.split("-") #Se desarma la key para conseguir la posicion en la lista
            self._casillas[int(aux[1])-1].setImagen(r"Data\Images\Juego\Fichas\letra-"+self._casillas[int(aux[1])-1].getFicha().upper()+".png") 
            window[key].update(image_filename=self._casillas[int(aux[1])-1].getImagen())
    
    def cambiarFichas(self, window, bolsa_fichas):
        """Cambia las fichas seleccionadas por otras, elegidas por la bolsa de fichas.\n
        Retorna True si se realizo correctamente, False en caso contrario
        """
        if (self._fichas_a_cambiar != []): #Si hay fichas seleccionadas para cambiar
            letras_viejas = []
            
            #Guardo las letras viejas y desocupo las casillas a cambiar
            for key in self._fichas_a_cambiar:  
                aux = key.split("-") #Se desarma la key para conseguir la posicion en la lista
                letras_viejas.append(self._casillas[int(aux[1])-1].getFicha())
                self._casillas[int(aux[1])-1].desocupar()  
            cant_letras_a_cambiar = len(self._fichas_a_cambiar)

            #traigo nuevas letras de la bolsa de fichas (si no hay mas letras devuelve lista vacia)
            lis_nuevas_letras = bolsa_fichas.letras_random(cant_letras_a_cambiar) 

            if (lis_nuevas_letras == []): #Si no hay nuevas letras:
                return False

            else: #Si hay letras nuevas:
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
        if self._fichas_a_cambiar != []: #
            for key in self._fichas_a_cambiar:
                aux = key.split("-") #Se desarma la key para conseguir la posicion en la lista
                self._casillas[int(aux[1])-1].setImagen(r"Data\Images\Juego\Fichas\letra-"+self._casillas[int(aux[1])-1].getFicha().upper()+".png") 
                window[key].update(image_filename=self._casillas[int(aux[1])-1].getImagen())
            self._fichas_a_cambiar = []


# {---------------------------------------------------------------------------------}
# {--------------------------- CREACIÓN DEL OBJETO ---------------------------------}
# {---------------------------------------------------------------------------------}

def crear_fila_fichas(bolsa_fichas, genero):
    fila_fichas = FilaFichas(bolsa_fichas.letras_random(7),genero)
    return fila_fichas