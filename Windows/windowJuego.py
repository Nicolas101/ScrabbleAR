def hacer_ventana(layout_tablero, layout_fichasJ, layout_fichasM, num_random, pad_tablero,window_size):
    import PySimpleGUI as sg

    barra_datos = [
        [sg.Text("DATOS DE PARTIDA",pad=((45,45),(13,12)))],
        [sg.Text("_"*112)],
        [sg.Text("TIEMPO",pad=((80,),(0,10)))],
        [sg.Button("Pausa",key="-PAUSA-",pad=((60,7),(0,0))), sg.Text("",key='-RELOJ-',size=(6,1),pad=((0,0),(0,0)))],
        [sg.Text("_"*112)],
        [sg.Text("PUNTAJE",pad=((80,55),(0,10)))],
        [sg.Text("• Maquina:",pad=((12,0),(0,0))),sg.Text("0",key="-PuntosM-",size=(5,1),pad=((0,0),(0,0)))],
        [sg.Text("• Jugador:",pad=((12,0),(0,0))),sg.Text("0",key="-PuntosJ-",size=(5,1),pad=((0,0),(0,0)))],
        [sg.Text("_"*112)],
        [sg.Text("TURNO",pad=((85,0),(0,10)))],
        [sg.Text("",key="-TURNO-",size=(25,1),pad=((85,0),(0,0)))],
        [sg.Text("_"*112)],
        [sg.Button("Confirmar Jugada",key='-CONFIRMAR-',size=(20,2),pad=((25,0),(0,3)))],
        [sg.Text('',key='text-confirmar',size=(15,1),pad=((40,0),(0,10)))],
        [sg.Button("Cambiar fichas",key="-B_CAMBIAR_PASAR-",size=(15,2),pad=((45,0),(40,10)))],
        [sg.Text("Seleccione fichas para cambiar",key='cambiar_fichas_text',pad=((20,0),(0,5)),visible=False)],
        [sg.Button("Aceptar",pad=((0,0),(0,0)),visible=False)],
        [sg.Button("Cancelar",visible=False,pad=((0,0),(0,0)))],
    ]

    columna_izq = [  
        [sg.Column(layout_fichasM,pad=((34,0),(0,0)))],
        [sg.Column(layout_tablero,pad=((pad_tablero[num_random]["pad-izq"],pad_tablero[num_random]["pad-der"]),(pad_tablero[num_random]["pad-top"],pad_tablero[num_random]["pad-bot"])))],
        [sg.Column(layout_fichasJ,pad=((34,0),(0,0)))]
    ]

    layout_juego = [
        [sg.Column(columna_izq,background_color="#71B3BD"), sg.VerticalSeparator(), sg.Column(barra_datos,size=(223,600),pad=((0,0),(0,0))), sg.VerticalSeparator()]
    ]

    return sg.Window("ScrabbleAR - En Juego",layout_juego,size=window_size,background_color="#71B3BD")
    