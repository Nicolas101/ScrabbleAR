import PySimpleGUI as sg
import random
from Juego.Clases.Casilla import Casilla

# {---------------------------------------------------------------------------------}
# {------------------------------ CLASE TABLERO ------------------------------------}
# {---------------------------------------------------------------------------------}

class Tablero:
    """Esta clase crea un objeto Tablero que es una matriz de objetos Casilla.\n
    Parámetros:\n
    tamaño: es la dimensión de la matriz (TxT).\n
    casillas_especiales: es un diccionario que contiene las keys de las casillas que son "especiales".\n
    inicio: es una tupla que contiene la key de la casilla de inicio del juego y una letra para esa casilla (key,letra).\n
    """
    def __init__(self, tamaño, tipo, casilas_especiales=None, inicio=(None,None)):
        self._tamaño = tamaño
        self._tipo = tipo
        self._casillas_especiales = casilas_especiales
        self._inicio = inicio
        self._casillas = [] # matriz que contiene todos los objetos "casilla" del tablero
        self._palabra = [inicio[0]] # lista de keys de las fichas que estan formando la palabra
        self._habilitado = False

    def getLayout(self):
        """Crea un layout para PySimpleGUI y lo retorna
        """
        return self._armar()

    def getLayoutActualizado(self):
        """Retorna el layout para PySimpleGUI guardado anteriormente
        """
        layout = []
        for fila in self._casillas:
            fila_casilla = []
            for casilla in fila:
                fila_casilla.append(casilla.getLayout())
            layout.append(fila_casilla)
        return layout

    def getTamaño(self):
        return self._tamaño

    def getLetraInicio(self):
        """Retorna la letra de la ficha de inicio
        """
        return self._inicio[1]

    def getCasillasEspeciales(self):
        """Retorna el diccionario de casillas especiales
        """
        return self._casillas_especiales

    def _armar(self):
        """Retorna una lista para PySimpleGUI que contiene una lista(matriz) de objetos Casilla
        """
        layout = []
        for i in range(1, self._tamaño + 1):
            fila_layout = []
            fila_casillas = []
            for j in range(1, self._tamaño + 1):
                especial = False
                key = str(i)+"-"+str(j)

                #Creación de una casilla Especial:
                for clave in self._casillas_especiales:
                    if key in self._casillas_especiales[clave]:
                        especial = True
                        casilla = Casilla(r"Data/Images/Juego/Tablero"+self._tipo+r"/casilla-especial"+clave+".png",key,especial=(True,clave),background="#40B7C9")

                if not especial:
                    if key == self._inicio[0]:
                        #Creación de la casilla de inicio:
                        casilla = Casilla(r"Data/Images/Juego/Tablero"+self._tipo+r"/letra-"+self._inicio[1]+".png",key,deshabilitada=True,ocupada=True,ficha=self._inicio[1],background="#40B7C9")
                    else:
                        #Creacion de una casilla vacia:
                        casilla = Casilla(r"Data/Images/Juego/Tablero"+self._tipo+r"/casilla-vacia.png",key,background="#40B7C9")

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
                if event == casilla.getKey() and not casilla.estaDeshabilitada():
                    return True
        return False

    def estaHabilitado(self):
        return self._habilitado

    def habilitar(self):
        self._habilitado = True

    def deshabilitar(self):
        self._habilitado = False

    def insertarFicha(self,key,window,letra):
        """Setea los parámetros necesarios para indicar que se inserto una ficha en la casilla especificada(key)
        """
        self._palabra.append(key)
        aux = key.split("-")
        self._casillas[int(aux[0])-1][int(aux[1])-1].ocupar()
        self._casillas[int(aux[0])-1][int(aux[1])-1].deshabilitar()
        self._casillas[int(aux[0])-1][int(aux[1])-1].setImagen(r"Data/Images/Juego/Tablero"+self._tipo+r"/letra-"+letra+".png")
        self._casillas[int(aux[0])-1][int(aux[1])-1].setFicha(letra)
        window.Element(key).Update(image_filename=self._casillas[int(aux[0])-1][int(aux[1])-1].getImagen())

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

            if key != self._inicio[0]: #Si no es la ficha de inicio:
                aux = key.split('-')
                letras_devolver.append(self._casillas[int(aux[0])-1][int(aux[1])-1].getFicha())
                self._casillas[int(aux[0])-1][int(aux[1])-1].desocupar()
                self._casillas[int(aux[0])-1][int(aux[1])-1].habilitar()

                #Actualizo el contenido de la casilla:
                if self._casillas[int(aux[0])-1][int(aux[1])-1].esEspecial():
                    self._casillas[int(aux[0])-1][int(aux[1])-1].setImagen(r"Data/Images/Juego/Tablero"+self._tipo+r"/casilla-especial"+self._casillas[int(aux[0])-1][int(aux[1])-1].getEspecial()+".png")
                else:
                    self._casillas[int(aux[0])-1][int(aux[1])-1].setImagen(r"Data/Images/Juego/Tablero"+self._tipo+r"/casilla-vacia.png")
                window.Element(key).Update(image_filename=self._casillas[int(aux[0])-1][int(aux[1])-1].getImagen())

        self.reiniciarPalabraInicio()
        return letras_devolver

    def verificarPalabra(self):
        """Verifica que la palabra formada este bien formada y posicionada.\n
        Si esta bien formada retorna la palabra y, en caso contrario, retorna "xxxxxx"
        """
        con_inicio = self._inicio[0] in self._palabra
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
                    pal += self._casillas[key[0]-1][key[1]-1].getFicha() # Armo la palabra a devolver
                return [pal,con_inicio]
            else:
                return ['xxxxxx',con_inicio]
        else:
            return ['xxxxxx',con_inicio]

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
    """Crea un objeto tablero y lo devuelve
    """

    casillas_especiales1 = {
    "x2":("2-6","2-10","6-2","6-14","7-7","7-9","9-7","9-9","10-2","10-14","14-6","14-10"),
    "x3":("1-4","1-12","3-7","3-9","4-1","4-8","4-15","7-3","7-13","8-4","8-12","9-3","9-13","12-1","12-15","12-8","13-7","13-9","15-4","15-12"),
    "-3":("1-1","1-8","1-15","8-1","8-15","15-1","15-8","15-15"),
    "-2":("2-2","2-14","3-3","3-13","13-3","13-13","14-2","14-14"),
    "-1":("4-4","4-12","5-5","5-11","6-6","6-10","10-6","10-10","11-5","11-11","12-4","12-12"),
    }
    casillas_especiales2 = {
        "x2":('2-5','2-12','4-10','5-2','8-8','8-12','8-18','10-3','10-17','12-2','12-8','12-12','15-18','16-10','18-8','18-15'),
        "x3":('1-17','3-19','7-10','13-10','17-1','19-3'),
        "-3":('2-15','5-18','8-4','8-16','12-4','12-16','15-2','18-5'),
        "-2":('1-3','3-1','5-7','5-13','15-7','15-13','17-19','19-17'),
        "-1":('2-8','8-2','10-7','10-13','12-18','18-12'),
    }
    casillas_especiales3 = {
        "x2":('5-1','3-12','5-7','5-21','6-17','8-8','8-13','9-4','11-19','12-15','13-8','14-4','15-11','16-17','17-1','17-21','18-8','19-12'),
        "x3":('3-11','4-2','4-20','5-6','5-16','7-12','9-8','10-3','10-19','11-15','14-8','15-5','15-12','15-17','18-2','18-9','18-13','18-20'),
        "-3":('1-5','1-17','4-8','4-13','7-17','8-4','8-9','8-14','12-7','12-19','13-4','13-14','17-7','17-16','19-11','21-5','21-17'),
        "-2":('2-4','2-18','4-9','4-14','7-5','7-10','8-18','9-14','11-7','12-3','13-18','14-14','15-10','17-6','17-15','20-4','20-18'),
        "-1":('3-3','3-10','3-19','5-15','6-5','7-11','9-18','10-7','10-15','11-3','14-9','14-13','14-18','16-5','18-14','19-3','19-10','19-19')
    }

    num_tablero = random.randint(1,3)

    if num_tablero == 1:
        tamaño = 15
        tablero = Tablero(tamaño,str(num_tablero),casillas_especiales1,inicio=("8-8",bolsa_fichas.letras_random(1)[0]))
    elif num_tablero == 2:
        tamaño = 19
        tablero = Tablero(tamaño,str(num_tablero),casillas_especiales2,inicio=("10-10",bolsa_fichas.letras_random(1)[0]))
    else:
        tamaño = 21
        tablero = Tablero(tamaño,str(num_tablero),casillas_especiales3,inicio=("11-11",bolsa_fichas.letras_random(1)[0]))

    return tablero
