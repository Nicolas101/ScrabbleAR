def hacer_ventana(window_size):
    import PySimpleGUI as sg

    layout = [
        [sg.Text("ScrabbleAR - Game",background_color="#71B3BD",font=("Fixedsys",40),pad=((0,0),(100,0)))],
        [sg.Text('_'*60,background_color="#71B3BD", pad=((0,0),(0,68)))],
        [sg.Button("Cómo jugar",size=(18,1),pad=((0,0),(0,20)),font=("Fixedsys",18),auto_size_button=False)],
        [sg.Button("Jugar",key="-PLAY-",size=(24,2),pad=((0,0),(0,20)),font=("Fixedsys",18),auto_size_button=False)],
        [sg.Button("Configuración",key="-CONFIG-",size=(18,1),pad=((0,0),(0,20)),font=("Fixedsys",18),auto_size_button=False)],
        [sg.Button("TOP 10",size=(18,2),pad=((0,325),(40,0))),sg.Button("SALIR",key="-SALIR-",size=(18,2),pad=((325,0),(40,0)))]
    ]

    return sg.Window("ScrabbleAR - Menú",layout,element_justification="center",size=window_size,background_color="#71B3BD")