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
        print(tablero.copiaPalabra())
        if (tablero.copiaPalabra() != []): 
            letra_inicio = tablero.getLetraInicio()
            lis_letras.append(letra_inicio)
        else:
            letra_inicio = ''
        print(lis_letras)
        print(fila_fichas.getLetras())
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
                    if (letra_inicio in palabra_encontrada):
                        palabra_encontrada = palabra
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
                        if (letra_inicio in palabra_encontrada):
                            palabra_encontrada = palabra
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
                            if (letra_inicio in palabra_encontrada):
                                palabra_encontrada = palabra
                                break
                            else:
                                encontro = False
        if (encontro):
            aux = palabra_encontrada.split()
            if (letra_inicio != ''):
                aux.remove(letra_inicio)
            nuevo_string = ''
            for x in aux:
                nuevo_string += x 
            print(nuevo_string)
            print(palabra_encontrada)
            #fila_fichas.eliminarLetras(nuevo_string)
            #fila_fichas.agregarLetras(bolsa_fichas.letras_random(len(nuevo_string)))
            tablero.reiniciarPalabra()
            return palabra_encontrada
        else:
            print('xxxxx')
            if tablero.copiaPalabra() != []:
                tablero.reiniciarPalabraInicio()    
            else:
                tablero.reiniciarPalabra()
            #cambiarFichas(fila_fichas, bolsa_fichas)
            return 'xxxxx'



