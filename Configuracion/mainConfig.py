def mostrar_configuracion():   
    from Configuracion.Windows import windowConfig  
    from Configuracion import tiempo,letras
    import os
    import json

    window_config = windowConfig.hacer_ventana((1000,600))

    lis_ubicaciones = generar_ubicaciones()
    
    data_facil = obtener_datos_archivo(lis_ubicaciones[0])
    data_medio = obtener_datos_archivo(lis_ubicaciones[1])
    data_dificil = obtener_datos_archivo(lis_ubicaciones[2])

    #dic_facil_aux = dict(data_facil[(len(data_facil)-1)])
    dic_facil_aux = copiar_diccionario(data_facil[(len(data_facil)-1)])
    dic_medio_aux = copiar_diccionario(data_medio[(len(data_medio)-1)])
    dic_dificil_aux = copiar_diccionario(data_dificil[(len(data_medio)-1)])

    facil_modifico = False
    medio_modifico = False
    dificil_modifico = False

    while True:
        event, values = window_config.read()
        if event in (None,"-BACK-"):
            break

        elif event == '-TIEMPO_F-':
            tiempo_facil = tiempo.ejecutar(dic_facil_aux['tiempo'])
            if tiempo_facil != None:
                dic_facil_aux['tiempo'] = tiempo_facil
                facil_modifico = True

        elif event == '-PUNTOS_F-':
            valores = letras.ejecutar(dict(dic_facil_aux['letras']),'Puntos')
            if valores != None:
                facil_modifico = True
                for letra in valores:
                    dic_facil_aux['letras'][letra]['puntuacion'] = valores[letra][0]

        elif event == '-TIEMPO_M-':
            tiempo_medio = tiempo.ejecutar(dic_medio_aux['tiempo'])
            if tiempo_medio != None:
                dic_medio_aux['tiempo'] = tiempo_medio
                medio_modifico = True

        elif event == '-TIEMPO_D-':
            tiempo_dificil = tiempo.ejecutar(dic_dificil_aux['tiempo'])
            if tiempo_dificil != None:
                dic_dificil_aux['tiempo'] = tiempo_dificil
                dificil_modifico = True

        elif event == '-RESTAURAR_VALORES-':
            dic_facil_aux = copiar_diccionario(restaurar_valores(data_facil, lis_ubicaciones[0]))
            dic_medio_aux = copiar_diccionario(restaurar_valores(data_medio, lis_ubicaciones[1]))
            dic_dificil_aux = copiar_diccionario(restaurar_valores(data_dificil, lis_ubicaciones[2]))

        elif event == '-GUARDAR-':
            if facil_modifico:
                guardar_cambios(dic_facil_aux,data_facil,lis_ubicaciones[0])
            if medio_modifico:
                guardar_cambios(dic_medio_aux,data_medio,lis_ubicaciones[1])
            if dificil_modifico:
                guardar_cambios(dic_dificil_aux,data_dificil,lis_ubicaciones[2])
    
    window_config.close()

def restaurar_valores(data, ubicacion):
    import json
    if len(data)>1:
        arch = open(ubicacion,'w')
        data.pop()
        json.dump(data,arch,indent=4)
        arch.close()
    return data[0].copy()

def guardar_cambios(diccionario,data,ubicacion):
    import json
    if len(data)>1:
        data.pop()
    data.append(diccionario)
    arch = open(ubicacion, 'w')
    json.dump(data,arch,indent=4)
    arch.close()

def generar_ubicaciones():
    import os

    lis_ubicaciones = []
    lis_archivos = ['Facil.json','Medio.json','Dificil.json']
    dir_actual = os.getcwd()
    for arch in lis_archivos:
        direc = dir_actual+'\\Data\\'+arch
        lis_ubicaciones.append(direc)
    
    return lis_ubicaciones

def obtener_datos_archivo(ubicacion):
    import json
    archivo = open(ubicacion,'r')
    data = json.load(archivo)
    archivo.close()

    return data[:]

def copiar_diccionario(dic_viejo):
    dic_nuevo = {'letras':{},'tiempo':dic_viejo['tiempo']}
    for letra in dic_viejo['letras']:
        dic_nuevo['letras'][letra] = dic_viejo['letras'][letra].copy()
    return dic_nuevo

if __name__ == "__main__":
    mostrar_configuracion()   