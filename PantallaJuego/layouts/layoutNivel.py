import PySimpleGUI as sg

def crearLayout(window_size):
    layout_selec_nivel = [
    [sg.Text("¿Qué nivel deseas jugar?",background_color="#71B3BD",font=("Fixedsys",34),pad=((30,30),(150,50)))],
    [sg.Button("Fácil",key="-FACIL-",size=(18,1),font=("Arial",18),pad=((0,15),(0,15))),sg.Button("Medio",key="-MEDIO-",size=(18,1),font=("Arial",18),pad=((0,0),(0,15)))],
    [sg.Button("Dificil",key="-DIFICL-",size=(18,1),font=("Arial",18),pad=((0,15),(0,0))),sg.Button("Personalizado",key="-PERSONALIZADO-",size=(18,1),font=("Arial",18),pad=((0,0),(0,0)))],
    ]
    pantalla_selec_nivel = sg.Window("ScrabbleAR - Selección de nivel",layout_selec_nivel,size=window_size,background_color="#71B3BD",element_justification="center")
    return pantalla_selec_nivel