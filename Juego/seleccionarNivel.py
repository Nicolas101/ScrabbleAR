def seleccionar_nivel():
    """Muestra la ventana para seleccionar el nivel del juego.\n
    Retorna el nivel elegido y los datos del mismo
    """
    def cargar_datos(nombre_archivo):
        """Retorna los datos del archivo de nivel pasado por parámetro
        """
        import os
        import json
        
        dir_actual = os.getcwd()
        ubicacion_archivo = (dir_actual+'\\Data\\Files\\'+nombre_archivo) #armo la direccion donde esta el archivo deseado
        archivo = open(ubicacion_archivo,'r') #abro el archivo en modo solo lectura 
        lis_datos = json.load(archivo) #consigo la lista de datos la cual puede tener un solo elemento o dos en caso de que haya una modificacion
        diccionario = lis_datos[len(lis_datos)-1] #saco el diccionario el cual tiene los datos que necesito(letras y tiempo)
        
        return diccionario

    from Windows import windowSeleccionarNivel
    window_nivel = windowSeleccionarNivel.hacer_ventana()

    event, values= window_nivel.read()
    datos = []   
     
    #**************** CLICK EN FACIL ****************
    if event == '-FACIL-':
        datos = cargar_datos('Facil.json')
    
    #**************** CLICK EN MEDIO ****************
    elif event == '-MEDIO-':
        datos = cargar_datos('Medio.json')
    
    #**************** CLICK EN DIFICIL ****************
    elif event == '-DIFICIL-':
        datos = cargar_datos('Dificil.json')

    window_nivel.close()
    return [event,datos]




    
