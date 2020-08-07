def hacer_ventana(text_f, text_m, text_d):
    """Devuelve la ventana de configuración
    """
    import PySimpleGUI as sg 
    
    facil = [
        [sg.Image(r"Data\Images\Configuracion\titulo-facil.png",background_color='#40B7C9',pad=((40,0),(0,0)))],
        [sg.Text(text_f,key="text_facil",size=(17,1),font=("Arial black",12),background_color='#40B7C9',text_color="#767676",justification="center",pad=((10,0),(0,20)))],
        [sg.Button(image_filename=r"Data\Images\configuracion\boton-tiempo.png",key="-TIEMPO_F-",tooltip="Limite de tiempo máximo de juego en este nivel.  \nHaga click para modificar",button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((0,0),(0,0)))],
        [sg.Button(image_filename=r"Data\Images\configuracion\boton-puntaje.png",key="-PUNTOS_F-",tooltip="Puntaje por letra en este nivel.  \nHaga click para modificar",button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((0,0),(5,5)))],
        [sg.Button(image_filename=r"Data\Images\configuracion\boton-fichas.png",key="-FICHAS_F-",tooltip="Cantidad de fichas por letra en este nivel.  \nHaga click para modificar",button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((0,0),(0,0)))],
    ]

    medio = [
        [sg.Image(r"Data\Images\Configuracion\titulo-medio.png",background_color='#40B7C9',pad=((27,0),(0,0)))],
        [sg.Text(text_m,key="text_medio",size=(17,1),font=("Arial black",12),background_color='#40B7C9',text_color="#767676",justification="center",pad=((10,0),(0,20)))],
        [sg.Button(image_filename=r"Data\Images\configuracion\boton-tiempo.png",key="-TIEMPO_M-",tooltip="Limite de tiempo máximo de juego en este nivel.  \nHaga click para modificar",button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((0,0),(0,0)))],
        [sg.Button(image_filename=r"Data\Images\configuracion\boton-puntaje.png",key="-PUNTOS_M-",tooltip="Puntaje por letra en este nivel.  \nHaga click para modificar",button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((0,0),(5,5)))],
        [sg.Button(image_filename=r"Data\Images\configuracion\boton-fichas.png",key="-FICHAS_M-",tooltip="Cantidad de fichas por letra en este nivel.  \nHaga click para modificar",button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((0,0),(0,0)))],
    ]

    dificil = [
        [sg.Image(r"Data\Images\Configuracion\titulo-dificil.png",background_color='#40B7C9',pad=((22,0),(0,0)))],
        [sg.Text(text_d,key='text_dificil',size=(17,1),font=("Arial black",12),background_color='#40B7C9',text_color="#767676",justification="center",pad=((10,0),(0,20)))],
        [sg.Button(image_filename=r"Data\Images\configuracion\boton-tiempo.png",key="-TIEMPO_D-",tooltip="Limite de tiempo máximo de juego en este nivel.  \nHaga click para modificar",button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((0,0),(0,0)))],
        [sg.Button(image_filename=r"Data\Images\configuracion\boton-puntaje.png",key="-PUNTOS_D-",tooltip="Puntaje por letra en este nivel.  \nHaga click para modificar",button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((0,0),(5,5)))],
        [sg.Button(image_filename=r"Data\Images\configuracion\boton-fichas.png",key="-FICHAS_D-",tooltip="Cantidad de fichas por letra en este nivel.  \nHaga click para modificar",button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((0,0),(0,0)))],
    ]

    niveles = [
        [sg.Column(facil,background_color='#40B7C9',pad=((0,0),(0,0))),
        sg.Column(medio,background_color='#40B7C9',pad=((70,70),(6,0))),
        sg.Column(dificil,background_color='#40B7C9',pad=((0,0),(0,0)))]
    ]

    botones = [
        [sg.Button(image_filename=r"Data\Images\configuracion\boton-menu.png",key="-BACK-",button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((0,450),(0,0))),
        sg.Button(image_filename=r"Data\Images\configuracion\boton-guardar.png",key='-GUARDAR-',button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((0,15),(0,0))),
        sg.Button(image_filename=r"Data\Images\configuracion\boton-restaurar-valores.png",key='-RESTAURAR_VALORES-',button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((0,0),(0,0)))]
    ]

    layout = [
        [sg.Image(r"Data\Images\Configuracion\titulo.png",background_color='#40B7C9',pad=((70,0),(10,0)))],
        [sg.Column(niveles,background_color='#40B7C9',pad=((100,0),(40,0)))],
        [sg.Column(botones,background_color='#40B7C9',pad=((20,20),(90,0)))]
        ]

    return sg.Window('ScrabbleAR - Configuración',layout,size=(1000,600),background_color='#40B7C9')

if __name__ == "__main__":
    w = hacer_ventana("*Predeterminado*","*Predeterminado*","*Predeterminado*")

    event = w.read()

    w.close()