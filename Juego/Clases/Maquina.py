from Juego.Clases.Jugador import Jugador
from Juego.Clases.FilaDeFichas import FilaFichas
from Juego.Clases.BolsaFichas import BolsaFichas
from Juego.Clases.Tablero import Tablero    
from pattern.text.es import verbs, tag, spelling, lexicon, parse, split
import random

# {---------------------------------------------------------------------------------}
# {------------------------------ CLASE MAQUINA ------------------------------------}
# {---------------------------------------------------------------------------------}

class Maquina(Jugador):
    """Es una subclase de la clase Jugador que contiene todo el comportamiento del oponente 
    """
    def armarPalabra(self, fila_fichas, bolsa_fichas, tablero, dificultad,clases_validas):
        """Intenta armar una palabra con sus fichas. \n
        Si la palabra es correcta retorna: la palabra y la cantidad de fichas a reponer\n
        Si no pudo formar una palabra retorna: "xxxxxx" y un 7, indicando que se deben cambiar todas las fichas
        """
        lis_letras = list(map(lambda l: l.lower(), fila_fichas.getLetras())) #lis_letras contiene las letras de la maquina en minuscula  
        #si se debe usar la letra de inicio se la agrega a lis letras 
        if (tablero.copiaPalabra() != []): 
            letra_inicio = tablero.getLetraInicio().lower()
            lis_letras.append(letra_inicio)
        else:
            letra_inicio = '0'
        palabra_encontrada = ''
        #se llama al metodo _intentarArmar para buscar una palabra que se pueda armar con las letras que se tiene
        palabra_encontrada = self._intentarArmar(verbs.keys(),dificultad,lis_letras,letra_inicio,clases_validas)
        if (palabra_encontrada == 'xxxxxx'):
            palabra_encontrada = self._intentarArmar(lexicon.keys(),dificultad,lis_letras, letra_inicio,clases_validas)
            if (palabra_encontrada == 'xxxxxx'):
                palabra_encontrada = self._intentarArmar(lexicon.keys(),dificultad,lis_letras,letra_inicio,clases_validas)
        if (palabra_encontrada != 'xxxxxx'):
            #si se encontró una palabra la devuelve a esta junto con la cantidad de letras nuevas que necesita la maquina
            aux = list(map(lambda letra: letra,palabra_encontrada))
            if (letra_inicio != '0'):
                aux.remove(letra_inicio)
            nuevo_string = ''
            for x in aux:
                nuevo_string += x
            fila_fichas.eliminarLetras(nuevo_string.upper())
            cant_letras_a_cambiar = len(nuevo_string) #si la palabra es correcta, este es el numero de nuevas letras que necesita la fila de fichas
            return [palabra_encontrada.upper(), cant_letras_a_cambiar]
        else:
            #si no encontró una palabra se devuelve 'xxxxxx' y se especifica que se deben cambiar todas las letras
            cant_letras_a_cambiar = 7
            
            return ['xxxxxx', cant_letras_a_cambiar]

    def _intentarArmar(self, diccionario, dificultad, lis_letras, letra_inicio,clases_validas):
        """Busca una palabra que pueda armarse con las letras que tiene la maquina en el diccionario
        pasado por parametro(verbs, lexicon o spelling)
        """
        lis_letras_aux = lis_letras[:]
        for palabra in diccionario:
            #se pasa por cada palabra del diccionario hasta encontrar una que se pueda armar
            #utilizando las letras que se tienen y que, si se esta en nivel medio o dificil, sea un adjetivo o verbo
            valida = True
            if (len(palabra)>2):
                encontro = True
                for letra in palabra:
                    if letra in lis_letras_aux:
                        lis_letras_aux.remove(letra.lower())
                    else:
                        encontro = False
                        lis_letras_aux = lis_letras[:]
                        break
                if (encontro):
                    if ((letra_inicio != '0')and(letra_inicio in palabra))or(letra_inicio == '0'):
                        if (dificultad != '-FACIL-'):
                            valida = self._verificarPalabra(palabra,clases_validas)
                        if(valida):
                            palabra_encontrada = palabra
                            break
                        else:
                            encontro = False
                    else:
                        encontro = False
        if encontro:
            return palabra_encontrada
        else:
            return 'xxxxxx'
            
    def _verificarPalabra(self, palabra,clases_validas):
        """Verifica que la palabra sea correcta para la especificacion
        de la dificultad en la que se esta jugando
        """
        aux = parse(palabra).split()[0][0][1]
        if aux in clases_validas:
            return True
        else:
            return False

    def insertarPalabra(self, palabra, tablero, window, tamaño):
        """Inserta la palabra generada por la maquina en el tablero
        """
        if tablero.copiaPalabra() != []:
            self._insertarConInicio(palabra, tablero, window) #si la palabra utiliza la letra de inicio se usa este metodo
        else:
            self._insertarSinInicio(palabra, tablero, window,tamaño)
        
    def _insertarConInicio(self, palabra, tablero, window):
        """Inserta la palabra en el tablero teniendo en cuenta que se debe utilizar la letra de inicio de juego
        """
        key_inicio = tablero.copiaPalabra()[0] #consigo la key de la letra de inicio
        #pos de inicio toma el valor de lo que hay que restarle a la key de incio para conseguir la key donde ira la primer letra de la palabra
        pos_de_inicio = 0
        for letra in palabra:
            if letra == tablero.getLetraInicio():
                break
            pos_de_inicio += 1
        key_primera_int = []
        for elem in key_inicio.split('-'):
            key_primera_int.append(int(elem))
        ingreso = random.randint(0,1) #0: ingresa la palabra VERTICALMENTE/ 1: ingresa la palabra HORIZONTALMENTE
        key_primera_int[ingreso] -= pos_de_inicio #le resto a uno de los dos elemtos de key_primera_int(dependiendo si voy a ingresar vertical u horizontal) pos_de_inicio y asi obtengo la primer key donde voy a insertar
        #voy insertando las letras en el tablero siempre y cuando no sean la de inicio que ya viene insertada
        pase_la_de_inicio = False
        #voy insertando las letras en el tablero siempre y cuando no sean la de inicio que ya viene insertada
        for letra in palabra:
            if (letra != tablero.getLetraInicio())or(pase_la_de_inicio):
                key = str(key_primera_int[0])+'-'+str(key_primera_int[1])
                tablero.insertarFicha(key, window, letra)
            else:
                pase_la_de_inicio = True
            key_primera_int[ingreso] += 1

        #ordeno las keys para que quede cada key con la letra que le corresponde y asi poder sumar bien los puntos
        lis_aux_int = []
        for key in tablero.copiaPalabra():
            key_split = key.split('-')
            lis_aux_int.append([(int(key_split[0])),(int(key_split[1]))])#lis_aux_int almacena las keys pero en int en vez de string
        if (ingreso == 1):
            lis_ord = sorted(lis_aux_int, key=lambda valor: valor[1]) # ordena de menor a mayor las keys segun la columna
        else:
            lis_ord = sorted(lis_aux_int, key=lambda valor: valor[0]) # ordena de menor a mayor las keys segun la fila
        tablero.ordenarPalabra(lis_ord)

    def _insertarSinInicio(self, palabra, tablero, window, tamaño):
        """Inserta la palabra en un lugar al azar que sea válido
        """
        ingresada = False
        #se repite el loop hasta que se pueda ingresar la palabra
        while (not ingresada):
            fila_columna = [random.randint(1,tamaño), random.randint(1,tamaño)] #posicion al azar
            fila_columna_aux = fila_columna[:]
            como_insertar = random.randint(0,1) #0: inserta VERTICAL / 1: inserta HORIZONTAL
            lugar_valido = True #esta variable permanecera en true si el lugar seleccionado es valido
            for letra in palabra:
                #este loop verifica que haya el espacio libre necesario para insertar la palabra
                #si hay una casilla ocupada o se "cae" del tablero, se pone la variable lugar valido en false
                if (fila_columna_aux[como_insertar]>tamaño):
                    lugar_valido = False
                    break
                key = str(fila_columna_aux[0])+'-'+str(fila_columna_aux[1])
                if (tablero.casillaOcupada(key)):
                    lugar_valido = False
                    break
                fila_columna_aux[como_insertar] += 1
            if (lugar_valido):
                #si el lugar era valido se inserta la palabra en el tablero
                for letra in palabra:
                    key = str(fila_columna[0])+'-'+str(fila_columna[1])
                    tablero.insertarFicha(key, window, letra)
                    fila_columna[como_insertar] += 1
                ingresada = True

    def nuevasLetras(self, fila_fichas, nuevas_letras, tablero, palabra_armada):
        """Agrega las nuevas letras pasadas por parametro a la variable _letras de la fila de fichas de la maquina
        ademas reinicia la variable _palabra del tablero ya que esta palabra ya fue insertada
        """
        #si la maquina pudo armar la palabra se pone vacia la variable _palabra
        #en caso contrario primero se debe verificar primero si la key de inicio esta en la variable ya que esta no se debe borrar
        if palabra_armada:
            tablero.reiniciarPalabra()
        else:
            if tablero.copiaPalabra() == []:
                tablero.reiniciarPalabra()
            else:
                tablero.reiniciarPalabraInicio()
        #se agregan las nuevas letras a la fila de fichas de la maquina
        for letra in nuevas_letras:
            fila_fichas.agregarLetra(letra)

            
        
        



