def hacer_ventana():
    import PySimpleGUI as sg
    layout = [
        [sg.Image(r"Data\Images\Juego\Ventana-salir\titulo.png",background_color="#40B7C9",pad=(0,10))],
        [sg.Button(image_filename=r"Data\Images\Juego\Ventana-salir\boton-guardar-y-salir.png",key="-GUARDAR_Y_SALIR2-",button_color=("#40B7C9","#40B7C9"),border_width=0,pad=(70,5))],
        [sg.Button(image_filename=r"Data\Images\Juego\Ventana-salir\boton-salir-sin-guardar.png",key="-SALIR_SIN_GUARDAR2-",button_color=("#40B7C9","#40B7C9"),border_width=0,pad=(70,5))]
    ]
    window = sg.Window("ScrabbleAR - Salir",layout,size=(300,200),background_color="#40B7C9",disable_close=True)
    
    return window