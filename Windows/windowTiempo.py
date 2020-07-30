def hacer_ventanta(valor_por_defecto):
    import PySimpleGUI as sg

    lis_values = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    layout = [
        [sg.Text('Tiempo')],
        [sg.Listbox(lis_values,default_values=[valor_por_defecto], key='Listbox',size=(5,5))],
        [sg.Button('Ok'),sg.Button('Cancelar')]
    ]

    return sg.Window('Tiempo',layout)