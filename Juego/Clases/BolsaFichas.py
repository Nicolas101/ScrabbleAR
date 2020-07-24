import random

# {---------------------------------------------------------------------------------}
# {--------------------------- CLASE BOLSA DE FICHAS -------------------------------}
# {---------------------------------------------------------------------------------}

class BolsaFichas():
    """Bolsa de fichas contiene todas las letras (fichas) que se van a utilizar en la partida
    """

    def __init__(self, bolsa_fichas):
        self._bolsa_fichas = bolsa_fichas
        self._habilitada = False
        self._cant_letras = self._contarLetras()

    def _contarLetras(self):
        """Retorna la cantidad de letras que posee el diccionario de letras al inicio
        """
        cant_letras = 0
        for letra in self._bolsa_fichas:
            cant_letras += self._bolsa_fichas[letra]['cantidad']
        return cant_letras   

    def letras_random(self, cantidad):
        """Retorna una lista eligiendo tantas letras (indicadas en el parámetro) de forma aleatoria de la bolsa de fichas.\n
        Si no hay más letras disponibles en la bolsa de fichas retorna una lista vacia
        """
        lista_letras = []
        if (cantidad <= self._cant_letras):
            lis_letras_prov = []
            for letra in list(self._bolsa_fichas.keys()):
                for i in range(0, (self._bolsa_fichas[letra]['cantidad'])):
                    lis_letras_prov.append(letra)
            
            for i in range(0,cantidad):
                letra_elegida = random.choice(lis_letras_prov)
                lis_letras_prov.remove(letra_elegida)
                self._bolsa_fichas[letra_elegida]['cantidad'] -= 1
                self._cant_letras -= 1
                lista_letras.append(letra_elegida)

        return lista_letras

    def habilitar(self):
        """Habilita la bolsa de fichas indicando que se esta usando
        """
        self._habilitada = True

    def deshabilitar(self):
        """Deshabilita la bolsa de fichas indicando que se dejo de usar
        """
        self._habilitada = False

    def estaHabilitada(self):
        """Retorna True si la bolsa esta habilitada, False en caso contrario
        """
        return self._habilitada

    def devolverPuntaje(self,palabra,lis_keys,casillas_especiales):
        """Retorna la cantidad de puntos correspondiente a la palabra pasada como parámetro
        """
        puntos = 0
        indice = 0
        print(lis_keys)
        print(palabra)
        for letra in palabra:
            if (lis_keys[indice] in casillas_especiales['x2'][0]):
                puntos += (self._bolsa_fichas[letra]['puntuacion']*2)
            elif (lis_keys[indice] in casillas_especiales['x3'][0]):
                puntos += (self._bolsa_fichas[letra]['puntuacion']*3)
            elif (lis_keys[indice] in casillas_especiales['-1'][0]):
                puntos += (self._bolsa_fichas[letra]['puntuacion']-1)
            elif (lis_keys[indice] in casillas_especiales['-2'][0]):
                puntos += (self._bolsa_fichas[letra]['puntuacion']-2)
            elif (lis_keys[indice] in casillas_especiales['-3'][0]):
                puntos += (self._bolsa_fichas[letra]['puntuacion']-3)
            else:
                puntos += self._bolsa_fichas[letra]['puntuacion']
            indice += 1
        return puntos
    
    def devolverLetras(self, letras_devolver):
        """Devuelve las letras pasadas como parámetro a la bolsa, sumando en 1 su cantidad
        """
        for letra in letras_devolver:
            self._bolsa_fichas[letra]['cantidad'] += 1

# {---------------------------------------------------------------------------------}
# {--------------------------- CREACIÓN DEL OBJETO ---------------------------------}
# {---------------------------------------------------------------------------------}

def crear_bolsa():
    dic_fichas = {'A':{'puntuacion':1,'cantidad':11},'B':{'puntuacion':3,'cantidad':3},'C':{'puntuacion':2,'cantidad':4},
                'D':{'puntuacion':2,'cantidad':4},'E':{'puntuacion':1,'cantidad':11},'F':{'puntuacion':4,'cantidad':2},
                'G':{'puntuacion':2,'cantidad':2},'H':{'puntuacion':4,'cantidad':2},'I':{'puntuacion':1,'cantidad':6},
                'J':{'puntuacion':6,'cantidad':2},'K':{'puntuacion':8,'cantidad':1},'L':{'puntuacion':1,'cantidad':4},
                'M':{'puntuacion':3,'cantidad':3},'N':{'puntuacion':1,'cantidad':5},'Ñ':{'puntuacion':8,'cantidad':1},
                'O':{'puntuacion':1,'cantidad':8},'P':{'puntuacion':3,'cantidad':2},'Q':{'puntuacion':8,'cantidad':1},
                'R':{'puntuacion':1,'cantidad':4},'S':{'puntuacion':1,'cantidad':7},'T':{'puntuacion':1,'cantidad':4},
                'U':{'puntuacion':1,'cantidad':6},'V':{'puntuacion':4,'cantidad':2},'W':{'puntuacion':8,'cantidad':1},
                'X':{'puntuacion':8,'cantidad':1},'Y':{'puntuacion':4,'cantidad':1},'Z':{'puntuacion':10,'cantidad':1}}
    bolsa_fichas = BolsaFichas(dic_fichas)
    return bolsa_fichas