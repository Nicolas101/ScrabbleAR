import PySimpleGUI as sg

def crearLayout(tablero, fila_fichasJ, fila_fichasM, num_random, pad_tablero,window_size):
    
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


    columna_izq = [  
        [sg.Column(fila_fichasM.getLayout(),pad=((34,0),(0,0)))],
        [sg.Column(tablero.getLayout(),pad=((pad_tablero[num_random]["pad-izq"],pad_tablero[num_random]["pad-der"]),(pad_tablero[num_random]["pad-top"],pad_tablero[num_random]["pad-bot"])))],
        [sg.Column(fila_fichasJ.getLayout(),pad=((34,0),(0,0)))]
    ]

    layout_juego = [
        [sg.Column(columna_izq,background_color="#71B3BD"), sg.VerticalSeparator(), sg.Column(barra_datos,size=(223,600),pad=((0,0),(0,0))), sg.VerticalSeparator()]
    ]

    pantalla_juego = sg.Window("ScrabbleAR - En Juego",layout_juego,size=window_size,background_color="#71B3BD")
    return pantalla_juego