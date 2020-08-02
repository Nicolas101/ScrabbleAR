def hacer_ventana():
    import PySimpleGUI as sg

    layout = [
        [sg.Button('Reanudar',key='-REANUDAR-'),sg.Button('Salir sin guardar',key='-SALIR_SIN_GUARDAR-'),sg.Button('Guardar y salir',key='-SALIR_Y_GUARDAR-')],
    ]

    window = sg.Window("Pausa",layout,size=(500,400))

    return window