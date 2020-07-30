def ejecutar(valor_por_defecto):
    
    from Windows import windowTiempo
    window = windowTiempo.hacer_ventanta(valor_por_defecto)

    while True:
        event,values = window.read()

        if event in [None,'Cancelar']:
            resultado = None
            break

        elif event == 'Ok':
            resultado = values['Listbox'][0]
            break

    window.close()
    return resultado