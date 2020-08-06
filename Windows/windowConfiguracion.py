def hacer_ventana(window_size,f_text,m_text,d_text):
    import PySimpleGUI as sg 
    
    nivel_facil = [
        [sg.Text("FÁCIL",background_color="#71B3BD",font=("Courier",26),pad=((0,0),(0,20)))],
        [sg.Button("Tiempo",key='-TIEMPO_F-',tooltip="Limite de tiempo máximo de juego en este nivel.  \nHaga click para modificar",size=(10,2),pad=((0,0),(0,10)))],
        [sg.Button("Puntaje",key='-PUNTOS_F-',tooltip="Puntaje por letra en este nivel.  \nHaga click para modificar",size=(10,2),pad=((0,0),(0,10)))],
        [sg.Button("Fichas",key='-FICHAS_F-',tooltip="Cantidad de fichas por letra en este nivel.  \nHaga click para modificar",size=(10,2),pad=((0,0),(0,10)))],
        [sg.Text(f_text,key='text_facil',background_color="#71B3BD",text_color="#767676",size=(15,1))]
    ]

    nivel_medio = [
        [sg.Text("MEDIO",background_color="#71B3BD",font=("Courier",26),pad=((0,0),(0,20)))],
        [sg.Button("Tiempo",key='-TIEMPO_M-',tooltip="Limite de tiempo máximo de juego en este nivel.  \nHaga click para modificar",size=(10,2),pad=((0,0),(0,10)))],
        [sg.Button("Puntaje",key='-PUNTOS_M-',tooltip="Puntaje por letra en este nivel.  \nHaga click para modificar",size=(10,2),pad=((0,0),(0,10)))],
        [sg.Button("Fichas",key='-FICHAS_M-',tooltip="Cantidad de fichas por letra en este nivel.  \nHaga click para modificar",size=(10,2),pad=((0,0),(0,10)))],
        [sg.Text(m_text,key='text_medio',background_color="#71B3BD",text_color="#767676",size=(15,1))]
    ]

    nivel_dificil = [
        [sg.Text("DIFÍCIL",background_color="#71B3BD",font=("Courier",26),pad=((0,0),(0,20)))],
        [sg.Button("Tiempo",key='-TIEMPO_D-',tooltip="Limite de tiempo máximo de juego en este nivel.  \nHaga click para modificar",size=(10,2),pad=((0,0),(0,10)))],
        [sg.Button("Puntaje",key='-PUNTOS_D-',tooltip="Puntaje por letra en este nivel.  \nHaga click para modificar",size=(10,2),pad=((0,0),(0,10)))],
        [sg.Button("Fichas",key='-FICHAS_D-',tooltip="Cantidad de fichas por letra en este nivel.  \nHaga click para modificar",size=(10,2),pad=((0,0),(0,10)))],
        [sg.Text(d_text,key='text_dificil',background_color="#71B3BD",text_color="#767676",size=(15,1))]
    ]

    layout = [
        [sg.Text("Configuración del juego",background_color="#71B3BD",font=("Fixedsys",40),pad=((0,0),(30,0)))],
        [sg.Text('_'*80,background_color="#71B3BD", pad=((0,0),(0,50)))],
        [sg.Column(nivel_facil,background_color="#71B3BD",element_justification="center",pad=((150,0),(0,0))),sg.VerticalSeparator(pad=(20,0)),sg.Column(nivel_medio,background_color="#71B3BD",element_justification="center",pad=(0,0)),sg.VerticalSeparator(pad=(20,0)),sg.Column(nivel_dificil,background_color="#71B3BD",element_justification="center",pad=(0,0))],
        [sg.Button("Nivel personalizado",tooltip="  ¡Crea tu propio nivel con tus propias caracteristicas!  ",size=(18,2),font=("Arial",16),pad=((0,0),(40,13)))],
        [sg.Button("Guardar",key='-GUARDAR-',size=(18,2),pad=((800,0),(0,0)))],
        [sg.Button("Volver",key="-BACK-",size=(18,2),pad=((0,650),(0,0))),sg.Button("Restaurar valores",key='-RESTAURAR_VALORES-',size=(18,2),pad=((0,0),(5,0)))]
        ]

    return sg.Window('ScrabbleAR - Configuración',layout,size=window_size,background_color="#71B3BD",element_justification="center")