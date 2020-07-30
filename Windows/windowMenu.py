def hacer_ventana(window_size):
    import PySimpleGUI as sg

    layout = [
        [sg.Image(filename=r"Data\Images\Menu\ScrabbleAR.png",background_color='#40B7C9',pad=((120,120),(50,55)))],
        [sg.Button("",image_filename=r"Data\Images\Menu\Boton-como-jugar.png",key="-HOWTOPLAY-",button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((305,305),(0,0)))],
        [sg.Button("",image_filename=r"Data\Images\Menu\Boton-jugar.png",key="-PLAY-",button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((260,260),(15,15)))],
        [sg.Button("",image_filename=r"Data\Images\Menu\Boton-configuracion.png",key="-CONFIG-",button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((305,305),(0,20)))],
        [sg.Button("",image_filename=r"Data\Images\Menu\Boton-top10.png",key="-TOP10-",button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((15,300),(0,0))),
        sg.Button("",image_filename=r"Data\Images\Menu\Boton-salir.png",key="-SALIR-",button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((300,15),(0,0)))]
    ]

    window = sg.Window("ScrabbleAR - Menú",layout,size=window_size,background_color='#40B7C9')

    return window


if __name__ == "__main__":
    window = hacer_ventana((1000,600))

    while True:
        event, values = window.read()
        if event is None:
            break

    window.close()