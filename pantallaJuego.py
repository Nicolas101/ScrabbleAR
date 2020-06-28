import PySimpleGUI as sg
from clasesJuego import Tablero
from clasesJuego import Casilla
from clasesJuego import FilaFichas
from clasesJuego import BolsaFichas
from validarPalabra import Validar, Clasificar
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

num_random = random.randint(1,3)

casillas_especiales1 = {
    "x2":(("2-6","2-10","6-2","6-14","7-7","7-9","9-7","9-9","10-2","10-14","14-6","14-10",), "#2283BB"),
    "x3":(("1-4","1-12","3-7","3-9","4-1","4-8","4-15","7-3","7-13","8-4","8-12","9-3","9-13","12-1","12-15","12-8","13-7","13-9","15-4","15-12"), "#45BB22"),
    "-3":(("1-1","1-8","1-15","8-1","8-15","15-1","15-8","15-15"), '#F02121'),
    "-2":(("2-2","2-14","3-3","3-13","13-3","13-13","14-2","14-14"), '#F06C21'),
    "-1":(("4-4","4-12","5-5","5-11","6-6","6-10","10-6","10-10","11-5","11-11","12-4","12-12"), '#F0B121')
}
casillas_especiales2 = {}
casillas_especiales3 = {}

if num_random == 1:
    tablero = Tablero(15,casillas_especiales1,inicio=("8-8",bolsa_fichas.letras_random(1)[0]))
elif num_random == 2:
    tablero = Tablero(18,casillas_especiales1,inicio=("8-8",bolsa_fichas.letras_random(1)[0]))#2
else:
    tablero = Tablero(20,casillas_especiales1,inicio=("8-8",bolsa_fichas.letras_random(1)[0]))#3

# {---------------------------------------------------------------------------------}
# {------------------------------ FILA DE FICHAS -----------------------------------}
# {---------------------------------------------------------------------------------}

fila_fichasJ = FilaFichas(key_add='FJ', letras=bolsa_fichas.letras_random(7))
fila_fichasM = FilaFichas(key_add='FM', letras=bolsa_fichas.letras_random(7))

# {---------------------------------------------------------------------------------}
# {------------------------------ BARRA DE DATOS -----------------------------------}
# {---------------------------------------------------------------------------------}

layout_barraDate = [
    [sg.Text("DATOS DE PARTIDA")],
    [sg.Text("Tiempo:"),sg.Text("(tiempo correspondiente)")],
    [sg.Button("Pausa")],
    [sg.Text("Maquina:"),sg.Text("(Puntos de la maquina)")],
    [sg.Text("Tus puntos:"),sg.Text("(puntos del jugador)")],
    [sg.Text("Turno:"),sg.Text("(turno correspondiente)")],
    [sg.Button("Confirmar Jugada")],
    [sg.Text('',key='text-confirmar',size=(15,1),visible=False)],
    [sg.Button("Cambiar fichas")],
    [sg.Text("Seleccione fichas para cambiar",key='cambiar_fichas_text',visible=False)],
    [sg.Button("Aceptar",visible=False)],
]

# {---------------------------------------------------------------------------------}
# {----------------------------- PANTALLA DE JUEGO ---------------------------------}
# {---------------------------------------------------------------------------------}

layout_game = [  
    [sg.Column(fila_fichasM.getLayout(),pad=((80,0),(0,10)))],
    [sg.Column(tablero.getLayout())],
    [sg.Column(fila_fichasJ.getLayout(),pad=((80,0),(10,0)))]
]

layout = [
    [sg.Column(layout_game,background_color="#71B3BD"), sg.Column(layout_barraDate,element_justification="center",size=(223,450))]
]

pantalla_juego = sg.Window("ScrabbleAR",layout,background_color="#71B3BD")

# {---------------------------------------------------------------------------------}
# {----------------------- PANTALLA DE SELECCIONAR NIVEL ---------------------------}
# {---------------------------------------------------------------------------------}

layout_nivel = [
    [sg.Text("¿Qué nivel deseas jugar?",background_color="#71B3BD",font=("Fixedsys",26),pad=((30,30),(0,30)))],
    [sg.Button("Fácil",key="-FACIL-",size=(18,1),font=("Arial",14),pad=((0,0),(8,0)))],
    [sg.Button("Medio",key="-MEDIO-",size=(18,1),font=("Arial",14),pad=((0,0),(8,0)))],
    [sg.Button("Dificil",key="-DIFICL-",size=(18,1),font=("Arial",14),pad=((0,0),(8,0)))],
    [sg.Button("Personalizado",key="-PERSONALIZADO-",size=(18,1),font=("Arial",14),pad=((0,0),(8,30)))],
]
pantalla_nivel = sg.Window("ScrabbleAR",layout_nivel,background_color="#71B3BD",element_justification="center",disable_close=True,disable_minimize=True)

# {---------------------------------------------------------------------------------}
# {--------------------------- PROGRAMA PRINCIAPL ----------------------------------}
# {---------------------------------------------------------------------------------}

def main():
    while True:
        event, values = pantalla_nivel.read()
        if event == "-FACIL-":
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
    pantalla_nivel.close()

    cambiar_fichas = False
    #pantalla_juego.UnHide()
    while True:
        event, values = pantalla_juego.read()
        if(event is None):
            break
        
        elif(event in fila_fichasJ.getKeysFila())and(not cambiar_fichas): 
            if not fila_fichasJ.hayFichaSelected():
                fila_fichasJ.marcarFichaSelected(pantalla_juego,event)
                tablero.habilitar(pantalla_juego) 
            else:
                fila_fichasJ.desmarcarFichaSelected(pantalla_juego)
                fila_fichasJ.marcarFichaSelected(pantalla_juego,event)

        elif(event in tablero.getKeysCasillas())and(not cambiar_fichas): 
            dato = pantalla_juego[fila_fichasJ.getFichaSelected()].GetText()
            tablero.insertar(dato,event,pantalla_juego)        
            fila_fichasJ.desmarcarFichaSelected(pantalla_juego)  
            fila_fichasJ.deshabilitarFicha(pantalla_juego)          
            tablero.deshabilitar(pantalla_juego)

        elif(event == "Confirmar Jugada"):
            palabra = tablero.getPalabra()
            if (Validar(palabra,nivel)):
                pantalla_juego['text-confirmar'].update('Palabra correcta',visible=True)
            else:
                fichas_a_devolver=tablero.devolverFichas(pantalla_juego)
                fila_fichasJ.insertarFichas(pantalla_juego,fichas_a_devolver)
                pantalla_juego['text-confirmar'].update('Palabra incorrecta',visible=True)


        elif(event == 'Cambiar fichas'):
            cambiar_fichas = True
            tablero.deshabilitar(pantalla_juego)
            pantalla_juego['cambiar_fichas_text'].Update(visible=True)
            pantalla_juego['Aceptar'].Update(visible=True)
            

        elif(event == 'Aceptar'):
            cambiar_fichas = False
            pantalla_juego['cambiar_fichas_text'].Update(visible=False)
            pantalla_juego['Aceptar'].Update(visible=False)
            
    #pantalla_juego.Hide()
    pantalla_juego.close() 

if __name__ == "__main__":
    main()



















