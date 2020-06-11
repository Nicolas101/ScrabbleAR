import PySimpleGUI as sg

# {---------------------------------------------------------------------------------}
# {----------------------------------- TABLERO -------------------------------------}
# {---------------------------------------------------------------------------------}

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

def hacer_tablero(casillas_especiales):
    def hacer_fila(num_fila,casillas_especiales):
        lis = []
        keys = []
        for i in range(0,15):
            nom=str(num_fila)+"-"+str(i)
            if (nom in casillas_especiales["+2"]):
                lis.append(sg.Button("+2",key=nom,pad=(0,0),size=(3,1),disabled=True,button_color=('black','#2283BB'),disabled_button_color=('black','#2283BB')))
            elif (nom in casillas_especiales["+3"]):
                lis.append(sg.Button("+3",key=nom,pad=(0,0),size=(3,1),disabled=True,button_color=('black','#45BB22'),disabled_button_color=('black','#45BB22')))
            elif(nom in casillas_especiales["-1"]):
                lis.append(sg.Button("-1",key=nom,pad=(0,0),size=(3,1),disabled=True,button_color=('black','#F0B121'),disabled_button_color=('black','#F0B121')))
            elif(nom in casillas_especiales["-2"]):
                lis.append(sg.Button("-2",key=nom,pad=(0,0),size=(3,1),disabled=True,button_color=('black','#F06C21'),disabled_button_color=('black','#F06C21')))
            elif(nom in casillas_especiales["-3"]):
                lis.append(sg.Button("-3",key=nom,pad=(0,0),size=(3,1),disabled=True,button_color=('black','#F02121'),disabled_button_color=('black','#F02121')))
            else:            
                lis.append(sg.Button(" ",key=str(num_fila)+"-"+str(i),pad=(0,0),size=(3,1),disabled=True,disabled_button_color=('black','white'),button_color=('black','white')))
            keys.append(str(num_fila)+"-"+str(i))
        
        return (lis,keys) 

    lis = []
    keys = []
    for i in range(0,15):
        valores = hacer_fila(i,casillas_especiales)
        lis.append(valores[0])   
        keys = keys + valores[1]

    return (lis,keys)


casillas_especiales={"+2":["1-5","1-9","5-1","5-13","6-6","6-8","8-6","8-8","9-1","9-13","13-5","13-9"],
                    "+3":["0-3","0-11","2-6","2-8","3-0","3-7","3-14","6-2","6-12","7-3","7-11","8-2","8-12","11-0","11-14","11-7","12-6","12-8","14-3"],
                    "-3":["0-0","0-7","0-14","7-0","7-14","14-0","14-7","14-14"],
                    "-2":["1-1","1-13","2-2","2-12","12-2","12-12","13-1","13-13"],
                    "-1":["3-3","3-11","4-4","4-10","5-5","5-9","9-5","9-9","10-4","10-10","11-3","11-11"]}

valores_tablero = hacer_tablero(casillas_especiales)  
keys_tablero = valores_tablero[1]   # Lista de keys de cada boton del tablero
layout_tablero = valores_tablero[0]   


# {---------------------------------------------------------------------------------}
# {------------------------------ FILA DE FICHAS -----------------------------------}
# {---------------------------------------------------------------------------------}

def fila_fichasJ():
    lis = []
    keys = []
    for i in range(0,7):
        lis.append(sg.Button(str(i),key="fJ-"+str(i),pad=(0,0),size=(7,1),disabled_button_color=('#747678','#747678'),button_color=('black','white')))
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

pantalla_juego = sg.Window("Scrabble",layout,background_color="#71B3BD",size=(725,480))


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
            habilitar_tablero(pantalla_juego)
            ficha_clicked = event
        elif(event in keys_tablero):
            pantalla_juego[event].Update(pantalla_juego[ficha_clicked].GetText())
            pantalla_juego[ficha_clicked].Update(disabled=True)
            desabilitar_tablero(pantalla_juego)
        
    pantalla_juego.close() 

if __name__ == "__main__":
    main()



















