def hacer_ventana():
    import PySimpleGUI as sg

    layout=[
        [sg.Text('Hay una partida guardada, desea continuarla?')],
        [sg.Button('Si',key='-SI-'),sg.Button('No',key='-NO-')]
    ]

    return sg.Window('Partida guardada',layout,disable_close=True)