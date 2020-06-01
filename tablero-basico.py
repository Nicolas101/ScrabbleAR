import PySimpleGUI as sg

def hacer_fila(num_fila):
    lis = []
    keys = []
    for i in range(0,15):
        lis.append(sg.Button(" ",key=str(num_fila)+"-"+str(i),pad=(0,0),size=(3,1)))
        keys.append(str(num_fila)+"-"+str(i))
        
    return (lis,keys)
        
def hacer_tablero():
    lis = []
    keys = []
    for i in range(0,15):
        valores = hacer_fila(i)
        lis.append(valores[0])   
        keys=keys+valores[1]

    return (lis,keys)

def hacer_filafichas():
    lis = []
    for i in range(0,7):
        lis.append(sg.Button("ficha",pad=(0,0)))
    return lis







valores_tablero= hacer_tablero()
keys_tablero=valores_tablero[1]

layout_tablero = valores_tablero[0]
layout_fichasMaquina = [hacer_filafichas()]
layout_fichasJugador = [hacer_filafichas()]

layout = [  
    [sg.Column(layout_fichasMaquina,pad=((0,0),(0,20)))],
    [sg.Column(layout_tablero)],
    [sg.Column(layout_fichasJugador,pad=((0,0),(20,0)))]
]
pantalla_juego = sg.Window("Scrabble",layout)



while True:
    event, values = pantalla_juego.read()
    if(event is None):
        break
    elif(event in keys_tablero): # Terminamos aca
        print("hola ma")

pantalla_juego.close() 



















