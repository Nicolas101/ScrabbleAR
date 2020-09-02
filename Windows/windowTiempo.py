def hacer_ventanta(valor_por_defecto,lis_values):
    """Devuelve la ventana de 'Selecconar el tiempo que dura la partida'
    """
    import PySimpleGUI as sg

    import os
    if os.access(r'Data\Images\Juego\Avatar-CPU.png',0):
        layout = [
            [sg.Image(r"Data\Images\Configuracion\Tiempo\titulo.png",background_color='#40B7C9',pad=((115,0),(10,10)))],
            [sg.Image(r"Data\Images\Configuracion\Tiempo\texto.png",background_color='#40B7C9',pad=((30,0),(0,10)))],
            [sg.Listbox(lis_values,default_values=[valor_por_defecto], key='Listbox',size=(40,9),pad=((90,0),(0,0)))],
            [sg.Button(image_filename=r"Data\Images\Configuracion\Letras\boton-confirmar.png",key="-CONFIRMAR-",button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((80,0),(20,0))),sg.Button(image_filename=r"Data\Images\Configuracion\Letras\boton-cancelar.png",key="-CANCELAR-",button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((10,0),(20,0)))]
        ]
    else:
        layout = [
            [sg.Image(r"Data/Images/Configuracion/Tiempo/titulo.png",background_color='#40B7C9',pad=((115,0),(10,10)))],
            [sg.Image(r"Data/Images/Configuracion/Tiempo/texto.png",background_color='#40B7C9',pad=((30,0),(0,10)))],
            [sg.Listbox(lis_values,default_values=[valor_por_defecto], key='Listbox',size=(40,9),pad=((90,0),(0,0)))],
            [sg.Button(image_filename=r"Data/Images/Configuracion/Letras/boton-confirmar.png",key="-CONFIRMAR-",button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((80,0),(20,0))),sg.Button(image_filename=r"Data/Images/Configuracion/Letras/boton-cancelar.png",key="-CANCELAR-",button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((10,0),(20,0)))]
        ]

    window = sg.Window("ScrabbleAR - Tiempo",size=(500,400),background_color='#40B7C9').Layout(layout)

    return window
