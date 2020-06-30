import PySimpleGUI as sg 
import random

# {---------------------------------------------------------------------------------}
# {------------------------------ CLASE CASILLA ------------------------------------}
# {---------------------------------------------------------------------------------}

class Casilla():
    """ Esta clase se utiliza para crear todos los botones de la matriz del 
    tablero y de la fila de fichas\n
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

# {---------------------------------------------------------------------------------}
# {------------------------------ CLASE TABLERO ------------------------------------}
# {---------------------------------------------------------------------------------}

class Tablero:
    """ Esta clase crea un objeto Tablero que es una matriz de objetos "Casilla".\n
    Parámetros:\n
    tamaño: es la dimensión de la matriz (TxT).\n
    casillas_especiales: es un diccionario que contiene las keys de las casillas que son "especiales".\n
    inicio: es una tupla que contiene la key de la casilla de inicio del juego y una letra para esa casilla (key,letra).\n
    """
    def __init__(self, tamaño, casilas_especiales=None, inicio=(None,None)):
        self._tamaño = tamaño  
        self._casillas_especiales = casilas_especiales 
        self._inicio = inicio 
        self._casillas = [] # matriz que contiene todos los objetos "casilla" del tablero
        self._palabra = [inicio[0]] # letras de la palabra a formar
        self._layout = self._armar() # layout para PySimpleGUI
    
    def getLayout(self):
        return self._layout

    def _armar(self):
        """Este método arma una lista para la interfaz gráfica que contiene una matriz de objetos "Casilla"\n
        y guarda los objetos casilla en la propiedad _casillas.
        """
        layout = [] 
        for i in range(1, self._tamaño + 1):
            fila_layout = []
            fila_casillas = []
            for j in range(1, self._tamaño + 1):
                especial = False
                key = str(i)+"-"+str(j)
                #Para crear una casilla "especial":
                for clave in self._casillas_especiales:
                    if(key in self._casillas_especiales[clave][0]):
                        casilla = Casilla((3,1), key, deshabilitada=True, ocupada=False, especial=(True,clave,('black',self._casillas_especiales[clave][1])))
                        especial = True
                #Para crear una casilla normal o la casilla de inicio:        
                if not especial:
                    if key == self._inicio[0]:
                        casilla = Casilla((3,1), clave=self._inicio[0], contenido=self._inicio[1], color=('white','#684225'), deshabilitada=True, ocupada=True) #casilla de inicio
                    else:
                        casilla = Casilla((3,1), key, deshabilitada=True, ocupada=False) #casilla normal
                fila_casillas.append(casilla)
                fila_layout.append(casilla.getLayout())
            self._casillas.append(fila_casillas)     
            layout.append(fila_layout)

        return layout

    def click(self, event):
        """Este método retorna True si el evento fue en una de las casillas del tablero, False en caso contrario
        """
        for fila in self._casillas:
            for casilla in fila:
                if event == casilla.getKey():
                    return True
        return False        

    def habilitar(self, pantalla):
        """Este método habilita todas las casillas del tablero que esten desocupadas.
        """
        for fila in self._casillas:
            for casilla in fila:
                if casilla.estaOcupada():
                    continue
                else:
                    casilla.habilitar()
                    pantalla[casilla.getKey()].update(disabled=False)

    def deshabilitar(self, pantalla):
        """Este método deshabilita todas las casillas del tablero que esten desocupadas.
        """
        for fila in self._casillas:
            for casilla in fila:
                if casilla.estaOcupada():
                    continue
                else:
                    casilla.deshabilitar()
                    pantalla[casilla.getKey()].update(disabled=True)
    
    def insertarFicha(self,key,pantalla,valor):
        """Este método coloca una ficha en el tablero
        """
        self._palabra.append(key)
        aux = key.split("-")
        self._casillas[int(aux[0])-1][int(aux[1])-1].ocupar()
        self._casillas[int(aux[0])-1][int(aux[1])-1].deshabilitar()
        self._casillas[int(aux[0])-1][int(aux[1])-1].setContenido(valor)
        self._casillas[int(aux[0])-1][int(aux[1])-1].setColor(('white','#684225'))
        pantalla[key].update(valor, button_color=('white','#684225'), disabled_button_color=('white','#684225'), disabled=True)

    def reiniciarPalabra(self):
        self._palabra=[]

    def _reiniciarPalabraInicio(self):
        if (self._inicio[0] in self._palabra):
            self._palabra=[self._inicio[0]]
        else:
            self._palabra=[]

    def devolverFichas(self,pantalla_juego):
        lis_letras = []
        for key in self._palabra:
            if (key!=self._inicio[0]):
                aux = key.split('-')
                self._casillas[int(aux[0])-1][int(aux[1])-1].desocupar()
                lis_letras.append(pantalla_juego[key].GetText())
                especial = False
                for clave in self._casillas_especiales:
                    if key in self._casillas_especiales[clave][0]:
                        pantalla_juego[key].Update(clave, button_color=('black',self._casillas_especiales[clave][1]),disabled_button_color=('black',self._casillas_especiales[clave][1]))
                        especial = True
                if not especial:
                    pantalla_juego[key].Update('', button_color=('black','white'),disabled_button_color=('black','white'))
        self._reiniciarPalabraInicio()
        return lis_letras

    def getPalabra(self):
        lis_aux=[]
        for x in self._palabra:
            elems=x.split('-')
            for i in range(0,2):
                elems[i]=int(elems[i])
            lis_aux.append(elems)
        a_comparar=lis_aux[0][0]
        horizontal=True
        vertical=True
        for e in lis_aux:
            if(e[0]!=a_comparar):
                horizontal=False
        if (horizontal==False):
            a_comparar=lis_aux[0][1]
            
            for e in lis_aux:
                if(e[1]!=a_comparar):
                    vertical=False
            if (vertical==True):
                lis_ord=sorted(lis_aux, key=lambda valor: valor[0])
        else:
            lis_ord=sorted(lis_aux, key=lambda valor: valor[1])
        if (horizontal==True)or(vertical==True):
            pal=''
            for key in lis_ord:
                pal+= self._casillas[key[0]-1][key[1]-1].getContenido()
            return pal
        else:
            return 'xxxxxx'

# {---------------------------------------------------------------------------------}
# {--------------------------- CLASE FILA DE FICHAS --------------------------------}
# {---------------------------------------------------------------------------------}

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
                
# {---------------------------------------------------------------------------------}
# {--------------------------- CLASE BOLSA DE FICHAS -------------------------------}
# {---------------------------------------------------------------------------------}

class BolsaFichas():
    def __init__(self, bolsa_fichas):
        self._bolsa_fichas = bolsa_fichas
        self._habilitada = False

    def letras_random(self, cantidad):
        letras = list(self._bolsa_fichas.keys())
        string_letras = ''
        for i in letras:
            string_letras = string_letras + (i*self._bolsa_fichas[i]['cantidad'])
        lista_letras = []
        for x in range(0,cantidad):
            letra_elegida = random.choice(string_letras)
            lista_letras.append(letra_elegida)
            self._bolsa_fichas[letra_elegida]['cantidad'] = self._bolsa_fichas[letra_elegida]['cantidad'] - 1
        return lista_letras

    def habilitar(self):
        self._habilitada = True

    def deshabilitar(self):
        self._habilitada = False

    def estaHabilitada(self):
        return self._habilitada

    def devolverPuntaje(self,palabra):
        puntos = 0
        for letra in palabra:
            puntos += self._bolsa_fichas[letra]['puntuacion']
        return puntos
    
    
        
