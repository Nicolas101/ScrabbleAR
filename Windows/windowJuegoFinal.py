def hacer_ventana(imagen_titulo, total_maquina, puntaje_maquina, restar_maquina, total_usuario, puntaje_usuario, restar_usuario):
    import PySimpleGUI as sg

    layout = [
        [sg.Image(imagen_titulo,background_color="#40B7C9",pad=((10,0),(10,10)))],
        [sg.Text("Tus puntos:",background_color="#40B7C9",font=("Arial black",12),text_color="black",pad=((35,0),(0,0))),sg.Text(str(total_usuario)+" ("+str(puntaje_usuario)+" - "+str(restar_usuario)+")",background_color="#40B7C9",font=("Arial black",12),text_color="black")],
        [sg.Text("Puntos CPU:",background_color="#40B7C9",font=("Arial black",12),text_color="black",pad=((30,0),(0,0))),sg.Text(str(total_maquina)+" ("+str(puntaje_maquina)+" - "+str(restar_maquina)+")",background_color="#40B7C9",font=("Arial black",12),text_color="black")],
        [sg.Button(image_filename=r"Data\Images\Juego\Partida-terminada\Ventana-final\boton-menu.png",button_color=("#40B7C9","#40B7C9"),border_width=0,pad=((70,0),(10,0)))]
    ]
    window = sg.Window("Scrabblear - Fin",layout,size=(300,200),background_color="#40B7C9")

    return window
