def start_game(nivel,variables):
    """Muestra la ventana para jugar y todo su desarrollo.\n
    Retorna si termino la partida y los datos de ella
    """
    from Juego.validarPalabra import es_valida, clasificar
    from Juego import pausa,terminarPartida
    from Windows import windowSalirJuego
    from datetime import date
    
    game_over = False
    maquina_pasa_turno = True
    
    window_salir = windowSalirJuego.hacer_ventana()
    
    variables["Timer"].iniciarTimer()

    while True:                 
        variables["Window_juego"].read(timeout=0) 

        if not game_over: #Si no termino el juego:

            if variables["Turno"] == 0: 
                # *******************************************************************************************************************
                # ************************************************** TURNO DEL USUARIO **********************************************
                # *******************************************************************************************************************
                if maquina_pasa_turno:
                    variables["Window_juego"]["-TEXT_JUGADOR-"].update("TU TURNO!\nFORMA UNA PALABRA")
                variables["Fichas_jugador"].habilitar()

                no_event = True
                while no_event:
                    event,values = variables["Window_juego"].read(1000)

                    if event != "__TIMEOUT__":
                        variables["Timer"].ajustarTiempo()
                        no_event = False

                    variables["Timer"].actualizarTimer()
                    variables["Window_juego"]['-RELOJ-'].Update(variables["Timer"].tiempoActual())

                    if variables["Timer"].termino():
                        game_over = True
                        game_over_text = "Se acabo el tiempo, fin del juego"
                        break

                #********************************* CLICK EN LA X (CERRAR VENTANA) *********************************
                if event is None:
                    event_salir, values_salir = window_salir.read()
                    if event_salir == "-GUARDAR_Y_SALIR2-":
                        datos_partida = [True,
                            variables["Bolsa_de_fichas"],
                            variables["Tablero"],
                            variables["Fichas_jugador"],
                            variables["Fichas_maquina"],
                            variables["Usuario"],
                            variables["Maquina"],
                            variables["Timer"].getSegundos(),
                            variables["Timer"].getMinutos(),
                            variables["Timer"].getTiempoLimite(),
                            variables["Turno"],
                            variables["Confirmar_habilitado"],
                            variables["Cambiar_habilitado"],
                            variables["Clases_validas"],
                            nivel
                        ] #El primer elemento si es True indica que hay una partida guardada, False en caso contrario

                    else:
                        datos_partida = [False]

                    window_salir.close()
                    break 

                #********************************* CLICK EN PAUSA *********************************
                elif event == "-PAUSA-":
                    variables["Timer"].pausar()
                    output, game_over, datos_partida = pausa.main(nivel,variables)
                    if output == "-REANUDAR-":
                        variables["Timer"].reanudar()
                    elif output in ("-GUARDAR_Y_SALIR-","-SALIR_SIN_GUARDAR-"):
                        break
                    elif output == "-TERMINAR_PARTIDA-":
                        game_over_text = "Fin del juego, partida finalizada"
                        continue
                
                #********************************* CLICK EN LA FILA DE FICHAS *********************************
                elif variables["Fichas_jugador"].click(event) and variables["Fichas_jugador"].estaHabilitada():
                    if variables["Bolsa_de_fichas"].estaHabilitada(): #Si quiere cambiar fichas:
                        variables["Fichas_jugador"].agregarFichaACambiar(event,variables["Window_juego"])

                    else: #Si quiere poner una ficha en el tablero:
                        variables["Window_juego"]["-TEXT_CPU-"].update("")

                        if not variables["Fichas_jugador"].hayFichaSelected():
                            variables["Fichas_jugador"].marcarFichaSelected(variables["Window_juego"],event) 
                        else:
                            variables["Fichas_jugador"].desmarcarFichaSelected(variables["Window_juego"])
                            variables["Fichas_jugador"].marcarFichaSelected(variables["Window_juego"],event)
                        variables["Tablero"].habilitar()

                #********************************* CLICK EN EL TABLERO *********************************   
                elif variables["Tablero"].click(event) and variables["Tablero"].estaHabilitado():
                    ficha = variables["Fichas_jugador"].sacarFicha(variables["Window_juego"]) 
                    variables["Tablero"].insertarFicha(event,variables["Window_juego"],ficha) 
                    variables["Cambiar_habilitado"] = False                                 
                    variables["Tablero"].deshabilitar()

                #********************************* CLICK EN CONFIRMAR JUGADA *********************************
                elif event == "-CONFIRMAR-" and variables["Confirmar_habilitado"]:
                    variables["Cambiar_habilitado"] = True
                    palabra,con_inicio = variables["Tablero"].verificarPalabra()

                    if es_valida(palabra,nivel,variables["Clases_validas"]): #Si la palabra es válida:
                        variables["Window_juego"]['-TEXT_JUGADOR-'].update('PALABRA CORRECTA!',visible=True)
                        variables["Usuario"].ingresarPalabra(palabra,variables["Bolsa_de_fichas"].devolverPuntaje(palabra,variables["Tablero"].copiaPalabra(),variables["Tablero"].getCasillasEspeciales()))
                        variables["Window_juego"]['-PALABRAS_JUGADOR-'].Update("Palabras ingresadas:",variables["Usuario"].getPalabras())
                        variables["Window_juego"]["-PUNTOS_JUGADOR-"].update(str(variables["Usuario"].getPuntaje()))
                        cant_letras = len(palabra)
                        if con_inicio:
                            cant_letras -= 1
                        nuevas_fichas = variables["Bolsa_de_fichas"].letras_random(cant_letras)

                        #Verificar si se pueden reponer las fichas usadas:
                        if nuevas_fichas == []:
                            #fin del juego 
                            game_over = True
                            game_over_text = "No hay mas fichas, juego terminado"
                        else:               
                            variables["Fichas_jugador"].insertarFichas(variables["Window_juego"],nuevas_fichas)
                            variables["Tablero"].reiniciarPalabra()
                            variables["Turno"] = 1

                    else: #Si la palabra no es válida:
                        variables["Window_juego"]['-TEXT_JUGADOR-'].update('PALABRA INCORRECTA!\nINTENTE NUEVAMENTE',visible=True)
                        fichas_a_devolver = variables["Tablero"].devolverFichas(variables["Window_juego"])
                        variables["Fichas_jugador"].insertarFichas(variables["Window_juego"],fichas_a_devolver)  

                #********************************** CLICK EN CAMBIAR FICHAS *********************************
                elif event == "-CAMBIAR_PASAR-" and variables["Cambiar_habilitado"]:
                    if variables["Usuario"].getCambiosFichas() != 0: #Si tiene cambios disponibles:

                        if variables["Fichas_jugador"].hayFichaSelected():
                            variables["Fichas_jugador"].desmarcarFichaSelected(variables["Window_juego"])

                        variables["Tablero"].deshabilitar()
                        variables["Confirmar_habilitado"] = False
                        variables["Bolsa_de_fichas"].habilitar() 
                        variables["Window_juego"]["-TEXT_JUGADOR-"].update("SELECCIONA LAS FICHAS\nPARA CAMBIAR")
                        variables["Window_juego"]["-TEXT_CPU-"].update("")
                        variables["Window_juego"]['-ACEPTAR-'].Update(visible=True)
                        variables["Window_juego"]["-CANCELAR-"].Update(visible=True)

                    else: #Si no tiene cambios disponibles
                        variables["Usuario"].pasarTurno()
                        variables["Window_juego"]["-TEXT_JUGADOR-"].update("HAS PASADO EL TURNO")
                        variables["Turno"] = 1

                        if (variables["Usuario"].getTurnosPasados() == 3):
                            variables["Window_juego"]["-CAMBIAR_PASAR-"].Update(image_filename=r"Data\Images\Juego\Botones\boton-cambiar-fichas.png")
                            variables["Usuario"].verificarTurnosPasados()

                #********************************* CLICK EN ACEPTAR (CAMBIAR FICHAS) *********************************    
                elif event == '-ACEPTAR-':
                    variables["Usuario"].restarCambio()
                    variables["Confirmar_habilitado"] = True

                    if variables["Fichas_jugador"].cambiarFichas(variables["Window_juego"],variables["Bolsa_de_fichas"]): #Si se pudo reponer todas las fichas a cambiar:
                        variables["Bolsa_de_fichas"].deshabilitar()
                        variables["Window_juego"]["-TEXT_JUGADOR-"].Update("")
                        variables["Window_juego"]['-ACEPTAR-'].Update(visible=False)
                        variables["Window_juego"]['-CANCELAR-'].Update(visible=False)
                        variables["Turno"] = 1

                    else: #Si no se pudieron reponer todas las fichas a cambiar:
                        #Se termina el juego porque no hay fichas suficientes
                        game_over = True
                        game_over_text = "No hay mas fichas, juego terminado"

                    if (variables["Usuario"].getCambiosFichas() == 0): #Si no le quedan mas cambios de ficha:
                        #Se actualiza el boton de "cambiar fichas" a "pasar turno"
                        variables["Window_juego"]['-CAMBIAR_PASAR-'].Update(image_filename=r"Data\Images\Juego\Botones\boton-pasar-turno.png")   
                
                #********************************* CLICK EN CANCELAR (CAMBIAR FICHAS) *********************************    
                elif event == '-CANCELAR-':
                    variables["Bolsa_de_fichas"].deshabilitar()
                    variables["Window_juego"]['-ACEPTAR-'].Update(visible=False)
                    variables["Window_juego"]['-CANCELAR-'].Update(visible=False)
                    variables["Window_juego"]["-TEXT_JUGADOR-"].Update("")
                    variables["Fichas_jugador"].cancelarCambioDeFichas(variables["Window_juego"]) 
                    variables["Confirmar_habilitado"] = True
                
                maquina_pasa_turno = False

            else:
                # *******************************************************************************************************************
                # ********************************************* TURNO DE LA MAQUINA *************************************************
                # *******************************************************************************************************************
                variables["Window_juego"]["-TEXT_CPU-"].update("TURNO DEL OPONENTE")
                variables["Window_juego"].read(timeout=1000)

                variables["Timer"].actualizarTimer()
                variables["Window_juego"]['-RELOJ-'].Update(variables["Timer"].tiempoActual())

                if variables["Timer"].termino():
                        game_over = True
                        game_over_text = "Se acabo el tiempo, fin del juego"

                else: #Si no se acabo el tiempo de la partida:
                    #la maquina intenta armar una palabra con sus fichas:
                    variables["Window_juego"]["-TEXT_JUGADOR-"].update("")

                    palabra_maquina, cant_letras_a_cambiar = variables["Maquina"].armarPalabra(variables["Fichas_maquina"],variables["Bolsa_de_fichas"],variables["Tablero"],nivel,variables["Clases_validas"])

                    if palabra_maquina != 'xxxxxx': #Si encontro una palabra válida:
                        variables["Window_juego"]["-TEXT_CPU-"].update("PALABRA CORRECTA!")
                        palabra_armada = True
                        variables["Maquina"].insertarPalabra(palabra_maquina, variables["Tablero"], variables["Window_juego"], variables["Tablero"].getTamaño()) #Inserta la palabra en el tablero
                        variables["Maquina"].ingresarPalabra(palabra_maquina,variables["Bolsa_de_fichas"].devolverPuntaje(palabra_maquina,variables["Tablero"].copiaPalabra(),variables["Tablero"].getCasillasEspeciales()))
                        variables["Window_juego"]['-PALABRAS_CPU-'].Update('Palabras ingresadas:',variables["Maquina"].getPalabras())
                        variables["Window_juego"]["-PUNTOS_CPU-"].update(str(variables["Maquina"].getPuntaje()))
                        puede_cambiar = True #variable que avisa que se puede hacer el cambio de fichas

                    else: #Si no pudo formar una palabra:
                        palabra_armada = False

                        if variables["Maquina"].getCambiosFichas() == 0:  #Si la maquina no tiene más cambios de fichas:
                            variables["Window_juego"]["-TEXT_CPU-"].Update("TURNO PASADO")
                            variables["Maquina"].pasarTurno()
                            variables["Maquina"].verificarTurnosPasados()
                            puede_cambiar = False

                        else: #Si la maquina tiene cambios de fichas:
                            variables["Window_juego"]["-TEXT_CPU-"].Update("CAMBIO DE FICHAS")
                            variables["Maquina"].restarCambio()
                            puede_cambiar = True

                    if puede_cambiar: #Si la palabra fue correcta o la maquina tenia cambios de fichas se realiza el cambio
                        if palabra_armada == False:
                            letras_maquina_devolver = variables["Fichas_maquina"].getLetras()
                            variables["Fichas_maquina"].eliminarTodasLasLetras()
                        nuevas_letras = variables["Bolsa_de_fichas"].letras_random(cant_letras_a_cambiar)
                        if palabra_armada == False:
                            variables["Bolsa_de_fichas"].devolverLetras(letras_maquina_devolver)
                            

                        if nuevas_letras != []: #Si se puede hacer el cambio   
                            variables["Maquina"].nuevasLetras(variables["Fichas_maquina"], nuevas_letras, variables["Tablero"], palabra_armada)  #Agrega las nuevas fichas

                        else:  #Si no se pudo hacer el cambio de fichas:
                            #Se termina el juego porque no hay mas fichas
                            game_over = True
                            game_over_text = "No hay mas fichas, juego terminado"

                    variables["Cambiar_habilitado"] = True
                    variables["Confirmar_habilitado"]  = True
                    maquina_pasa_turno = True
                    variables["Turno"] = 0  

        else: #Si termino el juego:

            if variables['Turno'] == 0: 
                #Si termino el juego en el turno del jugador y no termino de completar una palabra, devuelvo las fichas al jugador
                fichas_devolver = variables['Tablero'].devolverFichas(variables['Window_juego'])
                variables['Fichas_jugador'].insertarFichas(variables['Window_juego'],fichas_devolver)
            
            total_usuario = terminarPartida.main(variables["Maquina"].getPuntaje(),
                variables["Bolsa_de_fichas"].calcularPuntajeLista(variables["Fichas_maquina"].getLetras()),
                variables["Fichas_maquina"].getLetras(),
                variables["Usuario"].getPuntaje(),
                variables["Bolsa_de_fichas"].calcularPuntajeLista(variables["Fichas_jugador"].getLetras()),
                variables["Fichas_jugador"].getLetras(),
                game_over_text
            )

            datos_partida = [total_usuario,str(date.today()),nivel]
            break

    variables["Window_juego"].close()

    return [game_over,datos_partida]


