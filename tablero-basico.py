import PySimpleGUI as sg

# TABLERO 
def habilitar_tablero(pantalla_juego):
    for i in range(0,15):
        for j in range(0,15):
            key = str(i)+"-"+str(j)
            pantalla_juego[key].Update(disabled=False)

def desabilitar_tablero(pantalla_juego):
    for i in range(0,15):
        for j in range(0,15):
            key = str(i)+"-"+str(j)
            pantalla_juego[key].Update(disabled=True)   

def hacer_tablero():
    def hacer_fila(num_fila):
        lis = []
        keys = []
        for i in range(0,15):
            lis.append(sg.Button(" ",key=str(num_fila)+"-"+str(i),pad=(0,0),size=(3,1),disabled=True,disabled_button_color=('white','blue')))
            keys.append(str(num_fila)+"-"+str(i))
        
        return (lis,keys) 

    lis = []
    keys = []
    for i in range(0,15):
        valores = hacer_fila(i)
        lis.append(valores[0])   
        keys = keys + valores[1]

    return (lis,keys)

valores_tablero = hacer_tablero()  
keys_tablero = valores_tablero[1]   # Lista de keys de cada boton del tablero
layout_tablero = valores_tablero[0]   


# FILA DE FICHAS
def fila_fichasJ():
    lis = []
    keys = []
    for i in range(0,7):
        lis.append(sg.Button(str(i),key="fJ-"+str(i),pad=(0,0),size=(7,1)))
        keys.append("fJ-"+str(i)) 

    return (lis,keys)

def fila_fichasM():
    lis = []
    for i in range(0,7):
        lis.append(sg.Button(" ",key="fM-"+str(i),pad=(0,0),size=(7,1)))

    return lis

layout_fichasMaquina = [fila_fichasM()]

valores_fichasJugador = fila_fichasJ()
keys_fichasJ = valores_fichasJugador[1]
layout_fichasJugador = [valores_fichasJugador[0]]   

# BARRA DE DATOS
layout_barraDate = [
    [sg.Text("DATOS DE PARTIDA")],
    [sg.Text("Tiempo:"),sg.Text("(tiempo correspondiente)")],
    [sg.Button("Pausa")],
    [sg.Text("Maquina:"),sg.Text("(Puntos de la maquina)")],
    [sg.Text("Tus puntos:"),sg.Text("(puntos del jugador)")],
    [sg.Text("Turno:"),sg.Text("(turno correspondiente)")],
    [sg.Button("Confirmar Jugada")],
    [sg.Button(image_filename="bolsa_fichas.jpg")],
    [sg.Button("Cambiar fichas")],
    [sg.Text("Seleccione las fichas que desea cambiar",visible=False)],
    [sg.Button("Aceptar",visible=False)]
]


# PANTALLA DE JUEGO
layout_game = [  
    [sg.Column(layout_fichasMaquina,pad=((0,0),(0,20)))],
    [sg.Column(layout_tablero)],
    [sg.Column(layout_fichasJugador,pad=((0,0),(20,0)))]
]

layout = [
    [sg.Column(layout_game), sg.Column(layout_barraDate,element_justification="center")]
]

pantalla_juego = sg.Window("Scrabble",layout)

while True:
    event, values = pantalla_juego.read()
    if(event is None):
        break
    elif(event in keys_fichasJ):
        habilitar_tablero(pantalla_juego)
        ficha_clicked = event
    elif(event in keys_tablero):
        pantalla_juego[event].Update(pantalla_juego[ficha_clicked].GetText())
        pantalla_juego[ficha_clicked].Update(disabled=True)
        desabilitar_tablero(pantalla_juego)
        

pantalla_juego.close() 



















