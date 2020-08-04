def hacer_ventana():
    import PySimpleGUI as sg

    layout = [
        [sg.Image(r"Data\Images\SelecNivel\titulo.png",background_color="#40B7C9",pad=((40,40),(15,20)))],
        [sg.Button(image_filename=r"Data\Images\SelecNivel\boton-nivel-facil.png",key="-FACIL-",button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((108,108),(0,5)))],
        [sg.Button(image_filename=r"Data\Images\SelecNivel\boton-nivel-medio.png",key="-MEDIO-",button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((108,108),(0,5)))],
        [sg.Button(image_filename=r"Data\Images\SelecNivel\boton-nivel-dificil.png",key="-DIFICIL-",button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((108,108),(0,0)))]
    ]

    window = sg.Window("ScrabbleAR - Selección de nivel",layout,size=(500,400),background_color="#40B7C9")

    return window
    