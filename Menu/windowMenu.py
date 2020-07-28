def hacer_ventana(window_size):
    import PySimpleGUI as sg

    layout = [
        [sg.Image(filename=r"Menu\Data\TítuloMenu.png",background_color='#40B7C9',pad=((70,70),(10,27)))],
        [sg.Button("",image_filename=r"Menu\Data\BotónComojugar.png",key="-HOWTOPLAY-",button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((305,305),(0,0)))],
        [sg.Button("",image_filename=r"Menu\Data\BotónJugar.png",key="-PLAY-",button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((250,250),(0,10)))],
        [sg.Button("",image_filename=r"Menu\Data\BotónConfiguración.png",key="-CONFIG-",button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((305,305),(0,0)))],
        [sg.Button("",image_filename=r"Menu\Data\BotónTop10.png",key="-TOP10-",button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((15,300),(0,0))),
        sg.Button("",image_filename=r"Menu\Data\BotónSalir.png",key="-SALIR-",button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((300,15),(0,0)))]
    ]
    window = sg.Window("ScrabbleAR - Menú",layout,size=window_size,background_color='#40B7C9')

    return window