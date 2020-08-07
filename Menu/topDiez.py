def nuevo_puntaje(datos):
    """Si el puntaje entra en el top 10 de mejores puntajes de su nivel, lo ingresa
    """
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

def mostrar_topDiez():
    """Muestra la ventana de top 10 puntajes
    """
    from Windows import windowTopDiez
    import json
    import os

    dir_actual = os.getcwd()
    direc = dir_actual+'\\Data\\Files\\TopDiez.json'
    archivo = open(direc,'r')
    data_arch = json.load(archivo)
    archivo.close()

    window = windowTopDiez.hacer_ventana(data_arch['Facil'],data_arch['Medio'],data_arch['Dificil'])

    event,values = window.read()

    window.close()

