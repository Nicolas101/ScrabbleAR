def ejecutar(diccionario,categoria):
    """Muestra la ventana de seleccionar puntaje/cantidad de cada letra
    """
    from Windows import windowLetras

    if categoria == 'Puntos':
        clave = 'puntuacion'
    else:
        clave = 'cantidad'

    window = windowLetras.hacer_ventana(diccionario,categoria,clave)

    event,values = window.read()
    
    if event == '-CONFIRMAR-':
        valores = values
    elif event in ['-CANCELAR-',None]:
        valores = None
    window.close()

    return valores
    




