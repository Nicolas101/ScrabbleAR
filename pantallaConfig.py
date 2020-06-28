import PySimpleGUI as sg 

nivel_facil = [
    [sg.Text("FÁCIL",background_color="#71B3BD",font=("Courier",22),pad=((0,0),(0,8)))],
    [sg.Button("Tiempo",tooltip="Limite de tiempo máximo de juego en este nivel.  \nHaga click para modificar"),sg.Text("*Predeterminado*",background_color="#71B3BD",text_color="#767676")],
    [sg.Button("Puntaje",tooltip="Puntaje por letra en este nivel.  \nHaga click para modificar"),sg.Text("*Predeterminado*",background_color="#71B3BD",text_color="#767676")],
    [sg.Button("Fichas",tooltip="Cantidad de fichas por letra en este nivel.  \nHaga click para modificar"),sg.Text("*Predeterminado*",background_color="#71B3BD",text_color="#767676")]
]

nivel_medio = [
    [sg.Text("MEDIO",background_color="#71B3BD",font=("Courier",22),pad=((0,0),(0,8)))],
    [sg.Button("Tiempo",tooltip="Limite de tiempo máximo de juego en este nivel.  \nHaga click para modificar"),sg.Text("*Predeterminado*",background_color="#71B3BD",text_color="#767676")],
    [sg.Button("Puntaje",tooltip="Puntaje por letra en este nivel.  \nHaga click para modificar"),sg.Text("*Predeterminado*",background_color="#71B3BD",text_color="#767676")],
    [sg.Button("Fichas",tooltip="Cantidad de fichas por letra en este nivel.  \nHaga click para modificar"),sg.Text("*Predeterminado*",background_color="#71B3BD",text_color="#767676")]
]

nivel_dificil = [
    [sg.Text("DIFÍCIL",background_color="#71B3BD",font=("Courier",22),pad=((0,0),(0,8)))],
    [sg.Button("Tiempo",tooltip="Limite de tiempo máximo de juego en este nivel.  \nHaga click para modificar"),sg.Text("*Predeterminado*",background_color="#71B3BD",text_color="#767676")],
    [sg.Button("Puntaje",tooltip="Puntaje por letra en este nivel.  \nHaga click para modificar"),sg.Text("*Predeterminado*",background_color="#71B3BD",text_color="#767676")],
    [sg.Button("Fichas",tooltip="Cantidad de fichas por letra en este nivel.  \nHaga click para modificar"),sg.Text("*Predeterminado*",background_color="#71B3BD",text_color="#767676")]
]

layout = [
    [sg.Text("Configuración del juego",background_color="#71B3BD",font=("Fixedsys",30),pad=((0,0),(30,50)))],
    [sg.Column(nivel_facil,background_color="#71B3BD",element_justification="center",pad=((50,0),(0,0))),sg.VerticalSeparator(pad=(20,0)),sg.Column(nivel_medio,background_color="#71B3BD",element_justification="center",pad=(0,0)),sg.VerticalSeparator(pad=(20,0)),sg.Column(nivel_dificil,background_color="#71B3BD",element_justification="center",pad=(0,0))],
    [sg.Button("Nivel personalizado",size=(18,1),font=("Arial",16),pad=((0,0),(50,50)))],
    [sg.Button("Guardar",size=(18,1),pad=((500,0),(0,0)))],
    [sg.Button("Volver",key="-BACK-",size=(18,1),pad=((0,350),(0,0))),sg.Button("Restaurar valores",size=(18,1),pad=((0,0),(5,0)))]
    ]
pantalla_config = sg.Window('Configuración',layout,size=(725,480),background_color="#71B3BD",element_justification="center")

def main():
    
    pantalla_config.UnHide()
    while True:
        event, values = pantalla_config.read()
        if event in (None,"-BACK-"):
            break
    
    pantalla_config.Hide()
    #pantalla_config.close()

if __name__ == "__main__":
    main()    