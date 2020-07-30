def start_game(nivel,datos):
    """Muestra la ventana de juego y el desarrollo de la partida
    """
    if nivel != None:
        try:
            #Si se ejecuta el ScrabbleAR.py:
            from Juego.validarPalabra import es_valida, clasificar
            from Juego.Clases.BolsaFichas import crear_bolsa
            from Juego.Clases.Tablero import crear_tablero    
            from Juego.Clases.FilaDeFichas import crear_fila_fichas                     
            from Juego.Clases.Jugador import Jugador
            from Juego.Clases.Maquina import Maquina
        except ModuleNotFoundError:
            #Si se ejecuta este archivo:
            from validarPalabra import es_valida, clasificar
            from Clases.BolsaFichas import crear_bolsa
            from Clases.Tablero import crear_tablero
            from Clases.FilaDeFichas import crear_fila_fichas            
            from Clases.Jugador import Jugador
            from Clases.Maquina import Maquina

        from Windows import windowJuego, windowPausa
        import PySimpleGUI as sg
        import random
        import time

        #BOLSA DE FICHAS
        bolsa_fichas = crear_bolsa(datos['letras'])

        #TABLERO
        tablero,pad_tablero,num_random,tamaño_tablero = crear_tablero(bolsa_fichas)

        #FILA DE FICHAS
        fila_fichasJ = crear_fila_fichas(bolsa_fichas, 'FJ')
        fila_fichasM = crear_fila_fichas(bolsa_fichas, 'FM')

        #PANTALLA DE JUEGO
        window_game = windowJuego.hacer_ventana(tablero.getLayout(),fila_fichasJ.getLayout(),fila_fichasM.getLayout(),num_random,pad_tablero,(1000,600))

        #PANTALLA DE PAUSA
        window_pausa = windowPausa.hacer_ventana()

        #USUARIO Y MAQUINA
        usuario = Jugador()
        maquina = Maquina()
 
        turno = random.randint(0,1) # 0: turno del usuario // 1: turno del oponente
        
        game_over = False

        #TIMER
        seconds = 00
        minutes = 00
        time_start = time.time()
        tiempo_limite = datos['tiempo']

        while True:                 
            window_game.read(timeout=0)
            
            if not game_over:

                # *************************************** TURNO DEL USUARIO ********************************************** 
                if (turno == 0): 
                    window_game["-TURNO-"].update("Tu turno")

                    no_event = True
                    while no_event:
                        event, values = window_game.read(1000)

                        #ACTUALIZACION DEL TIMER
                        seconds = int(time.time() - time_start) - minutes*60
                        if seconds >= 60:
                            minutes += 1
                            seconds = 00
                        window_game['-RELOJ-'].Update(str(minutes)+":"+str(seconds))

                        #PREGUNTAR SI SE LLEGO AL TIEMPO LIMITE
                        if minutes == tiempo_limite:
                            game_over = True
                            game_over_text = "Se acabo el tiempo, fin del juego"
                            break

                        if event != "__TIMEOUT__":
                            no_event = False

                    #*********** CERRAR LA VENTANA **********
                    if(event is None):
                        break
                    
                    #*********** CLICK EN LA FILA DE FICHAS **********
                    elif fila_fichasJ.click(event):
                        if bolsa_fichas.estaHabilitada():
                            fila_fichasJ.agregarFichaACambiar(event,window_game)
                        else:
                            if not fila_fichasJ.hayFichaSelected():
                                fila_fichasJ.marcarFichaSelected(window_game,event) 
                            else:
                                fila_fichasJ.desmarcarFichaSelected(window_game)
                                fila_fichasJ.marcarFichaSelected(window_game,event)
                            tablero.habilitar(window_game)

                    #*********** CLICK EN EL TABLERO **********    
                    elif tablero.click(event):
                        window_game['-B_CAMBIAR_PASAR-'].update(disabled=True)
                        tablero.insertarFicha(event,window_game,window_game[fila_fichasJ.getFichaSelected()].GetText()) 
                        fila_fichasJ.sacarFicha(window_game)            
                        tablero.deshabilitar(window_game)

                    #*********** CLICK EN CONFIRMAR JUGADA **********
                    elif(event == "-CONFIRMAR-"):
                        window_game['-B_CAMBIAR_PASAR-'].update(disabled=False)
                        palabra = tablero.verificarPalabra()

                        if (es_valida(palabra,nivel)):
                            window_game['text-confirmar'].update('Palabra correcta',visible=True)
                            usuario.sumarPuntos(bolsa_fichas.devolverPuntaje(palabra,tablero.copiaPalabra(),tablero.getCasillasEspeciales()))
                            window_game["-PuntosJ-"].update(str(usuario.getPuntaje()))
                            tablero.reiniciarPalabra()
                            nuevas_fichas = bolsa_fichas.letras_random(len(palabra))

                            if (nuevas_fichas == []):
                                game_over = True
                                game_over_text = "Se acabaron las fichas, juego terminado"
                                print('fin')
                                #FIN DEL JUEGO PORQUE NO HAY MAS FICHAS
                            else:
                                fila_fichasJ.insertarFichas(window_game,nuevas_fichas)
                                turno = 1
                        else:
                            fichas_a_devolver = tablero.devolverFichas(window_game)
                            fila_fichasJ.insertarFichas(window_game,fichas_a_devolver)
                            window_game['text-confirmar'].update('Palabra incorrecta',visible=True)

                    #*********** CLICK EN CAMBIAR FICHAS **********
                    elif(event == '-B_CAMBIAR_PASAR-'):
                        if (usuario.getCambiosFichas() != 0):
                            if fila_fichasJ.hayFichaSelected():
                                fila_fichasJ.desmarcarFichaSelected(window_game)
                            bolsa_fichas.habilitar()
                            tablero.deshabilitar(window_game)
                            window_game["-CONFIRMAR-"].Update(disabled=True)
                            window_game['cambiar_fichas_text'].Update(visible=True)
                            window_game['Aceptar'].Update(visible=True)
                            window_game["Cancelar"].Update(visible=True)
                        else:
                            usuario.pasarTurno()
                            if (usuario.getTurnosPasados() == 3):
                                print(usuario.getTurnosPasados())
                                window_game['-B_CAMBIAR_PASAR-'].Update('Cambiar fichas')
                            usuario.verificarTurnosPasados()
                            turno = 1

                    #*********** CLICK EN ACEPTAR (CAMBIAR FICHAS) **********    
                    elif(event == 'Aceptar'):
                        usuario.restarCambio()
                        window_game['-CONFIRMAR-'].Update(disabled=False)
                        if (usuario.getCambiosFichas() == 0):
                            window_game['-B_CAMBIAR_PASAR-'].Update('Pasar turno')
                        if fila_fichasJ.cambiarFichas(window_game,bolsa_fichas):
                            bolsa_fichas.deshabilitar()
                            window_game['cambiar_fichas_text'].Update(visible=False)
                            window_game['Aceptar'].Update(visible=False)
                            window_game['Cancelar'].Update(visible=False)
                            turno = 1
                        else:
                            game_over = True
                            game_over_text = "Se acabaron las fichas, juego terminado"
                            print('fin')
                            #se termina el juego porq no hay fichas suficientes
                    
                    #*********** CLICK EN CANCELAR (CAMBIAR FICHAS) **********    
                    elif event == 'Cancelar':
                        fila_fichasJ.cancelarCambioDeFichas(window_game) 
                        window_game['Aceptar'].Update(visible=False)
                        window_game['Cancelar'].Update(visible=False)
                        window_game['cambiar_fichas_text'].Update(visible=False)
                        bolsa_fichas.deshabilitar()
                        window_game['-CONFIRMAR-'].Update(disabled=False)

                    #*********** CLICK EN PAUSA **********
                    elif event == "-PAUSA-":
                        
                        tiempo_cuando_pauso = time.time()
                        window_game.Disable()
                        window_pausa.UnHide()
                        event, values = window_pausa.read()
                        if event == "-REANUDAR-":
                            window_pausa.Hide()
                            window_game.Enable()
                            window_game.Hide()
                            window_game.UnHide()
                            time_start += time.time() - tiempo_cuando_pauso
                        elif event == "-SALIR_SIN_GUARDAR-":
                            window_pausa.Hide()
                            game_over=True
                            break
                        elif event == "-SALIR_Y_GUARDAR-":
                            window_pausa.Hide()
                            game_over=True
                            #guardar_partida() (a implementar)

                    #*********** CLICK EN TERMINAR PARTIDA **********
                    #a implementar
        
                # *************************************** TURNO DE LA MAQUINA **********************************************       
                else:
                    window_game["-TURNO-"].update("Turno del oponente")
                    window_game.read(timeout=1000)
                    
                    #ACTUALIZACION DEL TIMER
                    seconds = int(time.time() - time_start) - minutes*60
                    if seconds >= 60:
                        minutes += 1
                        seconds = 00
                    window_game['-RELOJ-'].Update(str(minutes)+":"+str(seconds))

                    #PREGUNTAR SI SE LLEGO AL TIEMPO LIMITE
                    if minutes == tiempo_limite:
                        game_over = True
                        game_over_text = "Se acabo el tiempo, fin del juego"
                        break

                    #la maquina intenta armar una palabra con las letras que tiene en su fila
                    palabra_maquina, cant_letras_a_cambiar = maquina.armarPalabra(fila_fichasM,bolsa_fichas,tablero,nivel)
                    #si pudo formar la palabra la inserta en el tablero y trae nuevas letras de la bolsa
                    if (palabra_maquina != 'xxxxxx'): 
                        palabra_armada = True
                        maquina.insertarPalabra(palabra_maquina, tablero, window_game, tamaño_tablero)
                        maquina.sumarPuntos(bolsa_fichas.devolverPuntaje(palabra_maquina,tablero.copiaPalabra(),tablero.getCasillasEspeciales()))
                        window_game["-PuntosM-"].update(str(maquina.getPuntaje()))
                        puede_cambiar = True #variable que avisa que se puede hacer el cambio de fichas
                    else:
                        #aviso en pantalla que la maquina no pudo ingresar una palabra, por lo que cambia todas las fichas o pasa el turno(falta implementar)
                        palabra_armada = False
                        if (maquina.getCambiosFichas() == 0):
                            #si la maquina no tiene mas cambios de fichas se debe pasar el turno
                            maquina.pasarTurno()
                            maquina.verificarTurnosPasados()
                            puede_cambiar = False
                        else:
                            #si tiene cambios de fichas se resta uno y se hace el cambio de las 7 fichas
                            maquina.restarCambio()
                            puede_cambiar = True  
                    if (puede_cambiar): #si la palabra fue correcta o la maquina tenia cambios de fichas se realiza el cambio
                        nuevas_letras = bolsa_fichas.letras_random(cant_letras_a_cambiar)
                        if nuevas_letras != []:
                            #si habia suficientes letras en la bolsa de ficha las agrega a la fila      
                            maquina.nuevasLetras(fila_fichasM, nuevas_letras, tablero, palabra_armada) 
                        else:
                            #termina el juego porq no hay mas fichas
                            game_over = True
                            game_over_text = "Se acabaron las fichas, juego terminado"
                            print('fin')
                    turno = 0           
            else:
                window_game.Disable()
                #terminar_juego() (a implementar)
                sg.popup(game_over_text)
                break

        window_game.close()

def terminar_juego():
    pass

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
    start_game("-FACIL-",diccionario)
