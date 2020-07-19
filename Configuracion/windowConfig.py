def hacer_ventana(window_size):
    import PySimpleGUI as sg 
    
    nivel_facil = [
        [sg.Text("FÁCIL",background_color="#71B3BD",font=("Courier",26),pad=((0,0),(0,20)))],
        [sg.Button("Tiempo",tooltip="Limite de tiempo máximo de juego en este nivel.  \nHaga click para modificar",size=(10,2),pad=((0,0),(0,10))),sg.Text("*Predeterminado*",background_color="#71B3BD",text_color="#767676")],
        [sg.Button("Puntaje",tooltip="Puntaje por letra en este nivel.  \nHaga click para modificar",size=(10,2),pad=((0,0),(0,10))),sg.Text("*Predeterminado*",background_color="#71B3BD",text_color="#767676")],
        [sg.Button("Fichas",tooltip="Cantidad de fichas por letra en este nivel.  \nHaga click para modificar",size=(10,2),pad=((0,0),(0,10))),sg.Text("*Predeterminado*",background_color="#71B3BD",text_color="#767676")]
    ]

    nivel_medio = [
        [sg.Text("MEDIO",background_color="#71B3BD",font=("Courier",26),pad=((0,0),(0,20)))],
        [sg.Button("Tiempo",tooltip="Limite de tiempo máximo de juego en este nivel.  \nHaga click para modificar",size=(10,2),pad=((0,0),(0,10))),sg.Text("*Predeterminado*",background_color="#71B3BD",text_color="#767676")],
        [sg.Button("Puntaje",tooltip="Puntaje por letra en este nivel.  \nHaga click para modificar",size=(10,2),pad=((0,0),(0,10))),sg.Text("*Predeterminado*",background_color="#71B3BD",text_color="#767676")],
        [sg.Button("Fichas",tooltip="Cantidad de fichas por letra en este nivel.  \nHaga click para modificar",size=(10,2),pad=((0,0),(0,10))),sg.Text("*Predeterminado*",background_color="#71B3BD",text_color="#767676")]
    ]

    nivel_dificil = [
        [sg.Text("DIFÍCIL",background_color="#71B3BD",font=("Courier",26),pad=((0,0),(0,20)))],
        [sg.Button("Tiempo",tooltip="Limite de tiempo máximo de juego en este nivel.  \nHaga click para modificar",size=(10,2),pad=((0,0),(0,10))),sg.Text("*Predeterminado*",background_color="#71B3BD",text_color="#767676")],
        [sg.Button("Puntaje",tooltip="Puntaje por letra en este nivel.  \nHaga click para modificar",size=(10,2),pad=((0,0),(0,10))),sg.Text("*Predeterminado*",background_color="#71B3BD",text_color="#767676")],
        [sg.Button("Fichas",tooltip="Cantidad de fichas por letra en este nivel.  \nHaga click para modificar",size=(10,2),pad=((0,0),(0,10))),sg.Text("*Predeterminado*",background_color="#71B3BD",text_color="#767676")]
    ]

    layout = [
        [sg.Text("Configuración del juego",background_color="#71B3BD",font=("Fixedsys",40),pad=((0,0),(30,0)))],
        [sg.Text('_'*80,background_color="#71B3BD", pad=((0,0),(0,50)))],
        [sg.Column(nivel_facil,background_color="#71B3BD",element_justification="center",pad=((150,0),(0,0))),sg.VerticalSeparator(pad=(20,0)),sg.Column(nivel_medio,background_color="#71B3BD",element_justification="center",pad=(0,0)),sg.VerticalSeparator(pad=(20,0)),sg.Column(nivel_dificil,background_color="#71B3BD",element_justification="center",pad=(0,0))],
        [sg.Button("Nivel personalizado",tooltip="  ¡Crea tu propio nivel con tus propias caracteristicas!  ",size=(18,2),font=("Arial",16),pad=((0,0),(40,13)))],
        [sg.Button("Guardar",size=(18,2),pad=((800,0),(0,0)))],
        [sg.Button("Volver",key="-BACK-",size=(18,2),pad=((0,650),(0,0))),sg.Button("Restaurar valores",size=(18,2),pad=((0,0),(5,0)))]
        ]

    return sg.Window('ScrabbleAR - Configuración',layout,size=window_size,background_color="#71B3BD",element_justification="center")