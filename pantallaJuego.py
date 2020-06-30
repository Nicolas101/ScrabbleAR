import PySimpleGUI as sg
from clasesJuego import Tablero
from clasesJuego import Casilla
from clasesJuego import FilaFichas
from clasesJuego import BolsaFichas
from validarPalabra import esValida, clasificar
import random

# {---------------------------------------------------------------------------------}
# {-------------------------------- BOLSA DE FICHAS --------------------------------}
# {---------------------------------------------------------------------------------}

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

# {---------------------------------------------------------------------------------}
# {----------------------------------- TABLERO -------------------------------------}
# {---------------------------------------------------------------------------------}  

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
    tablero = Tablero(15,casillas_especiales1,inicio=("8-8",bolsa_fichas.letras_random(1)[0]))
elif num_random == 2:
    tablero = Tablero(19,casillas_especiales2,inicio=("10-10",bolsa_fichas.letras_random(1)[0]))
else:
    tablero = Tablero(20,casillas_especiales2,inicio=("10-10",bolsa_fichas.letras_random(1)[0]))#3

pad_tablero = {
    1:{"pad-izq":126,"pad-der":146,"pad-top":70,"pad-bot":70}, # medidas para tablero 1
    2:{"pad-izq":71,"pad-der":81,"pad-top":23,"pad-bot":23}, # medidas para tablero 2
    3:{"pad-izq":61,"pad-der":61,"pad-top":10,"pad-bot":10}, # medidas para tablero 3
}

# {---------------------------------------------------------------------------------}
# {------------------------------ FILA DE FICHAS -----------------------------------}
# {---------------------------------------------------------------------------------}

fila_fichasJ = FilaFichas(key_add='FJ', letras=bolsa_fichas.letras_random(7))
fila_fichasM = FilaFichas(key_add='FM', letras=bolsa_fichas.letras_random(7))

# {---------------------------------------------------------------------------------}
# {------------------------------ BARRA DE DATOS -----------------------------------}
# {---------------------------------------------------------------------------------}

barra_datos = [
    [sg.Text("DATOS DE PARTIDA",pad=((45,45),(13,12)))],
    [sg.Text("_"*112)],
    [sg.Text("TIEMPO",pad=((80,),(0,10)))],
    [sg.Button("Pausa",pad=((60,7),(0,0))), sg.Text("00:00",pad=((0,0),(0,0)))],
    [sg.Text("_"*112)],
    [sg.Text("PUNTAJE",pad=((80,55),(0,10)))],
    [sg.Text("• Maquina:",pad=((12,0),(0,0))),sg.Text("0")],
    [sg.Text("• Jugador:",pad=((12,0),(0,0))),sg.Text("0",key="-misPuntos-",pad=((0,0),(0,0)))],
    [sg.Text("_"*112)],
    [sg.Text("TURNO",pad=((85,0),(0,10)))],
    [sg.Text("Tu turno",pad=((85,0),(0,0)))],
    [sg.Text("_"*112)],
    [sg.Button("Confirmar Jugada",size=(20,2),pad=((25,0),(0,3)))],
    [sg.Text('',key='text-confirmar',size=(15,1),pad=((40,0),(0,10)))],
    [sg.Button("Cambiar fichas",size=(15,2),pad=((45,0),(80,0)))],
    [sg.Text("Seleccione fichas para cambiar",key='cambiar_fichas_text',pad=((20,0),(0,0)),visible=False)],
    [sg.Button("Aceptar",pad=((80,0),(0,0)),visible=False)],
]

# {---------------------------------------------------------------------------------}
# {----------------------------- PANTALLA DE JUEGO ---------------------------------}
# {---------------------------------------------------------------------------------}

window_size = (1000,600)

columna_izq = [  
    [sg.Column(fila_fichasM.getLayout(),pad=((34,0),(0,0)))],
    [sg.Column(tablero.getLayout(),pad=((pad_tablero[num_random]["pad-izq"],pad_tablero[num_random]["pad-der"]),(pad_tablero[num_random]["pad-top"],pad_tablero[num_random]["pad-bot"])))],
    [sg.Column(fila_fichasJ.getLayout(),pad=((34,0),(0,0)))]
]

layout_juego = [
    [sg.Column(columna_izq,background_color="#71B3BD"), sg.VerticalSeparator(), sg.Column(barra_datos,size=(223,600),pad=((0,0),(0,0))), sg.VerticalSeparator()]
]

pantalla_juego = sg.Window("ScrabbleAR - En Juego",layout_juego,size=window_size,background_color="#71B3BD")

# {---------------------------------------------------------------------------------}
# {----------------------- PANTALLA DE SELECCIONAR NIVEL ---------------------------}
# {---------------------------------------------------------------------------------}

layout_selec_nivel = [
    [sg.Text("¿Qué nivel deseas jugar?",background_color="#71B3BD",font=("Fixedsys",34),pad=((30,30),(150,50)))],
    [sg.Button("Fácil",key="-FACIL-",size=(18,1),font=("Arial",18),pad=((0,15),(0,15))),sg.Button("Medio",key="-MEDIO-",size=(18,1),font=("Arial",18),pad=((0,0),(0,15)))],
    [sg.Button("Dificil",key="-DIFICL-",size=(18,1),font=("Arial",18),pad=((0,15),(0,0))),sg.Button("Personalizado",key="-PERSONALIZADO-",size=(18,1),font=("Arial",18),pad=((0,0),(0,0)))],
]
pantalla_selec_nivel = sg.Window("ScrabbleAR - Selección de nivel",layout_selec_nivel,size=window_size,background_color="#71B3BD",element_justification="center")

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
