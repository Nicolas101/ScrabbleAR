def hacer_ventana():
    """Devuelve la ventana de 'Hay una partida guardada'
    """
    import PySimpleGUI as sg

    import os
    if os.access(r'Data\Images\Juego\Avatar-CPU.png',0):
        layout = [
            [sg.Image(r"Data\Images\Menu\Partida-guardada\titulo.png",background_color="#40B7C9",pad=((60,0),(20,0)))],
            [sg.Image(r"Data\Images\Menu\Partida-guardada\texto.png",background_color="#40B7C9",pad=((56,0),(30,90)))],
            [sg.Button(image_filename=r"Data\Images\Menu\Partida-guardada\boton-si.png",key="-SI-",button_color=("#40B7C9","#40B7C9"),border_width=0,pad=((95,0),(0,0))), sg.Button(image_filename=r"Data\Images\Menu\Partida-guardada\boton-no.png",key="-NO-",button_color=("#40B7C9","#40B7C9"),border_width=0)]
        ]
    else:
        layout = [
            [sg.Image(r"Data/Images/Menu/Partida-guardada/titulo.png",background_color="#40B7C9",pad=((60,0),(20,0)))],
            [sg.Image(r"Data/Images/Menu/Partida-guardada/texto.png",background_color="#40B7C9",pad=((56,0),(30,90)))],
            [sg.Button(image_filename=r"Data/Images/Menu/Partida-guardada/boton-si.png",key="-SI-",button_color=("#40B7C9","#40B7C9"),border_width=0,pad=((95,0),(0,0))), sg.Button(image_filename=r"Data/Images/Menu/Partida-guardada/boton-no.png",key="-NO-",button_color=("#40B7C9","#40B7C9"),border_width=0)]
        ]

    return sg.Window('ScrabbleAR - Partida guardada',size=(500,400),background_color="#40B7C9",disable_close=True,margins=(0,0)).Layout(layout)
