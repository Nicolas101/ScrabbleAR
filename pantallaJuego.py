import PySimpleGUI as sg
from claseTablero import Tablero
from claseTablero import Casilla
import random

# {---------------------------------------------------------------------------------}
# {----------------------------------- TABLERO -------------------------------------}
# {---------------------------------------------------------------------------------}  

num_random = random.randint(1,3)

casillas_especiales1 = {
    "+2":(("2-6","2-10","6-2","6-14","7-7","7-9","9-7","9-9","10-2","10-14","14-6","14-10",), "#2283BB"),
    "+3":(("1-4","1-12","3-7","3-9","4-1","4-8","4-15","7-3","7-13","8-4","8-12","9-3","9-13","12-1","12-15","12-8","13-7","13-9","15-4"), "#45BB22"),
    "-3":(("1-1","1-8","1-15","8-1","8-15","15-1","15-8","15-15"), '#F02121'),
    "-2":(("2-2","2-14","3-3","3-13","13-3","13-13","14-2","14-14"), '#F06C21'),
    "-1":(("4-4","4-12","5-5","5-11","6-6","6-10","10-6","10-10","11-5","11-11","12-4","12-12"), '#F0B121')
}
casillas_especiales2 = {}
casillas_especiales3 = {}

if num_random == 1:
    tablero = Tablero(15,15,casillas_especiales1)
elif num_random == 2:
    tablero = Tablero(20,20,casillas_especiales1)#2
else:
    tablero = Tablero(25,25,casillas_especiales1)#3

# {---------------------------------------------------------------------------------}
# {-------------------------------- BOLSA DE FICHAS --------------------------------}
# {---------------------------------------------------------------------------------}

def letra_random(bolsa_fichas):
    letras = list(bolsa_fichas.keys())
    string_letras=''
    for i in letras:
        string_letras=string_letras+(i*bolsa_fichas[i]['cantidad'])
    return random.choice(string_letras)


bolsa_fichas = {'A':{'puntuacion':1,'cantidad':11},'B':{'puntuacion':3,'cantidad':3},'C':{'puntuacion':2,'cantidad':4},
                'D':{'puntuacion':2,'cantidad':4},'E':{'puntuacion':1,'cantidad':11},'F':{'puntuacion':4,'cantidad':2},
                'G':{'puntuacion':2,'cantidad':2},'H':{'puntuacion':4,'cantidad':2},'I':{'puntuacion':1,'cantidad':6},
                'J':{'puntuacion':6,'cantidad':2},'K':{'puntuacion':8,'cantidad':1},'L':{'puntuacion':1,'cantidad':4},
                'M':{'puntuacion':3,'cantidad':3},'N':{'puntuacion':1,'cantidad':5},'Ñ':{'puntuacion':8,'cantidad':1},
                'O':{'puntuacion':1,'cantidad':8},'P':{'puntuacion':3,'cantidad':2},'Q':{'puntuacion':8,'cantidad':1},
                'R':{'puntuacion':1,'cantidad':4},'S':{'puntuacion':1,'cantidad':7},'T':{'puntuacion':1,'cantidad':4},
                'U':{'puntuacion':1,'cantidad':6},'V':{'puntuacion':4,'cantidad':2},'W':{'puntuacion':8,'cantidad':1},
                'X':{'puntuacion':8,'cantidad':1},'Y':{'puntuacion':4,'cantidad':1},'Z':{'puntuacion':10,'cantidad':1}}

# {---------------------------------------------------------------------------------}
# {------------------------------ FILA DE FICHAS -----------------------------------}
# {---------------------------------------------------------------------------------}

def fila_fichasJ():
    lis = []
    keys = []
    for i in range(1,8):
        lis.append(sg.Button(letra_random(bolsa_fichas),key="fJ-"+str(i),pad=(0,0),size=(7,1),disabled_button_color=('#747678','#747678'),button_color=('black','white')))
        keys.append("fJ-"+str(i)) 

    return (lis,keys)

def fila_fichasM():
    lis = []
    for i in range(1,8):
        lis.append(sg.Button(" ",key="fM-"+str(i),pad=(0,0),size=(7,1),disabled_button_color=('black','white'),button_color=('black','white'),disabled=True))

    return lis

layout_fichasMaquina = [fila_fichasM()]

valores_fichasJugador = fila_fichasJ()
keys_fichasJ = valores_fichasJugador[1]
layout_fichasJugador = [valores_fichasJugador[0]]   


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
    [sg.Button("Cambiar fichas")],
    [sg.Text("Seleccione las fichas que desea cambiar",visible=False)],
    [sg.Button("Aceptar",visible=False)]
]

# {---------------------------------------------------------------------------------}
# {----------------------------- PANTALLA DE JUEGO ---------------------------------}
# {---------------------------------------------------------------------------------}

layout_game = [  
    [sg.Column(layout_fichasMaquina,pad=((0,0),(0,20)))],
    [sg.Column(tablero.getDiseño())],
    [sg.Column(layout_fichasJugador,pad=((0,0),(20,0)))]
]

layout = [
    [sg.Column(layout_game,background_color="#71B3BD"), sg.Column(layout_barraDate,element_justification="center",size=(223,450))]
]

pantalla_juego = sg.Window("Scrabble",layout,background_color="#71B3BD")


# {---------------------------------------------------------------------------------}
# {--------------------------- PROGRAMA PRINCIAPL ----------------------------------}
# {---------------------------------------------------------------------------------}

def main():
    while True:
        event, values = pantalla_juego.read()
        print(values)
        if(event is None):
            break
        elif(event in keys_fichasJ):
            tablero.habilitar(pantalla_juego)
            ficha_clicked = event
        elif(event in tablero.getKeys()):
            pantalla_juego[event].Update(pantalla_juego[ficha_clicked].GetText())
            pantalla_juego[ficha_clicked].Update(disabled=True)
            tablero.deshabilitar(pantalla_juego)
        
    pantalla_juego.close() 

if __name__ == "__main__":
    main()



















