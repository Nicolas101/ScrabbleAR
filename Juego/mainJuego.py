def start_game():
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

    nivel = seleccionar_nivel()

    if nivel != "":
        from Juego.validarPalabra import esValida, clasificar

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

        puntos_jugador = 0

        while True:
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
                palabra = tablero.getPalabra()
                if (esValida(palabra,nivel)):
                    window_game['text-confirmar'].update('Palabra correcta',visible=True)
                    puntos_jugador += bolsa_fichas.devolverPuntaje(palabra)
                    window_game["-misPuntos-"].update(str(puntos_jugador))
                    tablero.reiniciarPalabra()
                    cant_letras = len(palabra)
                    fila_fichasJ.insertarFichas(window_game,bolsa_fichas.letras_random(cant_letras))
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
        window_game.close() 

if __name__ == "__main__":
    start_game()
