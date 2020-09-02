def hacer_ventana(letras_maquina, letras_usuario,text_game_over):
    """Devuelve una ventana que muestra las letras que quedaron en los atriles al finalizar la partida
    y da la opcion de calcular el puntaje final
    """
    import PySimpleGUI as sg

    def hacer_fichas(letras, so):
        fichas = []
        if so == 'w':
            for letra in letras:
                fichas.append(sg.Image(r"Data\Images\Juego\Fichas\letra-"+letra+".png",background_color="#40B7C9",pad=(0,0)))
        else:
            for letra in letras:
                fichas.append(sg.Image(r"Data/Images/Juego/Fichas/letra-"+letra+".png",background_color="#40B7C9",pad=(0,0)))
        return [fichas]

    import os
    if os.access(r'Data\Images\Juego\Avatar-CPU.png',0):
        cpu = [
            [sg.Image(r"Data\Images\Juego\Partida-terminada\cpu-text.png",background_color="#40B7C9",pad=(0,0)),
            sg.Column(hacer_fichas(letras_maquina,'w'),background_color="#40B7C9")]
        ]

        usuario = [
            [sg.Image(r"Data\Images\Juego\Partida-terminada\tu-text.png",background_color="#40B7C9",pad=((10,10),(0,0))),
            sg.Column(hacer_fichas(letras_usuario,'w'),background_color="#40B7C9")]
        ]

        fichas = [
            [sg.Column(cpu,background_color="#40B7C9")],
            [sg.Column(usuario,background_color="#40B7C9")],
        ]

        layout = [
            [sg.Image(r"Data\Images\Juego\Partida-terminada\titulo.png",background_color="#40B7C9",pad=((5,5),(10,0)))],
            [sg.Text(text_game_over,font=("Arial black",12),text_color="black",background_color="#40B7C9",pad=((80,0),(0,0)))],
            [sg.Image(r"Data\Images\Juego\Partida-terminada\fichas-a-descontar.png",background_color="#40B7C9",pad=((120,0),(30,0)))],
            [sg.Column(fichas,background_color="#40B7C9")],
            [sg.Button(image_filename=r"Data\Images\Juego\Partida-terminada\boton-calcular-puntaje.png",button_color=("#40B7C9","#40B7C9"),border_width=0,pad=((150,0),(10,0)))]
        ]

    else:
        cpu = [
            [sg.Image(r"Data/Images/Juego/Partida-terminada/cpu-text.png",background_color="#40B7C9",pad=(0,0)),
            sg.Column(hacer_fichas(letras_maquina,'l'),background_color="#40B7C9")]
        ]

        usuario = [
            [sg.Image(r"Data/Images/Juego/Partida-terminada/tu-text.png",background_color="#40B7C9",pad=((10,10),(0,0))),
            sg.Column(hacer_fichas(letras_usuario,'l'),background_color="#40B7C9")]
        ]

        fichas = [
            [sg.Column(cpu,background_color="#40B7C9")],
            [sg.Column(usuario,background_color="#40B7C9")],
        ]

        layout = [
            [sg.Image(r"Data/Images/Juego/Partida-terminada/titulo.png",background_color="#40B7C9",pad=((5,5),(10,0)))],
            [sg.Text(text_game_over,font=("Arial black",12),text_color="black",background_color="#40B7C9",pad=((80,0),(0,0)))],
            [sg.Image(r"Data/Images/Juego/Partida-terminada/fichas-a-descontar.png",background_color="#40B7C9",pad=((120,0),(30,0)))],
            [sg.Column(fichas,background_color="#40B7C9")],
            [sg.Button(image_filename=r"Data/Images/Juego/Partida-terminada/boton-calcular-puntaje.png",button_color=("#40B7C9","#40B7C9"),border_width=0,pad=((150,0),(10,0)))]
        ]


    window = sg.Window("ScrabbleAR - Partida terminada",size=(500,400),background_color="#40B7C9",disable_close=True,margins=(0,0)).Layout(layout)

    return window
