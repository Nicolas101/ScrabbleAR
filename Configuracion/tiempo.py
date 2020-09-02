def ejecutar(valor_por_defecto,nivel):
    """Despliega la ventana que permite decidir cuanto tiempo durará la partida
    """
    if nivel == 'facil':
        lis_values = [1,2,3,4,5,6,7,8,9,10]
    elif nivel == 'medio':
        lis_values = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    else:
        lis_values = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

    from Windows import windowTiempo
    window = windowTiempo.hacer_ventanta(valor_por_defecto,lis_values)

    while True:
        event,values = window.Read()

        if event in [None,'-CANCELAR-']:
            resultado = None
            break

        elif event == '-CONFIRMAR-':
            resultado = values['Listbox'][0]
            break

    window.Close()
    return resultado
