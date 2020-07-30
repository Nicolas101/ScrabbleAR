import PySimpleGUI as sg 
import random
try:
    #Si se ejecuta el ScrabbleAR.py:
    from Juego.Clases.Casilla import Casilla
except ModuleNotFoundError:
    #Si se ejecuta el mainJuego.py:
    from Clases.Casilla import Casilla

# {---------------------------------------------------------------------------------}
# {------------------------------ CLASE TABLERO ------------------------------------}
# {---------------------------------------------------------------------------------}

class Tablero:
    """Esta clase crea un objeto Tablero que es una matriz de objetos "Casilla".\n
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
        self._palabra = [inicio[0]] # lista de keys de las fichas que estan formando la palabra
        self._layout = self._armar() # layout para PySimpleGUI
    
    def getLayout(self):
        """Retorna el layout para la GUI
        """
        return self._layout

    def getLetraInicio(self):
        """Retorna la letra de la ficha de inicio
        """
        return self._inicio[1]

    def getCasillasEspeciales(self):
        """Retorna el diccionario de casillas especiales
        """
        return self._casillas_especiales

    def _armar(self):
        """Retorna una lista para la GUI que contiene una matriz de objetos Casilla
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
        """Retorna True si el evento fue en una de las casillas del tablero, False en caso contrario
        """
        for fila in self._casillas:
            for casilla in fila:
                if event == casilla.getKey():
                    return True
        return False        

    def habilitar(self, window):
        """Habilita todas las casillas del tablero que esten desocupadas (que no haya una ficha)
        """
        for fila in self._casillas:
            for casilla in fila:
                if casilla.estaOcupada():
                    continue
                else:
                    casilla.habilitar()
                    window[casilla.getKey()].update(disabled=False)

    def deshabilitar(self, window):
        """Deshabilita todas las casillas del tablero que esten desocupadas (que no haya una ficha)
        """
        for fila in self._casillas:
            for casilla in fila:
                if casilla.estaOcupada():
                    continue
                else:
                    casilla.deshabilitar()
                window[casilla.getKey()].update(disabled=True)
    
    def insertarFicha(self,key,window,letra):
        """Setea los parámetros necesarios para indicar que se inserto una ficha en una casilla determinada
        """
        self._palabra.append(key)
        aux = key.split("-")
        self._casillas[int(aux[0])-1][int(aux[1])-1].ocupar()
        self._casillas[int(aux[0])-1][int(aux[1])-1].deshabilitar()
        self._casillas[int(aux[0])-1][int(aux[1])-1].setContenido(letra)
        self._casillas[int(aux[0])-1][int(aux[1])-1].setColor(('white','#684225'))
        window[key].update(letra, button_color=('white','#684225'), disabled_button_color=('white','#684225'), disabled=True)

    def reiniciarPalabra(self):
        """Setea la palabra a vacío
        """
        self._palabra=[]

    def reiniciarPalabraInicio(self):
        """Borra todas las letras de la palabra menos la de inicio
        """
        if (self._inicio[0] in self._palabra):
            self._palabra=[self._inicio[0]]
        else:
            self._palabra=[]

    def devolverFichas(self,window):
        """Setea los parámetros necesarios para indicar que las casillas ocupadas por fichas ahora estan desocupadas.\n
        Retorna una lista que contiene las letras de las fichas que se sacaron
        """
        letras_devolver = []
        for key in self._palabra:
            if (key != self._inicio[0]):
                aux = key.split('-')
                self._casillas[int(aux[0])-1][int(aux[1])-1].desocupar()
                letras_devolver.append(window[key].GetText())
                especial = False
                for clave in self._casillas_especiales:
                    if key in self._casillas_especiales[clave][0]:
                        window[key].Update(clave, button_color=('black',self._casillas_especiales[clave][1]),disabled_button_color=('black',self._casillas_especiales[clave][1]))
                        especial = True
                if not especial:
                    window[key].Update('', button_color=('black','white'),disabled_button_color=('black','white'))
        self.reiniciarPalabraInicio()
        return letras_devolver

    def verificarPalabra(self):
        """Verifica que la palabra formada este bien formada y posicionada.\n
        Si esta bien formada retorna la palabra y, en caso contrario, retorna "xxxxxx"
        """
        lis_aux=[]
        if (len(self._palabra)>1): # La palabra tiene que tener mas de una letra
            for x in self._palabra:
                elems = x.split('-') # elems[0]: num de fila // elems[1]: num de columna
                for i in range(0,2):
                    elems[i] = int(elems[i])
                lis_aux.append(elems)
            # lis_aux contiene listas de dos elementos que son la key de la letra de la palabra
            lis_ord = sorted(lis_aux, key=lambda valor: valor[1]) # ordena de menor a mayor las keys segun la columna
            a_comparar1 = lis_ord[0][0]
            a_comparar2 = lis_ord[0][1] # guardo el num de columna mas chico
            horizontal = True
            vertical = True
            for e in lis_ord:
                if(e[0] != a_comparar1)or(e[1] != a_comparar2): 
                    horizontal = False
                a_comparar2 += 1
            if (not horizontal):
                lis_ord = sorted(lis_aux, key=lambda valor: valor[0]) # ordena de menor a mayor las keys segun la fila
                a_comparar1 = lis_ord[0][1] 
                a_comparar2 = lis_ord[0][0] # guardo el num de fila mas chico
                for e in lis_ord:
                    if(e[1] != a_comparar1)or(e[0] != a_comparar2):
                        vertical=False
                    a_comparar2 += 1
            if (horizontal)or(vertical):
                self.ordenarPalabra(lis_ord)
                pal=''
                for key in lis_ord:
                    pal += self._casillas[key[0]-1][key[1]-1].getContenido() # Armo la palabra a devolver
                return pal
            else:
                return 'xxxxxx'
        else:
            return 'xxxxxx'
        
    def ordenarPalabra(self, lis_keys_ordenada):
        """Ordena los elementos de la palabra en su orden correcto
        """
        self._palabra = []
        for key in lis_keys_ordenada:
            self._palabra.append((str(key[0])+'-'+str(key[1])))

    def copiaPalabra(self):
        """Retorna una copia de la palabra (lista de keys)
        """
        return self._palabra[:]

    def casillaOcupada(self,key):
        """Devuelve si la casilla pasada por parametro se encuentra ocupada
        """
        aux = key.split("-")
        return self._casillas[int(aux[0])-1][int(aux[1])-1].estaOcupada()

# {---------------------------------------------------------------------------------}
# {--------------------------- CREACIÓN DEL OBJETO ---------------------------------}
# {---------------------------------------------------------------------------------}

def crear_tablero(bolsa_fichas):
    casillas_especiales1 = {
    "x2":(("2-6","2-10","6-2","6-14","7-7","7-9","9-7","9-9","10-2","10-14","14-6","14-10",), "#2283BB"),
    "x3":(("1-4","1-12","3-7","3-9","4-1","4-8","4-15","7-3","7-13","8-4","8-12","9-3","9-13","12-1","12-15","12-8","13-7","13-9","15-4","15-12"), "#45BB22"),
    "-3":(("1-1","1-8","1-15","8-1","8-15","15-1","15-8","15-15"), '#F02121'),
    "-2":(("2-2","2-14","3-3","3-13","13-3","13-13","14-2","14-14"), '#F06C21'),
    "-1":(("4-4","4-12","5-5","5-11","6-6","6-10","10-6","10-10","11-5","11-11","12-4","12-12"), '#F0B121')
    }
    casillas_especiales2 = {
        "x2":(('2-5','2-12','4-10','5-2','8-8','8-12','8-18','10-3','10-17','12-2','12-8','12-12','15-18','16-10','18-8','18-15'), "#2283BB"),
        "x3":(('1-17','3-19','7-10','13-10','17-1','19-3'), "#45BB22"),
        "-3":(('2-15','5-18','8-4','8-16','12-4','12-16','15-2','18-5'), '#F02121'),
        "-2":(('1-3','3-1','5-7','5-13','15-7','15-13','17-19','19-17'), '#F06C21'),
        "-1":(('2-8','8-2','10-7','10-13','12-18','18-12'), '#F0B121')
    }
    casillas_especiales3 = {}

    num_random = random.randint(1,3)

    if num_random == 1:
        tamaño = 15
        tablero = Tablero(tamaño,casillas_especiales1,inicio=("8-8",bolsa_fichas.letras_random(1)[0]))
    elif num_random == 2:
        tamaño = 19
        tablero = Tablero(tamaño,casillas_especiales2,inicio=("10-10",bolsa_fichas.letras_random(1)[0]))
    else:
        tamaño = 20
        tablero = Tablero(tamaño,casillas_especiales2,inicio=("10-10",bolsa_fichas.letras_random(1)[0]))#3

    pad_tablero = {
        1:{"pad-izq":126,"pad-der":146,"pad-top":70,"pad-bot":70}, # medidas para tablero 1
        2:{"pad-izq":71,"pad-der":81,"pad-top":23,"pad-bot":23}, # medidas para tablero 2
        3:{"pad-izq":61,"pad-der":61,"pad-top":10,"pad-bot":10}, # medidas para tablero 3
    }

    return [tablero,pad_tablero,num_random,tamaño]