def seleccionar_nivel():
    """Muestra la ventana para seleccionar el nivel del juego y retorna el nivel elegido
    """
    from Juego.Windows import windowNivel
    window_nivel = windowNivel.hacer_ventana((1000,600))

    event = window_nivel.read()

    window_nivel.close()
    return event

def start_game(nivel):
    """Muestra la ventana de juego y el desarrollo de la partida
    """
    if nivel != None:
        try:
            from Juego.validarPalabra import es_valida, clasificar
            from Juego.Clases.BolsaFichas import crear_bolsa
            from Juego.Clases.Tablero import crear_tablero    
            from Juego.Clases.FilaDeFichas import crear_fila_fichas          
            from Juego.Windows import windowJuego
            from Juego.Clases.Jugador import Jugador
            from Juego.Clases.Maquina import Maquina
        except ModuleNotFoundError:
            from validarPalabra import es_valida, clasificar
            from Clases.BolsaFichas import crear_bolsa
            from Clases.Tablero import crear_tablero
            from Clases.FilaDeFichas import crear_fila_fichas
            from Windows import windowJuego
            from Clases.Jugador import Jugador
            from Clases.Maquina import Maquina
        import PySimpleGUI as sg
        import random

        #BOLSA DE FICHAS
        bolsa_fichas = crear_bolsa()

        #TABLERO
        tablero,pad_tablero,num_random = crear_tablero(bolsa_fichas)

        #FILA DE FICHAS
        fila_fichasJ = crear_fila_fichas(bolsa_fichas, 'FJ')
        fila_fichasM = crear_fila_fichas(bolsa_fichas, 'FM')

        #PANTALLA DE JUEGO
        window_game = windowJuego.hacer_ventana(tablero.getLayout(),fila_fichasJ.getLayout(),fila_fichasM.getLayout(),num_random,pad_tablero,(1000,600))

        #USUARIO Y MAQUINA
        usuario = Jugador()
        maquina = Maquina()
 
        turno = random.randint(0,1) # 0: turno del usuario // 1: turno del oponente
        jugar = True
        
        game_over = False

        while True:                 
            window_game.read(timeout=0)
            
            if not game_over:
                # *************************************** TURNO DEL USUARIO ********************************************** 
                if (turno == 0): 
                    window_game["-TURNO-"].update("Tu turno")
                    event, values = window_game.read() 

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
                        window_game['Cambiar fichas'].update(disabled=True)
                        tablero.insertarFicha(event,window_game,window_game[fila_fichasJ.getFichaSelected()].GetText()) 
                        fila_fichasJ.sacarFicha(window_game)            
                        tablero.deshabilitar(window_game)

                    #*********** CLICK EN CONFIRMAR JUGADA **********
                    elif(event == "Confirmar Jugada"):
                        window_game['Cambiar fichas'].update(disabled=False)
                        palabra = tablero.verificarPalabra()
                        if (palabra != 'xxxxxx'):
                            if (es_valida(palabra,nivel)):
                                window_game['text-confirmar'].update('Palabra correcta',visible=True)
                                usuario.sumarPuntos(bolsa_fichas.devolverPuntaje(palabra,tablero.copiaPalabra(),tablero.getCasillasEspeciales()))
                                window_game["-PuntosJ-"].update(str(usuario.getPuntaje()))
                                tablero.reiniciarPalabra()
                                nuevas_fichas = bolsa_fichas.letras_random(len(palabra))
                                if (nuevas_fichas == []):
                                    game_over = True
                                    game_over_text = "Se acabaron las fichas, juego terminado"
                                    break
                                    #se termina el juego porq no hay fichas suficientes
                                else:
                                    fila_fichasJ.insertarFichas(window_game,nuevas_fichas)
                                    turno = 1
                            else:
                                fichas_a_devolver = tablero.devolverFichas(window_game)
                                fila_fichasJ.insertarFichas(window_game,fichas_a_devolver)
                                window_game['text-confirmar'].update('Palabra incorrecta',visible=True)

                    #*********** CLICK EN CAMBIAR FICHAS **********
                    elif(event == 'Cambiar fichas'):
                        if fila_fichasJ.hayFichaSelected():
                            fila_fichasJ.desmarcarFichaSelected(window_game)
                        bolsa_fichas.habilitar()
                        tablero.deshabilitar(window_game)
                        window_game['cambiar_fichas_text'].Update(visible=True)
                        window_game['Aceptar'].Update(visible=True)

                    #*********** CLICK EN ACEPTAR (CAMBIAR FICHAS) **********    
                    elif(event == 'Aceptar'):
                        if fila_fichasJ.cambiarFichas(window_game,bolsa_fichas):
                            bolsa_fichas.deshabilitar()
                            window_game['cambiar_fichas_text'].Update(visible=False)
                            window_game['Aceptar'].Update(visible=False)
                            turno = 1
                        else:
                            game_over = True
                            game_over_text = "Se acabaron las fichas, juego terminado"
                            break
                            #se termina el juego porq no hay fichas suficientes

        
                # *************************************** TURNO DE LA MAQUINA **********************************************       
                else:
                    window_game["-TURNO-"].update("Turno del oponente")
                    window_game.read(timeout=4000)
                    palabra_maquina = maquina.armarPalabra(fila_fichasM,bolsa_fichas,tablero)
                    #falta hacer
                    turno = 0           
            else:
                sg.popup(game_over_text)

        window_game.close() 

if __name__ == "__main__":
    start_game("-FACIL-")
