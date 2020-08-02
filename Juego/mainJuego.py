def start_game(nivel,datos,partida_guardada):
    """Muestra la ventana de juego y el desarrollo de la partida
    """
    if nivel != None:
        from Juego.validarPalabra import es_valida, clasificar
        from Juego.Clases.BolsaFichas import crear_bolsa
        from Juego.Clases.Tablero import crear_tablero    
        from Juego.Clases.FilaDeFichas import crear_fila_fichas                     
        from Juego.Clases.Jugador import Jugador
        from Juego.Clases.Maquina import Maquina
        from Juego.Clases.Timer import Timer
        from Windows import windowJuego, windowPausa
        import PySimpleGUI as sg
        import random
        
        if (not partida_guardada):
            #BOLSA DE FICHAS
            bolsa_fichas = crear_bolsa(datos['letras'])

            #TABLERO
            tablero,tamaño_tablero = crear_tablero(bolsa_fichas)

            #FILA DE FICHAS
            fila_fichasJ = crear_fila_fichas(bolsa_fichas,False)
            fila_fichasM = crear_fila_fichas(bolsa_fichas,True)

            #USUARIO Y MAQUINA
            usuario = Jugador()
            maquina = Maquina()

            #TEMPORIZADOR
            timer = Timer(datos['tiempo'])

            turno = random.randint(0,1) # 0: turno del usuario // 1: turno del oponente
        
        else: #si es la continuacion de una partida guardada
            
            #BOLSA DE FICHAS
            bolsa_fichas = datos[1]
            
            #TABLERO
            tablero = datos[2]
            tamaño_tablero = datos[3]
            
            #FILA DE FICHAS
            fila_fichasJ = datos[4]
            fila_fichasM = datos[5]
            
            #USUARIO Y MAQUINA
            usuario = datos[6]
            maquina = datos[7]
            
            #TEMPORIZADOR
            timer = Timer(datos[10],datos[8],datos[9])
            turno = datos[11]




        #PANTALLA DE JUEGO
        window_game = windowJuego.hacer_ventana(tablero.getLayout(),fila_fichasJ.getLayout(),fila_fichasM.getLayout(),(1000,600),usuario.getPuntaje(),maquina.getPuntaje())

        #PANTALLA DE PAUSA
        window_pausa = windowPausa.hacer_ventana()


        
        game_over = False
        if turno == 0 :
            confirmar_habilitado = True
            cambiar_habilitado = True
        else:
            confirmar_habilitado = False
            cambiar_habilitado = False
        
        timer.iniciarTimer()
        while True:                 
            window_game.read(timeout=0)            
            if not game_over:
                if turno == 0: 
                    # *******************************************************************************************************************
                    # ************************************************** TURNO DEL USUARIO **********************************************
                    # *******************************************************************************************************************
                    window_game["-TEXT_JUGADOR-"].update("TU TURNO!")
                    fila_fichasJ.habilitar()

                    no_event = True
                    while no_event:
                        event,values = window_game.read(1000)

                        if event != "__TIMEOUT__":
                            timer.ajustarTiempo()
                            no_event = False

                        timer.actualizarTimer()
                        window_game['-RELOJ-'].Update(timer.tiempoActual())

                        if timer.termino():
                            game_over = True
                            game_over_text = "Se acabo el tiempo, fin del juego"
                            break

                    #********************************* CERRAR LA VENTANA *********************************
                    if event is None:
                        #preguntar si desea salir sin guardar
                        #si desea salir sin guardar primer dato de datos_partida en falso
                        game_over = False
                        datos_partida = [False]#este primer elemento de la lista dice si se debe guardar o no la partida
                        break
                    
                    #********************************* CLICK EN LA FILA DE FICHAS *********************************
                    elif fila_fichasJ.click(event) and fila_fichasJ.estaHabilitada():
                        if bolsa_fichas.estaHabilitada(): #Si quiere cambiar fichas:
                            fila_fichasJ.agregarFichaACambiar(event,window_game)

                        else: #Si quiere poner una ficha en el tablero:
                            if not fila_fichasJ.hayFichaSelected():
                                fila_fichasJ.marcarFichaSelected(window_game,event) 
                            else:
                                fila_fichasJ.desmarcarFichaSelected(window_game)
                                fila_fichasJ.marcarFichaSelected(window_game,event)
                            tablero.habilitar()

                    #********************************* CLICK EN EL TABLERO *********************************   
                    elif tablero.click(event) and tablero.estaHabilitado():
                        #window_game["-CAMBIAR_PASAR-"].update(disabled=True)
                        ficha = fila_fichasJ.sacarFicha(window_game) 
                        tablero.insertarFicha(event,window_game,ficha) 
                        cambiar_habilitado = False                                 
                        tablero.deshabilitar()

                    #********************************* CLICK EN CONFIRMAR JUGADA *********************************
                    elif event == "-CONFIRMAR-" and confirmar_habilitado:
                        cambiar_habilitado = True
                        #window_game["-CAMBIAR_PASAR-"].update(disabled=False)
                        palabra,con_inicio = tablero.verificarPalabra()
                        print(palabra)

                        if es_valida(palabra,nivel): #Si la palabra es válida:
                            window_game['-TEXT_JUGADOR-'].update('PALABRA CORRECTA!',visible=True)
                            usuario.sumarPuntos(bolsa_fichas.devolverPuntaje(palabra,tablero.copiaPalabra(),tablero.getCasillasEspeciales()))
                            window_game["-PUNTOS_JUGADOR-"].update(str(usuario.getPuntaje()))
                            cant_letras = len(palabra)
                            if con_inicio:
                                cant_letras -= 1
                            nuevas_fichas = bolsa_fichas.letras_random(cant_letras)
                            print(nuevas_fichas)

                            #Verificar si se pueden reponer las fichas usadas:
                            if nuevas_fichas == []:
                                #fin del juego 
                                game_over = True
                                game_over_text = "Se acabaron las fichas, juego terminado"
                            else:               
                                fila_fichasJ.insertarFichas(window_game,nuevas_fichas)
                                tablero.reiniciarPalabra()
                                turno = 1

                        else: #Si la palabra no es válida:
                            window_game['-TEXT_JUGADOR-'].update('PALABRA INCORRECTA!',visible=True)
                            fichas_a_devolver = tablero.devolverFichas(window_game)
                            fila_fichasJ.insertarFichas(window_game,fichas_a_devolver)  

                    #********************************** CLICK EN CAMBIAR FICHAS *********************************
                    elif event == "-CAMBIAR_PASAR-" and cambiar_habilitado:
                        if usuario.getCambiosFichas() != 0: #Si tiene cambios disponibles:

                            if fila_fichasJ.hayFichaSelected():
                                fila_fichasJ.desmarcarFichaSelected(window_game)
                            tablero.deshabilitar()
                            confirmar_habilitado = False
                            #window_game["-CONFIRMAR-"].Update(disabled=True)

                            bolsa_fichas.habilitar() 
                            window_game['-TEXT_JUGADOR-'].Update("Selecciones las fichas\n para cambiar")
                            window_game['-ACEPTAR-'].Update(visible=True)
                            window_game["-CANCELAR-"].Update(visible=True)

                        else: #Si no tiene cambios disponibles
                            usuario.pasarTurno()
                            turno = 1

                            if (usuario.getTurnosPasados() == 3):
                                window_game["-CAMBIAR_PASAR-"].Update(image_filename=r"Data\Images\Juego\Botones\boton-cambiar-fichas.png")
                                usuario.verificarTurnosPasados()

                    #********************************* CLICK EN ACEPTAR (CAMBIAR FICHAS) *********************************    
                    elif event == '-ACEPTAR-':
                        usuario.restarCambio()
                        confirmar_habilitado = True
                        #window_game['-CONFIRMAR-'].Update(disabled=False)

                        if fila_fichasJ.cambiarFichas(window_game,bolsa_fichas): #Si se pudo reponer todas las fichas a cambiar:
                            bolsa_fichas.deshabilitar()
                            window_game["-TEXT_JUGADOR-"].Update("")
                            window_game['-ACEPTAR-'].Update(visible=False)
                            window_game['-CANCELAR-'].Update(visible=False)
                            turno = 1

                        else: #Si no se pudieron reponer todas las fichas a cambiar:
                            #Se termina el juego porque no hay fichas suficientes
                            game_over = True
                            game_over_text = "Se acabaron las fichas, juego terminado"

                        if (usuario.getCambiosFichas() == 0): #Si no le quedan mas cambios de ficha:
                            #Se actualiza el boton de "cambiar fichas" a "pasar turno"
                            window_game['-CAMBIAR_PASAR-'].Update(image_filename=r"Data\Images\Juego\Botones\boton-pasar-turno.png")   
                    
                    #********************************* CLICK EN CANCELAR (CAMBIAR FICHAS) *********************************    
                    elif event == '-CANCELAR-':
                        bolsa_fichas.deshabilitar()
                        window_game['-ACEPTAR-'].Update(visible=False)
                        window_game['-CANCELAR-'].Update(visible=False)
                        window_game["-TEXT_JUGADOR-"].Update("")
                        fila_fichasJ.cancelarCambioDeFichas(window_game) 
                        confirmar_habilitado = True
                        #window_game['-CONFIRMAR-'].Update(disabled=False)

                    #********************************* CLICK EN PAUSA *********************************
                    elif event == "-PAUSA-":
                        timer.pausar()
                        window_game.Disable()
                        window_pausa.UnHide()
                        event_pausa, values_pausa = window_pausa.read()
                        if event_pausa == "-REANUDAR-":
                            timer.reanudar()
                            window_pausa.Hide()
                            window_game.Enable()
                            window_game.Hide()
                            window_game.UnHide()
                        elif event_pausa == "-SALIR_SIN_GUARDAR-":
                            window_pausa.Hide()
                            game_over = False
                            datos_partida = [False]#este primer elemento de la lista dice si se debe guardar o no la partida
                            break
                        elif event_pausa == "-SALIR_Y_GUARDAR-":
                            window_pausa.Hide()
                            game_over=False
                            datos_partida = [True,bolsa_fichas,tablero,tamaño_tablero,fila_fichasJ,fila_fichasM,usuario,maquina,timer.getSegundos(),timer.getMinutos(),timer.getTiempoLimite(),turno,nivel]#true dice que la partida se guarda
                            #guardar_partida() (a implementar)
                            break

                    #********************************* CLICK EN TERMINAR PARTIDA *********************************
                    elif event == '-TERMINAR_PARTIDA-':
                        game_over = True
                        game_over_text = 'Has terminado la partida'
                    
                else:
                    # *******************************************************************************************************************
                    # ********************************************* TURNO DE LA MAQUINA *************************************************
                    # *******************************************************************************************************************
                    window_game["-TEXT_CPU-"].update("TURNO DEL OPONENTE")
                    window_game.read(timeout=1000)
                    timer.actualizarTimer()
                    window_game['-RELOJ-'].Update(timer.tiempoActual())

                    if timer.termino():
                            game_over = True
                            game_over_text = "Se acabo el tiempo, fin del juego"
                    
                    else:
                        #la maquina intenta armar una palabra con sus fichas:
                        palabra_maquina, cant_letras_a_cambiar = maquina.armarPalabra(fila_fichasM,bolsa_fichas,tablero,nivel)

                        if palabra_maquina != 'xxxxxx': #Si encontro una palabra válida:
                            window_game["-TEXT_CPU-"].update("PALABRA CORRECTA!")
                            palabra_armada = True
                            maquina.insertarPalabra(palabra_maquina, tablero, window_game, tamaño_tablero) #Inserta la palabra en el tablero
                            maquina.sumarPuntos(bolsa_fichas.devolverPuntaje(palabra_maquina,tablero.copiaPalabra(),tablero.getCasillasEspeciales()))
                            window_game["-PUNTOS_CPU-"].update(str(maquina.getPuntaje()))
                            puede_cambiar = True #variable que avisa que se puede hacer el cambio de fichas

                        else: #Si no pudo formar una palabra:
                            palabra_armada = False

                            if maquina.getCambiosFichas() == 0:  #Si la maquina no tiene más cambios de fichas:
                                window_game["-TEXT_CPU-"].Update("TURNO PASADO")
                                maquina.pasarTurno()
                                maquina.verificarTurnosPasados()
                                puede_cambiar = False

                            else: #Si la maquina tiene cambios de fichas:
                                window_game["-TEXT_CPU-"].Update("CAMBIO DE FICHAS")
                                maquina.restarCambio()
                                puede_cambiar = True  

                        if puede_cambiar: #Si la palabra fue correcta o la maquina tenia cambios de fichas se realiza el cambio
                            nuevas_letras = bolsa_fichas.letras_random(cant_letras_a_cambiar)

                            if nuevas_letras != []: #Si se puede hacer el cambio   
                                maquina.nuevasLetras(fila_fichasM, nuevas_letras, tablero, palabra_armada)  #Agrega las nuevas fichas

                            else:  #Si no se pudo hacer el cambio de fichas:
                                #Se termina el juego porque no hay mas fichas
                                game_over = True
                                game_over_text = "Se acabaron las fichas, juego terminado"

                        cambiar_habilitado = True
                        confirmar_habilitado = True
                        turno = 0  

                        if timer.termino():
                            game_over = True
                            game_over_text = "Se acabo el tiempo, fin del juego"    

            else:
                window_game.Disable()
                if usuario.getPuntaje()>maquina.getPuntaje():
                    game_over_text_dos = '¡Ganaste!'
                elif usuario.getPuntaje()<maquina.getPuntaje():
                    game_over_text_dos = 'Perdiste, lo siento :('
                else:
                    game_over_text_dos = '¡Es un empate!'
                sg.popup(game_over_text,game_over_text_dos,('Tu puntuación: '+str(usuario.getPuntaje())),('Puntos de la maquina: '+str(maquina.getPuntaje())))
                datos_partida = [usuario.getPuntaje(),'fecha',nivel]
                break

        window_game.close()
        print(game_over)
        print(datos_partida)
        return [game_over,datos_partida]


def guardar_partida():
    pass
#(martin va a hacer estos dos procesos entre hoy y mañana,tranca nico ta todo controlado)

if __name__ == "__main__":
    import os
    import json
    
    dir_actual = os.getcwd()
    ubicacion_archivo = (dir_actual+'\\Data\\Facil.json')
    archivo = open(ubicacion_archivo,'r')
    lis_datos = json.load(archivo)
    diccionario = lis_datos[len(lis_datos)-1]
    start_game("-FACIL-",diccionario,False)
