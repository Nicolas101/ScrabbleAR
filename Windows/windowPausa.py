def hacer_ventana():
    """Devuelve la ventana de pausa
    """
    import PySimpleGUI as sg

    import os
    if os.access(r'Data\Images\Juego\Avatar-CPU.png',0):
        layout = [
            [sg.Image(r"Data\Images\Pausa\titulo.png",background_color="#40B7C9",pad=((100,100),(15,20)))],
            [sg.Button(image_filename=r"Data\Images\Pausa\boton-terminar.png",key="-TERMINAR_PARTIDA-",button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((125,125),(0,0)))],
            [sg.Button(image_filename=r"Data\Images\Pausa\boton-reanudar.png",key="-REANUDAR-",button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((93,93),(5,5)))],
            [sg.Button(image_filename=r"Data\Images\Pausa\boton-guardar-y-salir.png",key="-GUARDAR_Y_SALIR-",button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((170,170),(0,5)))],
            [sg.Button(image_filename=r"Data\Images\Pausa\boton-salir-sin-guardar.png",key="-SALIR_SIN_GUARDAR-",button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((170,170),(0,0)))],
        ]
    else:
        layout = [
            [sg.Image(r"Data/Images/Pausa/titulo.png",background_color="#40B7C9",pad=((100,100),(15,20)))],
            [sg.Button(image_filename=r"Data/Images/Pausa/boton-terminar.png",key="-TERMINAR_PARTIDA-",button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((125,125),(0,0)))],
            [sg.Button(image_filename=r"Data/Images/Pausa/boton-reanudar.png",key="-REANUDAR-",button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((93,93),(5,5)))],
            [sg.Button(image_filename=r"Data/Images/Pausa/boton-guardar-y-salir.png",key="-GUARDAR_Y_SALIR-",button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((170,170),(0,5)))],
            [sg.Button(image_filename=r"Data/Images/Pausa/boton-salir-sin-guardar.png",key="-SALIR_SIN_GUARDAR-",button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((170,170),(0,0)))],
        ]

    window = sg.Window("ScrabbleAR - Pausa",size=(500,400),background_color="#40B7C9",disable_close=True,margins=(0,0)).Layout(layout)

    return window
