def mostrar_configuracion():
    """Muestra la pantalla de configuracion y permite modificar:
    -Tiempo que dura la partida
    -Puntos que vale cada letra
    -Cantidad de fichas por letra
    """
    from Windows import windowConfig  
    from Configuracion import tiempo,letras
    import os
    import json

    window_config = windowConfig.hacer_ventana((1000,600))

    lis_ubicaciones = generar_ubicaciones()#en lis ubicaciones quedan las direcciones de los archivos facil medio y dificil
    
    #cada variable data tiene una lista que puede tener uno o dos elementos dependiendo si solo esta la config.
    #original o tambien hay una modificada
    data_facil = obtener_datos_archivo(lis_ubicaciones[0])
    data_medio = obtener_datos_archivo(lis_ubicaciones[1])
    data_dificil = obtener_datos_archivo(lis_ubicaciones[2])

    #guardan la conf original o la copia si es que hay
    dic_facil_aux = copiar_diccionario(data_facil[(len(data_facil)-1)])
    dic_medio_aux = copiar_diccionario(data_medio[(len(data_medio)-1)])
    dic_dificil_aux = copiar_diccionario(data_dificil[(len(data_medio)-1)])

    facil_modifico = False
    medio_modifico = False
    dificil_modifico = False

    while True:
        event, values = window_config.read()

        #****************CLICK EN VOLVER*********************
        if event in (None,"-BACK-"):
            break
        
        #****************CLICK EN TIEMPO DE FACIL*********************
        elif event == '-TIEMPO_F-':
            tiempo_facil = tiempo.ejecutar(dic_facil_aux['tiempo'])
            if tiempo_facil != None:
                dic_facil_aux['tiempo'] = tiempo_facil
                facil_modifico = True

        #****************CLICK EN PUNTOS DE FACIL*********************
        elif event == '-PUNTOS_F-':
            valores = letras.ejecutar(dict(dic_facil_aux['letras']),'Puntos')
            if valores != None:
                facil_modifico = True
                for letra in valores:
                    dic_facil_aux['letras'][letra]['puntuacion'] = valores[letra][0]
        
        #****************CLICK EN FICHAS DE FACIL*********************
        elif event == '-FICHAS_F-':
            valores = letras.ejecutar(dict(dic_facil_aux['letras']),'Cantidad de Fichas')
            if valores != None:
                facil_modifico = True
                for letra in valores:
                    dic_facil_aux['letras'][letra]['cantidad'] = valores[letra][0]

        #****************CLICK EN TIEMPO DE MEDIO*********************
        elif event == '-TIEMPO_M-':
            tiempo_medio = tiempo.ejecutar(dic_medio_aux['tiempo'])
            if tiempo_medio != None:
                dic_medio_aux['tiempo'] = tiempo_medio
                medio_modifico = True
        
        #****************CLICK EN PUNTOS DE MEDIO*********************
        elif event == '-PUNTOS_M-':
            valores = letras.ejecutar(dict(dic_medio_aux['letras']),'Puntos')
            if valores != None:
                medio_modifico = True
                for letra in valores:
                    dic_medio_aux['letras'][letra]['puntuacion'] = valores[letra][0]
        
        #****************CLICK EN FICHAS DE MEDIO*********************
        elif event == '-FICHAS_M-':
            valores = letras.ejecutar(dict(dic_medio_aux['letras']),'Cantidad de Fichas')
            if valores != None:
                medio_modifico = True
                for letra in valores:
                    dic_medio_aux['letras'][letra]['cantidad'] = valores[letra][0]

        #****************CLICK EN TIEMPO DE DIFICIL*********************
        elif event == '-TIEMPO_D-':
            tiempo_dificil = tiempo.ejecutar(dic_dificil_aux['tiempo'])
            if tiempo_dificil != None:
                dic_dificil_aux['tiempo'] = tiempo_dificil
                dificil_modifico = True
        
        #****************CLICK EN PUNTOS DE DIFICIL*********************
        elif event == '-PUNTOS_D-':
            valores = letras.ejecutar(dict(dic_dificil_aux['letras']),'Puntos')
            if valores != None:
                dificil_modifico = True
                for letra in valores:
                    dic_dificil_aux['letras'][letra]['puntuacion'] = valores[letra][0]
        
        #****************CLICK EN FICHAS DE DIFICIL*********************
        elif event == '-FICHAS_D-':
            valores = letras.ejecutar(dict(dic_dificil_aux['letras']),'Cantidad de Fichas')
            if valores != None:
                dificil_modifico = True
                for letra in valores:
                    dic_dificil_aux['letras'][letra]['cantidad'] = valores[letra][0]

        #****************CLICK EN RESTAURAR VALORES*********************
        elif event == '-RESTAURAR_VALORES-':
            dic_facil_aux = copiar_diccionario(restaurar_valores(data_facil, lis_ubicaciones[0]))
            dic_medio_aux = copiar_diccionario(restaurar_valores(data_medio, lis_ubicaciones[1]))
            dic_dificil_aux = copiar_diccionario(restaurar_valores(data_dificil, lis_ubicaciones[2]))

        #****************CLICK EN GUARDAR*********************
        elif event == '-GUARDAR-':
            if facil_modifico:
                guardar_cambios(dic_facil_aux,data_facil,lis_ubicaciones[0])
            if medio_modifico:
                guardar_cambios(dic_medio_aux,data_medio,lis_ubicaciones[1])
            if dificil_modifico:
                guardar_cambios(dic_dificil_aux,data_dificil,lis_ubicaciones[2])
    
    window_config.close()

def restaurar_valores(data, ubicacion):
    """borra las modificaciones si es que hay y devuelve la configuracion original
    """
    import json
    if len(data)>1:
        arch = open(ubicacion,'w')
        data.pop()
        json.dump(data,arch,indent=4)
        arch.close()
    return data[0].copy()

def guardar_cambios(diccionario,data,ubicacion):
    """guarda en el archivo la nueva configuracion modificada
    """
    import json
    if len(data)>1:
        data.pop()
    data.append(diccionario)
    arch = open(ubicacion, 'w')
    json.dump(data,arch,indent=4)
    arch.close()

def generar_ubicaciones():
    """genera una lista con las ubicaciones de los tres archivos
    """
    import os

    lis_ubicaciones = []
    lis_archivos = ['Facil.json','Medio.json','Dificil.json']
    dir_actual = os.getcwd()
    for arch in lis_archivos:
        direc = dir_actual+'\\Data\\Files\\'+arch
        lis_ubicaciones.append(direc)
    
    return lis_ubicaciones

def obtener_datos_archivo(ubicacion):
    """devuelve el contenido del archivo cuya ubicacion se pasa por parametro
    """
    import json
    archivo = open(ubicacion,'r')
    data = json.load(archivo)
    archivo.close()

    return data[:]

def copiar_diccionario(dic_viejo):
    """devuelve una copia del diccionario pasado por parametro
    """
    dic_nuevo = {'letras':{},'tiempo':dic_viejo['tiempo']}
    for letra in dic_viejo['letras']:
        dic_nuevo['letras'][letra] = dic_viejo['letras'][letra].copy()
    return dic_nuevo

if __name__ == "__main__":
    mostrar_configuracion()   