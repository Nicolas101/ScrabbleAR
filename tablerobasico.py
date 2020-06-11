import PySimpleGUI as sg
import tableros
import random

# {---------------------------------------------------------------------------------}
# {----------------------------------- TABLERO -------------------------------------}
# {---------------------------------------------------------------------------------}

def habilitar_tablero(pantalla_juego,tam):
    for i in range(0,tam):
        for j in range(0,tam):
            key = str(i)+"-"+str(j)
            pantalla_juego[key].Update(disabled=False)

def desabilitar_tablero(pantalla_juego,tam):
    for i in range(0,tam):
        for j in range(0,tam):
            key = str(i)+"-"+str(j)
            pantalla_juego[key].Update(disabled=True)   



valores_tablero = tableros.main() 
keys_tablero = valores_tablero[1]   # Lista de keys de cada boton del tablero
layout_tablero = valores_tablero[0]
tamanio=valores_tablero[2]  


# {---------------------------------------------------------------------------------}
# {-------------------------------- BOLSA DE FICHAS --------------------------------}
# {---------------------------------------------------------------------------------}



def letra_random(bolsa_fichas):
    letras = list(bolsa_fichas.keys())
    string_letras=''
    for i in letras:
        string_letras=string_letras+(i*bolsa_fichas[i]['cantidad'])
    print(string_letras)
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
    for i in range(0,7):
        lis.append(sg.Button(letra_random(bolsa_fichas),key="fJ-"+str(i),pad=(0,0),size=(7,1),disabled_button_color=('#747678','#747678'),button_color=('black','white')))
        keys.append("fJ-"+str(i)) 

    return (lis,keys)

def fila_fichasM():
    lis = []
    for i in range(0,7):
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
    [sg.Column(layout_tablero)],
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
            habilitar_tablero(pantalla_juego,tamanio)
            ficha_clicked = event
        elif(event in keys_tablero):
            pantalla_juego[event].Update(pantalla_juego[ficha_clicked].GetText())
            pantalla_juego[ficha_clicked].Update(disabled=True)
            desabilitar_tablero(pantalla_juego,tamanio)
        
    pantalla_juego.close() 

if __name__ == "__main__":
    main()



















