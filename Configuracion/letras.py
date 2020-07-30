def ejecutar(diccionario,categoria):
    from Configuracion.Windows import windowLetras

    if categoria == 'Puntos':
        clave = 'puntuacion'
    else:
        clave = 'cantidad'

    window = windowLetras.hacer_ventana(diccionario,categoria,clave)

    event,values = window.read()
    
    if event == 'Ok':
        valores = values
    elif event in ['Cancelar',None]:
        valores = None
    window.close()
    return valores
    




