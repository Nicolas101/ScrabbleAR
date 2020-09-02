def hacer_ventana(facil,medio,dificil):
    """Devuelve la ventana de 'Top 10 puntajes'
    """
    import PySimpleGUI as sg

    def hacer_top(facil,medio,dificil):
        """Retorna una lista donde cada elemento es una lista con 4 elementos: [top, facil, medio, difcil]
        """
        #10 listas de 4 elementos
        lista_return = []
        for i in range(0,10):
            row = []
            row.append(sg.Text(str(i+1)+".",size=(3,1),font=("Arial black",14),background_color='#40B7C9',text_color="black",pad=((0,0),(0,0))))
            row.append(sg.Text(str(facil[i]["puntaje"])+" // "+facil[i]["fecha"],size=(18,1),font=("Arial black",12),background_color='#40B7C9',text_color="black",justification="center",pad=((0,0),(0,0))))
            row.append(sg.Text(str(medio[i]["puntaje"])+" // "+medio[i]["fecha"],size=(18,1),font=("Arial black",12),background_color='#40B7C9',text_color="black",justification="center",pad=((100,110),(0,0))))
            row.append(sg.Text(str(dificil[i]["puntaje"])+" // "+dificil[i]["fecha"],size=(18,1),font=("Arial black",12),background_color='#40B7C9',text_color="black",justification="center"))
            lista_return.append(row)

        return lista_return

    top = hacer_top(facil, medio, dificil)

    import os
    if os.access(r'Data\Images\Juego\Avatar-CPU.png',0):
        header = [
            [sg.Image(r"Data\Images\TopDiez\facil.png",background_color='#40B7C9',pad=((0,0),(0,0))),
            sg.Image(r"Data\Images\TopDiez\medio.png",background_color='#40B7C9',pad=((150,150),(5,0))),
            sg.Image(r"Data\Images\TopDiez\dificil.png",background_color='#40B7C9',pad=((0,0),(0,0)))]
        ]

        tabla_top_diez = [
            [sg.Column(header,background_color='#40B7C9',pad=((80,0),(10,0)))],
            top[0],top[1],top[2],top[3],top[4],top[5],top[6],top[7],top[8],top[9]
        ]

        layout = [
            [sg.Image(r"Data\Images\TopDiez\titulo.png",background_color='#40B7C9',pad=((280,0),(20,0)))],
            [sg.Column(tabla_top_diez,background_color='#40B7C9',pad=((50,0),(0,0)))],
            [sg.Button(image_filename=r"Data\Images\TopDiez\boton-menu.png",button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((410,0),(20,0)))]
        ]
    else:
        header = [
            [sg.Image(r"Data/Images/TopDiez/facil.png",background_color='#40B7C9',pad=((0,0),(0,0))),
            sg.Image(r"Data/Images/TopDiez/medio.png",background_color='#40B7C9',pad=((150,140),(5,0))),
            sg.Image(r"Data/Images/TopDiez/dificil.png",background_color='#40B7C9',pad=((0,0),(0,0)))]
        ]

        tabla_top_diez = [
            [sg.Column(header,background_color='#40B7C9',pad=((55,0),(10,0)))],
            top[0],top[1],top[2],top[3],top[4],top[5],top[6],top[7],top[8],top[9]
        ]

        layout = [
            [sg.Image(r"Data/Images/TopDiez/titulo.png",background_color='#40B7C9',pad=((280,0),(20,0)))],
            [sg.Column(tabla_top_diez,background_color='#40B7C9',pad=((50,0),(0,0)))],
            [sg.Button(image_filename=r"Data/Images/TopDiez/boton-menu.png",button_color=('#40B7C9','#40B7C9'),border_width=0,pad=((390,0),(20,0)))]
        ]

    window = sg.Window("ScrabbleAR - Top 10",size=(1000,600),background_color='#40B7C9').Layout(layout)

    return window
