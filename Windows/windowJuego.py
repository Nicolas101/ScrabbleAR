def hacer_ventana(layout_tablero, layout_fichasJ, layout_fichasM,puntos_jug,puntos_ma,palabras_usuario,palabras_maquina,nivel,clases_validas):
    import PySimpleGUI as sg

    def armar_clases(nivel, clases):
        if nivel == "-DIFICIL-": 
            if "JJ" in clases:
                layout = [sg.Image(r"Data\Images\Juego\Clases-validas\clase-verbos.png",background_color="#2781D3",pad=((10,0),(0,0))),
                    sg.Image(r"Data\Images\Juego\Clases-validas\clase-sustantivos.png",background_color="#2781D3",pad=((5,0),(0,0))),
                    sg.Image(r"Data\Images\Juego\Clases-validas\clase-seleccionada-adjetivos.png",background_color="#2781D3",pad=((0,0),(0,0)))]
            else:
                layout = [sg.Image(r"Data\Images\Juego\Clases-validas\clase-verbos.png",background_color="#2781D3",pad=((12,0),(0,0))),
                    sg.Image(r"Data\Images\Juego\Clases-validas\clase-seleccionada-sustantivos.png",background_color="#2781D3",pad=((0,0),(0,0))),
                    sg.Image(r"Data\Images\Juego\Clases-validas\clase-adjetivos.png",background_color="#2781D3",pad=((0,0),(0,0)))]
        elif nivel == "-MEDIO-":
            layout = [sg.Image(r"Data\Images\Juego\Clases-validas\clase-verbos.png",background_color="#2781D3",pad=((10,0),(0,0))),
                    sg.Image(r"Data\Images\Juego\Clases-validas\clase-seleccionada-sustantivos.png",background_color="#2781D3",pad=((0,0),(0,0))),
                    sg.Image(r"Data\Images\Juego\Clases-validas\clase-seleccionada-adjetivos.png",background_color="#2781D3",pad=((0,0),(0,0)))]
        else:
            layout = [sg.Image(r"Data\Images\Juego\Clases-validas\clase-seleccionada-verbos.png",background_color="#2781D3",pad=((0,0),(0,0))),
                    sg.Image(r"Data\Images\Juego\Clases-validas\clase-seleccionada-sustantivos.png",background_color="#2781D3",pad=((0,0),(0,0))),
                    sg.Image(r"Data\Images\Juego\Clases-validas\clase-seleccionada-adjetivos.png",background_color="#2781D3",pad=((0,0),(0,0)))]

        return [layout]


    datos_cpu = [
        [sg.T("",key="-TEXT_CPU-",size=(20,1),font=("Arial black",10),text_color="black",background_color="#6AB2E5",pad=(0,0))],
        [sg.Combo(palabras_maquina,key="-PALABRAS_CPU-",default_value="Palabras ingresadas:",size=(25,1),readonly=True)],
        [sg.T("Puntos:",font=("Arial black",10),text_color="black",background_color="#6AB2E5",pad=(0,0)),sg.T(puntos_ma,key="-PUNTOS_CPU-",size=(4,1),font=("Arial black",10),text_color="black",background_color="#6AB2E5",pad=(0,0))]
    ]

    datos_jugador = [
        [sg.T("",key="-TEXT_JUGADOR-",size=(40,2),font=("Arial black",10),text_color="black",background_color="#6AB2E5",pad=(0,0))],
        [sg.Combo(palabras_usuario,key="-PALABRAS_JUGADOR-",default_value="Palabras ingresadas:",size=(25,1),readonly=True)],
        [sg.T("Puntos:",font=("Arial black",10),text_color="black",background_color="#6AB2E5",pad=(0,0)),sg.T(puntos_jug,key="-PUNTOS_JUGADOR-",size=(4,1),font=("Arial black",10),text_color="black",background_color="#6AB2E5",pad=(0,0))]
    ]

    #COLUMNA DE LA CPU
    cpu = [
        [sg.Image(r"Data\Images\Juego\Avatar-CPU.png",background_color="#6AB2E5",pad=(5,5)),sg.Column(datos_cpu,background_color="#6AB2E5",pad=((0,0),(20,0)))],
        [sg.Column(layout_fichasM,background_color="#6AB2E5")]
    ]

    #COLUMNA DEL JUGADOR
    jugador = [
        [sg.Image(r"Data\Images\Juego\Avatar-jugador.png",background_color="#6AB2E5",pad=(5,5)),sg.Column(datos_jugador,background_color="#6AB2E5",pad=((0,0),(15,0)))],
        [sg.Column(layout_fichasJ,background_color="#6AB2E5")]
    ]

    #BOTNES ACEPTAR - CANCELAR (CAMBIAR FICHAS)
    botones_add = [
        [sg.Button("",image_filename=r"Data\Images\Juego\Botones\boton-aceptar.png",key="-ACEPTAR-",button_color=("#2781D3","#2781D3"),border_width=0,visible=False)],
        [sg.Button("",image_filename=r"Data\Images\Juego\Botones\boton-cancelar.png",key="-CANCELAR-",button_color=("#2781D3","#2781D3"),border_width=0,visible=False)]
    ]

    #BOTONES CONFIRMAR JUGADA - CAMBIAR FICHAS
    botones = [
        [sg.Button("",image_filename=r"Data\Images\Juego\Botones\boton-confirmar-jugada.png",key="-CONFIRMAR-",button_color=("#2781D3","#2781D3"),border_width=0,pad=((20,0),(0,0))),
        sg.Button("",image_filename=r"Data\Images\Juego\Botones\boton-cambiar-fichas.png",key="-CAMBIAR_PASAR-",button_color=("#2781D3","#2781D3"),border_width=0),
        sg.Column(botones_add,background_color="#2781D3",pad=((0,0),(5,0)))]
    ]

    #BOTONES PAUSA - TIEMPO 
    tiempo = [
        [sg.Button("",image_filename=r"Data\Images\Juego\Botones\boton-pausa.png",key="-PAUSA-",button_color=("#2781D3","#2781D3"),border_width=0,pad=((120,0),(0,0))),
        sg.Text("",key="-RELOJ-",size=(7,1),font=("Arial black",12),text_color="black",background_color="#2781D3")]
    ]

    barra_datos = [
        [sg.Image(r"Data\Images\Juego\titulo-barra-datos.png",background_color="#2781D3",pad=((30,30),(5,0)))],
        [sg.Column(armar_clases(nivel, clases_validas),background_color="#2781D3",pad=((5,0),(0,5)))],
        [sg.Column(jugador,size=(385,175),background_color="#6AB2E5",pad=((5,0),(0,0)))],
        [sg.Column(botones,background_color="#2781D3")],
        [sg.Column(cpu,size=(385,175),background_color="#6AB2E5",pad=((5,0),(0,0)))],   
        [sg.Column(tiempo,background_color="#2781D3",pad=((0,0),(5,0)))]
    ]

    #VENTANA COMPLETA      
    layout = [
        [sg.Column(layout_tablero,background_color="#40B7C9"),
        sg.Column(barra_datos,background_color="#2781D3",size=(400,590))]
    ]
    window = sg.Window("ScrabbleAR - En partida",layout,size=(1000,600),background_color="#40B7C9",margins=(0,0))

    return window
    