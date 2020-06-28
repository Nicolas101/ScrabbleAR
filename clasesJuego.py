import PySimpleGUI as sg 
import random

# {---------------------------------------------------------------------------------}
# {------------------------------ CLASE CASILLA ------------------------------------}
# {---------------------------------------------------------------------------------}

class Casilla():
    def __init__(self, contenido='', tamaño=None, color=('black','#FFFFFF'), clave=None, ocupado=False, especial=[False, None]):
        self._contenido = contenido
        self._tamaño = tamaño
        self._color = color
        self._key = clave
        self._ocupado = ocupado
        self._especial = especial 
        self._diseño = sg.Button(self._contenido,key=self._key, pad=(0,0), size=self._tamaño, button_color=self._color, disabled_button_color=self._color, disabled=self._ocupado)

    def getKey(self):
        return self._key

    def getDiseño(self):
        return self._diseño

    def habilitar(self):
        self._ocupado = False

    def deshabilitar(self):
        self._ocupado = True

    def setContenido(self,dato):
        self._contenido = dato
    
    def getContenido(self):
        return self._contenido
    
    def setColor(self,color):
        self._color = color

    def getColor(self):
        return self._color

# {---------------------------------------------------------------------------------}
# {------------------------------ CLASE TABLERO ------------------------------------}
# {---------------------------------------------------------------------------------}

class Tablero:
    def __init__(self, tamaño=0, casilas_especiales=None, inicio=(None, None)):
        self._tamaño = tamaño
        self._casillas_especiales = casilas_especiales
        self._lista_casillas = []
        self._inicio = inicio
        self._palabra = [inicio[0]]
        self._layout = self._armar()

    def getLayout(self):
        return self._layout

    def getKeysCasillas(self):
        lista_keys = []
        for casilla in self._lista_casillas:
            lista_keys.append(casilla.getKey())
        return lista_keys
    
    def _armar(self):
        layout = [] 
        for i in range(1, self._tamaño + 1):
            fila_casillas = []
            for j in range(1, self._tamaño + 1):
                especial = False
                key = str(i)+"-"+str(j)
                for clave in self._casillas_especiales:
                    if(key in self._casillas_especiales[clave][0]):
                        casilla = Casilla(clave=key,tamaño=(3,1), contenido=clave, color=('black',self._casillas_especiales[clave][1]), ocupado=True, especial=(True,clave)) #casilla especial
                        especial = True
                if not especial:
                    if key == self._inicio[0]:
                        casilla = Casilla(clave=self._inicio[0],tamaño=(3,1),ocupado=True,contenido=self._inicio[1],color=('white','#684225')) #casilla de inicio
                    else:
                        casilla = Casilla(clave=key,tamaño=(3,1), ocupado=True) #casilla normal
                fila_casillas.append(casilla.getDiseño())
                self._lista_casillas.append(casilla)  
            layout.append(fila_casillas)
        return layout

    def habilitar(self, pantalla_juego):
        for casilla in self._lista_casillas:
            if (casilla.getContenido() in 'x2x3-2-1-3'):
                pantalla_juego[casilla.getKey()].Update(disabled=False)
                casilla.habilitar()

    def deshabilitar(self, pantalla_juego):
        for casilla in self._lista_casillas:
            pantalla_juego[casilla.getKey()].Update(disabled=True)
            casilla.deshabilitar()
    
    def insertar(self,dato,key,pantalla_juego):
        pantalla_juego[key].Update(dato, button_color=('white','#684225'), disabled_button_color=('white','#684225'))
        aux = key.split('-')
        self._lista_casillas[((int(aux[1])-1)+(int(aux[0])-1)*self._tamaño)].setContenido(dato)
        self._lista_casillas[((int(aux[1])-1)+(int(aux[0])-1)*self._tamaño)].setColor(('white','#684225'))
        self._palabra.append(key)

    def devolverFichas(self,pantalla_juego):
        lis_letras = []
        for key in self._palabra:
            if (key!=self._inicio[0]):
                lis_letras.append(pantalla_juego[key].GetText())
                especial = False
                for clave in self._casillas_especiales:
                    if key in self._casillas_especiales[clave][0]:
                        pantalla_juego[key].Update(clave, button_color=('black',self._casillas_especiales[clave][1]),disabled_button_color=('black',self._casillas_especiales[clave][1]))
                        especial = True
                if not especial:
                    pantalla_juego[key].Update('', button_color=('black','white'),disabled_button_color=('black','white'))
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
                pal+= self._lista_casillas[((int(key[1])-1)+(int(key[0])-1)*self._tamaño)].getContenido()
            return pal
        else:
            return 'xxxxxx'

    

    
            

# {---------------------------------------------------------------------------------}
# {--------------------------- CLASE FILA DE FICHAS --------------------------------}
# {---------------------------------------------------------------------------------}

class FilaFichas():
    def __init__(self, cant_fichas=7, key_add=None, letras=None):
        self._cant_fichas = cant_fichas
        self._key_add = key_add
        self._letras = letras # lista de letras que contiene la fila
        self._ficha_selected = [False,None]
        self._fila_fichas = [] # lista de objetos "casilla" de la fila
        self._layout = self._armar() 
        
    def _armar(self):
        layout = []
        for i in range(1,8):
            key = self._key_add +'-'+ str(i)
            if (self._key_add == 'FJ'):
                ficha = Casilla(clave=key, tamaño=(6,2),contenido=self._letras[i-1]) # fichas del jugador
            else:
                ficha = Casilla(clave=key, tamaño=(6,2), ocupado=True) # fichas de la maquina
            self._fila_fichas.append(ficha)
            layout.append(ficha.getDiseño())     
        return [layout]
    
    def habilitarFila(self, pantalla_juego):
        for ficha in self._fila_fichas:
            pantalla_juego[ficha.getKey()].Update(disabled=False)
            ficha.habilitar()

    def deshabilitarFila(self, pantalla_juego):
        for ficha in self._fila_fichas:
            pantalla_juego[ficha.getKey()].Update(disabled=True)
            ficha.deshabilitar()

    def deshabilitarFicha(self, pantalla_juego):
        pantalla_juego[self._ficha_selected[1]].Update('', disabled=True,button_color=('black','#CCCCCC'))
        aux = self._ficha_selected[1].split('-')
        self._fila_fichas[int(aux[1])-1].setContenido("")
        self._fila_fichas[int(aux[1])-1].deshabilitar()
        self._fila_fichas[int(aux[1])-1].setColor(('black','#CCCCCC'))

    def getLayout(self):
        return self._layout

    def getKeysFila(self):
        lista_keys = []
        for ficha in self._fila_fichas:
            lista_keys.append(ficha.getKey())
        return lista_keys

    def marcarFichaSelected(self,pantalla_juego,key):
        self._ficha_selected[0] = True
        self._ficha_selected[1] = key       
        aux = key.split('-')
        self._fila_fichas[int(aux[1])-1].setColor(('black',"#5fefaa"))
        pantalla_juego[key].Update(button_color=('black',"#5fefaa"))

    def desmarcarFichaSelected(self,pantalla_juego):
        pantalla_juego[self._ficha_selected[1]].Update(button_color=('black','white'))
        aux = self._ficha_selected[1].split('-')
        self._fila_fichas[int(aux[1])-1].setColor(('black','white'))
        self._ficha_selected[0] = False

    def hayFichaSelected(self):
        return self._ficha_selected[0]

    def getFichaSelected(self):
        return self._ficha_selected[1]

    def insertarFichas(self,pantalla_juego,fichas):
        for casilla in self._fila_fichas:
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
    
    


        
