def hacer_ventana():
    """Devuelve la ventala del menú principal
    """
    import PySimpleGUI as sg

    layout = [
        [sg.Image(filename=r"Data\Images\Menu\Titulo.png",background_color='#40B7C9',pad=((120,120),(10,25)))],
        [sg.Button("",image_filename=r"Data\Images\Menu\Boton-como-jugar.png",key="-COMO_JUGAR-",button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((295,315),(0,0)))],
        [sg.Button("",image_filename=r"Data\Images\Menu\Boton-jugar.png",key="-JUGAR-",button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((250,270),(15,15)))],
        [sg.Button("",image_filename=r"Data\Images\Menu\Boton-configuracion.png",key="-CONFIGURACION-",button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((295,315),(0,20)))],
        [sg.Button("",image_filename=r"Data\Images\Menu\Boton-top10.png",key="-TOP10-",button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((15,300),(0,0))),
        sg.Button("",image_filename=r"Data\Images\Menu\Boton-salir.png",key="-SALIR-",button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((300,15),(0,0)))]
    ]

    window = sg.Window("ScrabbleAR - Menú",layout,size=(1000,600),background_color='#40B7C9')

    return window


