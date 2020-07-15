import random
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

def crearBolsa ():
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