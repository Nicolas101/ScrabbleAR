def main(nivel,variables):
    from Windows import windowPausa
    window = windowPausa.hacer_ventana()

    event, values = window.read()
    if event == "-GUARDAR_Y_SALIR-":
        seguir = False
        game_over = False
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

    elif event == "-SALIR_SIN_GUARDAR-":
        game_over = False
        datos_partida = [False]

    elif event == "-REANUDAR-":
        datos_partida = None
        game_over = False
    
    elif event == "-TERMINAR_PARTIDA-":
        game_over = True
        datos_partida = None

    window.close()
    return [event, game_over, datos_partida]

