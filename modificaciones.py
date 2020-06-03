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

def hacer_fila(num_fila):
    lis = []
    keys = []
    for i in range(0,15):
        lis.append(sg.Button(" ",key=str(num_fila)+"-"+str(i),pad=(0,0),size=(3,1),disabled=True,button_color=('black','#E5BE7D'),disabled_button_color=('black','#E5BE7D')))
        keys.append(str(num_fila)+"-"+str(i))
        
    return (lis,keys)
        
def hacer_tablero():
    lis = []
    keys = []
    for i in range(0,15):
        valores = hacer_fila(i)
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
        lis.append(sg.Button(" ",key="f-"+str(i+100),pad=(0,0),disabled=True,image_filename="google.png",image_size=(30,25)))
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


bolsa=crear_bolsa()
valores_fichas=["f-0","f-1","f-2","f-3","f-4","f-5","f-6"]
valores_tablero= hacer_tablero()
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