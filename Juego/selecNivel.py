def seleccionar_nivel():
    """Muestra la ventana para seleccionar el nivel del juego, retorna el nivel elegido y los datos del mismo
    """
    from Juego.Windows import windowNivel

    window_nivel = windowNivel.hacer_ventana((1000,600))

    event, values= window_nivel.read()
    datos = []
    #*********** CLICK EN FACIL **********
    if event == '-FACIL-':
        datos = elegir_nivel('Facil.json')
    
    #*********** CLICK EN MEDIO **********
    elif event == '-MEDIO-':
        datos = elegir_nivel('Medio.json')
    
    #*********** CLICK EN DIFICIL **********
    elif event == '-DIFICIL':
        datos = elegir_nivel('Dificil.json')
    
    #*********** CLICK EN PERSONALIZADO **********
    elif event == '-PERSONALIZADO-':
        pass

    window_nivel.close()
    return [event,datos]

def elegir_nivel(nombre_archivo):
    """Este proceso devuelve los datos del archivo de nivel pasado por parametro
    """
    import os
    import json
    
    dir_actual = os.getcwd()
    ubicacion_archivo = (dir_actual+'\\Data\\'+nombre_archivo) #armo la direccion donde esta el archivo deseado
    archivo = open(ubicacion_archivo,'r') #abro el archivo en modo solo lectura 
    lis_datos = json.load(archivo) #consigo la lista de datos la cual puede tener un solo elemento o dos en caso de que haya una modificacion
    diccionario = lis_datos[len(lis_datos)-1] #saco el diccionario el cual tiene los datos que necesito(letras y tiempo)
    
    return diccionario


    
