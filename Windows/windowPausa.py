def hacer_ventana():
    import PySimpleGUI as sg

    layout = [
        [sg.Button('Reanudar'),sg.Button('Salir sin guardar'),sg.Button('Guardar y salir')],
    ]

    window = sg.Window("Pausa",layout,size=(500,400))

    return window