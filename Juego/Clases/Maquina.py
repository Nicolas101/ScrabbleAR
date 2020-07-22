try:
    from Juego.Clases.Jugador import Jugador
    from Juego.Clases.FilaDeFichas import FilaFichas
    from Juego.Clases.BolsaFichas import BolsaFichas
    from Juego.Clases.Tablero import Tablero
except ModuleNotFoundError:
    from Clases.Jugador import Jugador
    from Clases.FilaDeFichas import FilaFichas
    from Clases.BolsaFichas import BolsaFichas
    from Clases.Tablero import Tablero
from pattern.text.es import verbs, tag, spelling, lexicon, parse, split

# {---------------------------------------------------------------------------------}
# {------------------------------ CLASE MAQUINA ------------------------------------}
# {---------------------------------------------------------------------------------}

class Maquina(Jugador):
    """Es una subclase de la clase Jugador que contiene todo el comportamiento del oponente
    """

    def cambiarFichas(self,fila_fichas,bolsa_fichas):
        #a implentar
        pass
    
    def armarPalabra(self,fila_fichas,bolsa_fichas,tablero):
        """
        """
        lis_letras = fila_fichas.getLetras()
        if (tablero.copiaPalabra() != []): 
            letra_inicio = tablero.getLetraInicio()
            lis_letras.append(letra_inicio)
        else:
            letra_inicio = '0'
        lis_letras_aux = lis_letras[:] #genera una copia
        encontro = False
        palabra_encontrada = ''
        for palabra in verbs.keys():
            if (len(palabra)>2):
                encontro = True
                for letra in palabra:
                    if letra.upper() in lis_letras_aux:
                        lis_letras_aux.remove(letra.upper())
                    else:
                        encontro = False
                        lis_letras_aux = lis_letras[:]
                        break
                if (encontro):
                    if ((letra_inicio != '0')and(letra_inicio in palabra))or(letra_inicio == '0'):
                        palabra_encontrada = palabra
                        print('1')
                        break
                    else:
                        encontro = False
        if (not encontro):
            for palabra in lexicon.keys():
                if (len(palabra)>2):
                    encontro = True
                    for letra in palabra:
                        if letra.upper() in lis_letras_aux:
                            lis_letras_aux.remove(letra.upper())
                        else:
                            encontro = False
                            lis_letras_aux = lis_letras[:]
                            break
                    if (encontro):
                        if ((letra_inicio != '0')and(letra_inicio in palabra))or(letra_inicio == '0'):
                            palabra_encontrada = palabra
                            print('2')
                            break
                        else:
                            encontro = False
            if (not encontro):
                for palabra in spelling.keys():
                    if (len(palabra)>2):
                        encontro = True
                        for letra in palabra:
                            if letra.upper() in lis_letras_aux:
                                lis_letras_aux.remove(letra.upper())
                            else:
                                encontro = False
                                lis_letras_aux = lis_letras[:]
                                break
                        if (encontro):
                            if ((letra_inicio != '0')and(letra_inicio in palabra))or(letra_inicio == '0'):
                                palabra_encontrada = palabra
                                print('3')
                                break
                            else:
                                encontro = False
        if (encontro):
            print(palabra_encontrada)
            aux = []
            for letra in palabra_encontrada:
                aux.append(letra)
            if (letra_inicio != '0'):
                aux.remove(letra_inicio)
            nuevo_string = ''
            for x in aux:
                nuevo_string += x 
            #fila_fichas.eliminarLetras(nuevo_string)
            #fila_fichas.agregarLetras(bolsa_fichas.letras_random(len(nuevo_string)))
            tablero.reiniciarPalabra()
            return palabra_encontrada
        else:
            print('xxxxx')
            if letra_inicio != '0':
                tablero.reiniciarPalabraInicio()    
            else:
                tablero.reiniciarPalabra()
            #cambiarFichas(fila_fichas, bolsa_fichas)
            return 'xxxxx'



