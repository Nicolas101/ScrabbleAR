import PySimpleGUI as sg

#'Black', 'BlueMono', 'BluePurple', 'BrightColors', 'BrownBlue', 'Dark', 'Dark2', 'DarkAmber', 'DarkBlack', 'DarkBlack1', 'DarkBlue', 'DarkBlue1', 'DarkBlue10', 'DarkBlue11', 'DarkBlue12',
#'DarkBlue13', 'DarkBlue14', 'DarkBlue15', 'DarkBlue16', 'DarkBlue17', 'DarkBlue2', 'DarkBlue3', 'DarkBlue4', 'DarkBlue5', 'DarkBlue6', 'DarkBlue7', 'DarkBlue8', 'DarkBlue9', 'DarkBrown',
#'DarkBrown1', 'DarkBrown2', 'DarkBrown3', 'DarkBrown4', 'DarkBrown5', 'DarkBrown6', 'DarkGreen', 'DarkGreen1', 'DarkGreen2', 'DarkGreen3', 'DarkGreen4', 'DarkGreen5', 'DarkGreen6', 'DarkGrey',
#'DarkGrey1', 'DarkGrey2', 'DarkGrey3', 'DarkGrey4', 'DarkGrey5', 'DarkGrey6', 'DarkGrey7', 'DarkPurple', 'DarkPurple1', 'DarkPurple2', 'DarkPurple3', 'DarkPurple4', 'DarkPurple5', 'DarkPurple6',
#'DarkRed', 'DarkRed1', 'DarkRed2', 'DarkTanBlue', 'DarkTeal', 'DarkTeal1', 'DarkTeal10', 'DarkTeal11', 'DarkTeal12', 'DarkTeal2', 'DarkTeal3', 'DarkTeal4', 'DarkTeal5', 'DarkTeal6', 'DarkTeal7', 
#'DarkTeal8', 'DarkTeal9', 'Default', 'Default1', 'DefaultNoMoreNagging', 'Green', 'GreenMono', 'GreenTan', 'HotDogStand', 'Kayak', 'LightBlue', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
#'LightBlue5', 'LightBlue6', 'LightBlue7', 'LightBrown', 'LightBrown1', 'LightBrown10', 'LightBrown11', 'LightBrown12', 'LightBrown13', 'LightBrown2', 'LightBrown3', 'LightBrown4', 'LightBrown5', 'LightBrown6',
#'LightBrown7', 'LightBrown8', 'LightBrown9', 'LightGray1', 'LightGreen', 'LightGreen1', 'LightGreen10', 'LightGreen2', 'LightGreen3', 'LightGreen4', 'LightGreen5', 'LightGreen6', 'LightGreen7', 'LightGreen8',
#'LightGreen9', 'LightGrey', 'LightGrey1', 'LightGrey2', 'LightGrey3', 'LightGrey4', 'LightGrey5', 'LightGrey6', 'LightPurple', 'LightTeal', 'LightYellow', 'Material1', 'Material2', 'NeutralBlue', 'Purple', 'Reddit',
#'Reds', 'SandyBeach', 'SystemDefault', 'SystemDefault1', 'SystemDefaultForReal', 'Tan', 'TanBlue', 'TealMono', 'Topanga'

sg.theme(new_theme="DarkBrown1")
sg.theme_background_color(color='#362217')

def hacer_fila(num_fila,fichas_especiales):
    lis = []
    keys = []
    for i in range(0,15):
        nom=str(num_fila)+"-"+str(i)
        if (nom in fichas_especiales["+2"]):
            lis.append(sg.Button(" ",key=nom,pad=(0,0),size=(3,1),disabled=True,button_color=('black','#2283BB'),disabled_button_color=('black','#2283BB')))
        elif (nom in fichas_especiales["+3"]):
            lis.append(sg.Button(" ",key=nom,pad=(0,0),size=(3,1),disabled=True,button_color=('black','#45BB22'),disabled_button_color=('black','#45BB22')))
        elif(nom in fichas_especiales["-1"]):
            lis.append(sg.Button(" ",key=nom,pad=(0,0),size=(3,1),disabled=True,button_color=('black','#F0B121'),disabled_button_color=('black','#F0B121')))
        elif(nom in fichas_especiales["-2"]):
            lis.append(sg.Button(" ",key=nom,pad=(0,0),size=(3,1),disabled=True,button_color=('black','#F06C21'),disabled_button_color=('black','#F06C21')))
        elif(nom in fichas_especiales["-3"]):
            lis.append(sg.Button(" ",key=nom,pad=(0,0),size=(3,1),disabled=True,button_color=('black','#F02121'),disabled_button_color=('black','#F02121')))
        else:
            lis.append(sg.Button(" ",key=nom,pad=(0,0),size=(3,1),disabled=True,button_color=('black','#E5BE7D'),disabled_button_color=('black','#E5BE7D')))
        keys.append(str(num_fila)+"-"+str(i))
        
    return (lis,keys)
        
def hacer_tablero(fichas_especiales):
    lis = []
    keys = []
    for i in range(0,15):
        valores = hacer_fila(i,fichas_especiales)
        lis.append(valores[0])   
        keys=keys+valores[1]

    return (lis,keys)

def hacer_filafichasJ():
    lis = []
    for i in range(0,7):
        lis.append(sg.Button(str(i),key="f-"+str(i),pad=(0,0),size=(3,1)))
    return lis

def hacer_filafichasM():
    lis = []
    for i in range(0,7):
        lis.append(sg.Button(" ",key="f-"+str(i+100),pad=(0,0),disabled=True))
    return lis

def deshabilitar_tablero(pantalla_juego):
    for i in range(0,15):
        for x in range(0,15):
            key=str(i)+"-"+str(x)
            pantalla_juego[key].Update(disabled=True)

def habilitar_tablero(pantalla_juego):
    for i in range(0,15):
        for x in range(0,15):
            key=str(i)+"-"+str(x)
            pantalla_juego[key].Update(disabled=False)

def crear_bolsa():
    bolsa=[]
    #en proceso
    bolsa=['a','a','a','a','a','a','a','b','b','b','b','b',]
    
    return bolsa

fichas_especiales={"+2":["1-5","1-9","5-1","5-13","6-6","6-8","8-6","8-8","9-1","9-13","13-5","13-9"],
                    "+3":["0-3","0-11","2-6","2-8","3-0","3-7","3-14","6-2","6-12","7-3","7-11","8-2","8-12","11-0","11-14","11-7","12-6","12-8","14-3"],
                    "-3":["0-0","0-7","0-14","7-0","7-14","14-0","14-7","14-14"],
                    "-2":["1-1","1-13","2-2","2-12","12-2","12-12","13-1","13-13"],
                    "-1":["3-3","3-11","4-4","4-10","5-5","5-9","9-5","9-9","10-4","10-10","11-3","11-11"]}
bolsa=crear_bolsa()
valores_fichas=["f-0","f-1","f-2","f-3","f-4","f-5","f-6"]
valores_tablero= hacer_tablero(fichas_especiales)
keys_tablero=valores_tablero[1]
layout_tablero = valores_tablero[0]
layout_fichasMaquina = [hacer_filafichasM()]
layout_fichasJugador = [hacer_filafichasJ()]

layout = [  
    [sg.Column(layout_fichasMaquina,pad=((0,0),(0,20)))],
    [sg.Column(layout_tablero)],
    [sg.Column(layout_fichasJugador,pad=((0,0),(20,0)))]
]
pantalla_juego = sg.Window("Scrabble",layout)



dato_ficha=0
key_ficha=0
while True:
    event, values = pantalla_juego.read()
    print(event)
    if(event is None):
        break
    elif(event in keys_tablero and dato_ficha!=0): #llegamos hasta aca
        print("hola ma")
        pantalla_juego[event].Update(dato_ficha)
        pantalla_juego[key_ficha].Update(disabled=True)
        deshabilitar_tablero(pantalla_juego)
    elif (event in valores_fichas):
        habilitar_tablero(pantalla_juego)
        key_ficha=event
        dato_ficha=pantalla_juego[event].GetText()
        print(dato_ficha)
        print("prueba")

pantalla_juego.close() 