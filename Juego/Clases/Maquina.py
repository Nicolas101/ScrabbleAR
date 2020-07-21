try:
    from Juego.Clases.Jugador import Jugador
    from Juego.Clases.FilaDeFichas import FilaFichas
    from Juego.Clases.BolsaFichas import BolsaFichas
except ModuleNotFoundError:
    from Clases.Jugador import Jugador
    from Clases.FilaDeFichas import FilaFichas
    from Clases.BolsaFichas import BolsaFichas
from pattern.es import verbs, tag, spelling, lexicon, parse, split

class Maquina(Jugador):

    def cambiarFichas(self,fichas,bolsa_fichas):
        #a implentar
        pass
    
    def armarPalabra(self,fila_fichas,bolsa_fichas):
        lis_letras = fila_fichas.getLetras()
        print(lis_letras)
        lis_letras_aux = lis_letras[:]
        encontro = False
        palabra_encontrada = ''
        for palabra in verbs.keys():
            if (len(palabra)>3):
                encontro = True
                for letra in palabra:
                    if letra.upper() in lis_letras_aux:
                        lis_letras_aux.remove(letra.upper())
                    else:
                        encontro = False
                        lis_letras_aux = lis_letras[:]
                        break
                if (encontro):
                    palabra_encontrada = palabra
                    break
        if (not encontro):
            for palabra in lexicon.keys():
                if (len(palabra)>3):
                    encontro = True
                    for letra in palabra:
                        if letra.upper() in lis_letras_aux:
                            lis_letras_aux.remove(letra.upper())
                        else:
                            encontro = False
                            lis_letras_aux = lis_letras[:]
                            break
                    if (encontro):
                        palabra_encontrada = palabra
                        break
#            if (not encontro):
 #               for palabra in spelling.keys():
  #                  if (len(palabra)>3):
   #                     encontro = True
    #                    for letra in palabra:
     #                       if letra.upper() in lis_letras_aux:
      #                          lis_letras_aux.remove(letra.upper())
       #                     else:
        #                        encontro = False
         #                       lis_letras_aux = lis_letras[:]
          #                      break
           #             if (encontro):
            #                palabra_encontrada = palabra
             #               break
        if (encontro):
            print(palabra_encontrada)
            return palabra_encontrada
        else:
            print('xxxxx')
            return 'xxxxx'



