import PySimpleGUI as sg
from PantallaJuego.objetos.Casilla import Casilla
from PantallaJuego.objetos.Tablero import Tablero, crearTablero
from PantallaJuego.objetos.FilaDeFichas import FilaFichas, crearFilaFichas
from PantallaJuego.objetos.BolsaFichas import BolsaFichas, crearBolsa
from PantallaJuego.validarPalabra import esValida, clasificar
from PantallaJuego.layouts import layoutJuego, layoutNivel
import random

# {---------------------------------------------------------------------------------}
# {-------------------------------- BOLSA DE FICHAS --------------------------------}
# {---------------------------------------------------------------------------------}


bolsa_fichas = crearBolsa()

# {---------------------------------------------------------------------------------}
# {----------------------------------- TABLERO -------------------------------------}
# {---------------------------------------------------------------------------------}  

tablero,pad_tablero,num_random= crearTablero(bolsa_fichas)

# {---------------------------------------------------------------------------------}
# {------------------------------ FILA DE FICHAS -----------------------------------}
# {---------------------------------------------------------------------------------}

fila_fichasJ = crearFilaFichas(bolsa_fichas, 'FJ')
fila_fichasM = crearFilaFichas(bolsa_fichas, 'FM')


# {---------------------------------------------------------------------------------}
# {----------------------------- PANTALLA DE JUEGO ---------------------------------}
# {---------------------------------------------------------------------------------}

window_size = (1000,600)

pantalla_juego = layoutJuego.crearLayout(tablero, fila_fichasJ, fila_fichasM, num_random, pad_tablero,window_size)

# {---------------------------------------------------------------------------------}
# {----------------------- PANTALLA DE SELECCIONAR NIVEL ---------------------------}
# {---------------------------------------------------------------------------------}

pantalla_selec_nivel = layoutNivel.crearLayout(window_size)

# {---------------------------------------------------------------------------------}
# {--------------------------- PROGRAMA PRINCIAPL ----------------------------------}
# {---------------------------------------------------------------------------------}

def main():
    nivel = ""
    while True:
        event, values = pantalla_selec_nivel.read()
        if event is None:
            break
        elif event == "-FACIL-":
            nivel = "facil"
            break
        elif event == "-MEDIO-":
            nivel = "medio"
            break
        elif event == "-DIFICL-":
            nivel = "dificil"
            break
        elif event == "-PERSONALIZADO-":
            nivel = "personalizado"
            break
    pantalla_selec_nivel.close()

    if nivel != "":
        puntos_jugador = 0
        #pantalla_juego.UnHide()
        while True:
            event, values = pantalla_juego.read()
            if(event is None):
                break
            
            elif fila_fichasJ.click(event):
                if bolsa_fichas.estaHabilitada():
                    pass
                else:
                    if not fila_fichasJ.hayFichaSelected():
                        fila_fichasJ.marcarFichaSelected(pantalla_juego,event) 
                    else:
                        fila_fichasJ.desmarcarFichaSelected(pantalla_juego)
                        fila_fichasJ.marcarFichaSelected(pantalla_juego,event)
                    tablero.habilitar(pantalla_juego)
                
            elif tablero.click(event): 
                tablero.insertarFicha(event,pantalla_juego,pantalla_juego[fila_fichasJ.getFichaSelected()].GetText()) 
                fila_fichasJ.sacarFicha(pantalla_juego)            
                tablero.deshabilitar(pantalla_juego)

            elif(event == "Confirmar Jugada"):
                palabra = tablero.getPalabra()
                if (esValida(palabra,nivel)):
                    pantalla_juego['text-confirmar'].update('Palabra correcta',visible=True)
                    puntos_jugador += bolsa_fichas.devolverPuntaje(palabra)
                    pantalla_juego["-misPuntos-"].update(str(puntos_jugador))
                    tablero.reiniciarPalabra()
                    cant_letras=len(palabra)
                    fila_fichasJ.insertarFichas(pantalla_juego,bolsa_fichas.letras_random(cant_letras))
                else:
                    fichas_a_devolver=tablero.devolverFichas(pantalla_juego)
                    fila_fichasJ.insertarFichas(pantalla_juego,fichas_a_devolver)
                    pantalla_juego['text-confirmar'].update('Palabra incorrecta',visible=True)

            elif(event == 'Cambiar fichas'):
                bolsa_fichas.habilitar()
                tablero.deshabilitar(pantalla_juego)
                pantalla_juego['cambiar_fichas_text'].Update(visible=True)
                pantalla_juego['Aceptar'].Update(visible=True)
                
            elif(event == 'Aceptar'):
                bolsa_fichas.deshabilitar()
                pantalla_juego['cambiar_fichas_text'].Update(visible=False)
                pantalla_juego['Aceptar'].Update(visible=False)
                
        #pantalla_juego.Hide()
        pantalla_juego.close() 

if __name__ == "__main__":
    main()
