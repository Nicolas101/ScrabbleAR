def main(nivel,variables):
    """Despliega la venta de pausa la cual para el tiempo de la partida y permite:
    -Reanudar
    -Guardar y salir
    -Salir sin guardar
    """
    from Windows import windowPausa
    import PySimpleGUI as sg
    window = windowPausa.hacer_ventana()

    event, values = window.Read()
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
        sg.Popup('Partida guardada correctamente!')

    elif event == "-SALIR_SIN_GUARDAR-":
        game_over = False
        datos_partida = [False]

    elif event == "-REANUDAR-":
        datos_partida = None
        game_over = False

    elif event == "-TERMINAR_PARTIDA-":
        game_over = True
        datos_partida = None

    window.Close()
    return [event, game_over, datos_partida]
