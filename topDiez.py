def nuevo_puntaje(datos):
    import json
    import os

    dir_actual = os.getcwd()
    direc = dir_actual+'\\Data\\Files\\TopDiez.json'
    archivo = open(direc,'r')
    data_arch = json.load(archivo)
    archivo.close()
    if datos[2] == '-FACIL-':
        nivel = 'Facil'
    elif datos[2] == '-MEDIO-':
        nivel = 'Medio'
    else:
        nivel = 'Dificil'
    lis_aux = data_arch[nivel][:]
    elem = lis_aux[len(lis_aux)-1]
    if datos[0]>elem['puntaje']:
        lis_aux.pop()
        lis_aux.append({'fecha':datos[1],'puntaje':datos[0]})
        lis_ord = list(sorted(lis_aux,key=lambda dicci: dicci['puntaje'],reverse=True))
        data_arch[nivel]= lis_ord
        archivo = open(direc,'w')
        json.dump(data_arch,archivo,indent=4)
        archivo.close()

