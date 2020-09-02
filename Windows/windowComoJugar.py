def hacer_ventana():
    """Devuelve la ventana de 'Como Jugar'
    """
    import PySimpleGUI as sg
    import os
    if os.access(r'Data\Images\Juego\Avatar-CPU.png',0):
        #####Windows#####
        texto_der = [
            [sg.Image(r"Data\Images\ComoJugar\texto4.png",background_color='#40B7C9',pad=((0,0),(0,30)))],
            [sg.Image(r"Data\Images\ComoJugar\texto5.png",background_color='#40B7C9',pad=((30,0),(0,0)))],
            [sg.Button(image_filename=r"Data\Images\TopDiez\boton-menu.png",button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((300,0),(35,0)))]
        ]

        texto_izq = [
            [sg.Image(r"Data\Images\ComoJugar\texto2.png",background_color='#40B7C9',pad=((0,0),(0,25)))],
            [sg.Image(r"Data\Images\ComoJugar\texto3.png",background_color='#40B7C9',pad=((0,0),(0,0)))]
        ]

        texto2 = [
            [sg.Column(texto_izq,background_color='#40B7C9',pad=((20,20),(0,0))),sg.Column(texto_der,background_color='#40B7C9')]
        ]

        layout = [
            [sg.Image(r"Data\Images\ComoJugar\titulo.png",background_color='#40B7C9',pad=((150,0),(10,15)))],
            [sg.Image(r"Data\Images\ComoJugar\texto1.png",background_color='#40B7C9',pad=((50,0),(0,0)))],
            [sg.Column(texto2,background_color='#40B7C9',pad=((0,0),(15,0)))],
        ]

    else:

        #####Linux#####
        texto_der = [
            [sg.Image(r"Data/Images/ComoJugar/texto4.png",background_color='#40B7C9',pad=((0,0),(0,30)))],
            [sg.Image(r"Data/Images/ComoJugar/texto5.png",background_color='#40B7C9',pad=((30,0),(0,0)))],
            [sg.Button(image_filename=r"Data/Images/TopDiez/boton-menu.png",button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((300,0),(35,0)))]
        ]

        texto_izq = [
            [sg.Image(r"Data/Images/ComoJugar/texto2.png",background_color='#40B7C9',pad=((0,0),(0,25)))],
            [sg.Image(r"Data/Images/ComoJugar/texto3.png",background_color='#40B7C9',pad=((0,0),(0,0)))]
        ]

        texto2 = [
            [sg.Column(texto_izq,background_color='#40B7C9',pad=((20,20),(0,0))),sg.Column(texto_der,background_color='#40B7C9')]
        ]

        layout = [
            [sg.Image(r"Data/Images/ComoJugar/titulo.png",background_color='#40B7C9',pad=((150,0),(10,15)))],
            [sg.Image(r"Data/Images/ComoJugar/texto1.png",background_color='#40B7C9',pad=((50,0),(0,0)))],
            [sg.Column(texto2,background_color='#40B7C9',pad=((0,0),(15,0)))],
        ]

    window = sg.Window("ScrabbleAR - Cómo jugar",size=(1000,600),background_color='#40B7C9',margins=(0,0)).Layout(layout)

    return window
