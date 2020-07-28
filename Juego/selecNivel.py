def seleccionar_nivel():
    """Muestra la ventana para seleccionar el nivel del juego y retorna el nivel elegido
    """
    from Juego.Windows import windowNivel
    window_nivel = windowNivel.hacer_ventana((1000,600))

    event, values= window_nivel.read()

    window_nivel.close()
    return event