def guardar_partida(datos):
    """Guarda las variables de la partida, pasados por parametro, en un archivo .obj
    """
    import pickle
    import os
    dir_actual = os.getcwd()
    ubicacion_archivo = (dir_actual+'\\Data\\Files\\'+'partidaguardada.obj')
    f = open(ubicacion_archivo,'wb')
    pickle.dump(datos,f)
    f.close()

def hay_partida_guardada():
    """Retorna True si hay una partida guardada, False en caso contrario
    """
    import pickle
    import os
    dir_actual = os.getcwd()
    ubicacion_archivo = (dir_actual+'\\Data\\Files\\'+'partidaguardada.obj')
    f = open(ubicacion_archivo,'rb')
    datos = pickle.load(f)
    f.close()
    return datos[0]

def obtener_datos():
    """Devuelve los datos de la partida guardada para poder continuarla
    """
    import pickle
    import os
    dir_actual = os.getcwd()
    ubicacion_archivo = (dir_actual+'\\Data\\Files\\'+'partidaguardada.obj')
    f = open(ubicacion_archivo,'rb')
    datos = pickle.load(f)
    nivel = datos.pop()
    f.close()
    return [nivel,datos]

def continuar_partida():
    """Muestra una ventana para saber si desea continuar con la partida.\n
    Retorna True si clickea en SI, False si clickea en NO
    """
    from Windows import windowPartidaGuardada

    window = windowPartidaGuardada.hacer_ventana()
    event, values = window.read()
    if event == "-SI-":
        valor = True
    else:
        valor = False
    window.close()

    return valor

def eliminar_partida():
    """Setea el primer dato del archivo de partida guardada en False, para indicar que no hay una partida guardada
    """
    import pickle
    import os
    dir_actual = os.getcwd()
    ubicacion_archivo = (dir_actual+'\\Data\\Files\\'+'partidaguardada.obj')
    f = open(ubicacion_archivo,'wb')
    pickle.dump([False],f)
    f.close()


