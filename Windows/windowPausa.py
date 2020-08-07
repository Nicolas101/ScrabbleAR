def hacer_ventana():
    """Devuelve la ventana de pausa
    """
    import PySimpleGUI as sg

    layout = [
        [sg.Image(r"Data\Images\Pausa\titulo.png",background_color="#40B7C9",pad=((100,100),(15,20)))],
        [sg.Button(image_filename=r"Data\Images\Pausa\boton-terminar.png",key="-TERMINAR_PARTIDA-",button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((125,125),(0,0)))],
        [sg.Button(image_filename=r"Data\Images\Pausa\boton-reanudar.png",key="-REANUDAR-",button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((93,93),(5,5)))],
        [sg.Button(image_filename=r"Data\Images\Pausa\boton-guardar-y-salir.png",key="-GUARDAR_Y_SALIR-",button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((170,170),(0,5)))],
        [sg.Button(image_filename=r"Data\Images\Pausa\boton-salir-sin-guardar.png",key="-SALIR_SIN_GUARDAR-",button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((170,170),(0,0)))],
    ]
    window = sg.Window("ScrabbleAR - Pausa",layout,size=(500,400),background_color="#40B7C9",disable_close=True)

    return window


if __name__ == "__main__":
    window = hacer_ventana()
    while True:
        event, values = window.read()
        if event == "-SALIR_SIN_GUARDAR-":
            break

    window.close()