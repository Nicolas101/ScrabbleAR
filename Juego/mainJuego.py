def seleccionar_nivel():
        #PANTALLA NIVEL
        from Juego.Windows import windowNivel
        window_nivel = windowNivel.hacer_vetnana((1000,600))

        nivel = ""
        while True:
            event, values = window_nivel.read()
            if event is None:
                nivel = ""
                break
            elif event == "-FACIL-":
                nivel = "facil"
                break
            elif event == "-MEDIO-":
                nivel = "medio"
                break
            elif event == "-DIFICL-":
                nivel = "dificil"
                break
            elif event == "-PERSONALIZADO-":
                nivel = "personalizado"
                break
        window_nivel.close()
        
        return nivel

def start_game(nivel): 
    if nivel != "":
        try:
            from Juego.validarPalabra import es_valida, clasificar

            #BOLSA DE FICHAS
            from Juego.Clases.BolsaFichas import crearBolsa
            bolsa_fichas = crearBolsa()

            #TABLERO
            from Juego.Clases.Tablero import crearTablero
            tablero,pad_tablero,num_random =  crearTablero(bolsa_fichas)

            #FILA DE FICHAS
            from Juego.Clases.FilaDeFichas import crearFilaFichas
            fila_fichasJ = crearFilaFichas(bolsa_fichas, 'FJ')
            fila_fichasM = crearFilaFichas(bolsa_fichas, 'FM')

            #PANTALLA DE JUEGO
            from Juego.Windows import windowJuego
            window_game = windowJuego.hacer_ventana(tablero.getLayout(),fila_fichasJ.getLayout(),fila_fichasM.getLayout(),num_random,pad_tablero,(1000,600))

            #USUARIO Y MAQUINA
            from Juego.Clases.Jugador import Jugador
            from Juego.Clases.Maquina import Maquina
            usuario = Jugador()
            maquina = Maquina()
        except ModuleNotFoundError:
            from validarPalabra import es_valida, clasificar

            #BOLSA DE FICHAS
            from Clases.BolsaFichas import crearBolsa
            bolsa_fichas = crearBolsa()

            #TABLERO
            from Clases.Tablero import crearTablero
            tablero,pad_tablero,num_random =  crearTablero(bolsa_fichas)

            #FILA DE FICHAS
            from Clases.FilaDeFichas import crearFilaFichas
            fila_fichasJ = crearFilaFichas(bolsa_fichas, 'FJ')
            fila_fichasM = crearFilaFichas(bolsa_fichas, 'FM')

            #PANTALLA DE JUEGO
            from Windows import windowJuego
            window_game = windowJuego.hacer_ventana(tablero.getLayout(),fila_fichasJ.getLayout(),fila_fichasM.getLayout(),num_random,pad_tablero,(1000,600))

            #USUARIO Y MAQUINA
            from Clases.Jugador import Jugador
            from Clases.Maquina import Maquina
            usuario = Jugador()
            maquina = Maquina()

        puntos_jugador = 0
        puntos_maquina = 0
        import random
        turno = random.randint(0,1)
        
        while True:       
            
            window_game.read(timeout=0)
            #TURNO DEL JUGADOR
            if (turno == 0): 
                window_game["-TURNO-"].update("Tu turno")
                event, values = window_game.read() 
                if(event is None):
                    break
                
                elif fila_fichasJ.click(event):
                    if bolsa_fichas.estaHabilitada():
                        pass
                    else:
                        if not fila_fichasJ.hayFichaSelected():
                            fila_fichasJ.marcarFichaSelected(window_game,event) 
                        else:
                            fila_fichasJ.desmarcarFichaSelected(window_game)
                            fila_fichasJ.marcarFichaSelected(window_game,event)
                        tablero.habilitar(window_game)
                    
                elif tablero.click(event): 
                    tablero.insertarFicha(event,window_game,window_game[fila_fichasJ.getFichaSelected()].GetText()) 
                    fila_fichasJ.sacarFicha(window_game)            
                    tablero.deshabilitar(window_game)

                elif(event == "Confirmar Jugada"):
                    palabra = tablero.verificarPalabra()
                    if (es_valida(palabra,nivel)):
                        window_game['text-confirmar'].update('Palabra correcta',visible=True)
                        puntos_jugador += bolsa_fichas.devolverPuntaje(palabra)
                        window_game["-PuntosJ-"].update(str(puntos_jugador))
                        tablero.reiniciarPalabra()
                        cant_letras = len(palabra)
                        fila_fichasJ.insertarFichas(window_game,bolsa_fichas.letras_random(cant_letras))
                        turno = 1
                    else:
                        fichas_a_devolver=tablero.devolverFichas(window_game)
                        fila_fichasJ.insertarFichas(window_game,fichas_a_devolver)
                        window_game['text-confirmar'].update('Palabra incorrecta',visible=True)

                elif(event == 'Cambiar fichas'):
                    bolsa_fichas.habilitar()
                    tablero.deshabilitar(window_game)
                    window_game['cambiar_fichas_text'].Update(visible=True)
                    window_game['Aceptar'].Update(visible=True)
                    
                elif(event == 'Aceptar'):
                    bolsa_fichas.deshabilitar()
                    window_game['cambiar_fichas_text'].Update(visible=False)
                    window_game['Aceptar'].Update(visible=False)
                    turno = 1
                    
            #TURNO DE LA MAQUINA        
            else:
                window_game["-TURNO-"].update("Turno del oponente")
                window_game.read(timeout=4000)
                palabra_maquina = maquina.armarPalabra(fila_fichasM,bolsa_fichas,tablero)
                #falta hacer
                turno = 0           
                 
        window_game.close() 

if __name__ == "__main__":
    start_game("facil")
