import PySimpleGUI as sg
import random

def hacer_tablero(casillas_especiales,tablero):
    def hacer_fila(num_fila,casillas_especiales,tamanio):
        lis = []
        keys = []
        for i in range(0,tamanio):
            nom=str(num_fila)+"-"+str(i)
            if (nom in casillas_especiales["+2"]):
                lis.append(sg.Button("+2",key=nom,pad=(0,0),size=(3,1),disabled=True,button_color=('black','#2283BB'),disabled_button_color=('black','#2283BB')))
            elif (nom in casillas_especiales["+3"]):
                lis.append(sg.Button("+3",key=nom,pad=(0,0),size=(3,1),disabled=True,button_color=('black','#45BB22'),disabled_button_color=('black','#45BB22')))
            elif(nom in casillas_especiales["-1"]):
                lis.append(sg.Button("-1",key=nom,pad=(0,0),size=(3,1),disabled=True,button_color=('black','#F0B121'),disabled_button_color=('black','#F0B121')))
            elif(nom in casillas_especiales["-2"]):
                lis.append(sg.Button("-2",key=nom,pad=(0,0),size=(3,1),disabled=True,button_color=('black','#F06C21'),disabled_button_color=('black','#F06C21')))
            elif(nom in casillas_especiales["-3"]):
                lis.append(sg.Button("-3",key=nom,pad=(0,0),size=(3,1),disabled=True,button_color=('black','#F02121'),disabled_button_color=('black','#F02121')))
            else:            
                lis.append(sg.Button(" ",key=str(num_fila)+"-"+str(i),pad=(0,0),size=(3,1),disabled=True,disabled_button_color=('black','white'),button_color=('black','white')))
            keys.append(str(num_fila)+"-"+str(i))
        
        return (lis,keys) 
    if tablero == 1:
        tamanio = 15
    elif tablero == 2:
        tamanio = 20
    else:
        tamanio = 18
    lis = []
    keys = []
    for i in range(0,tamanio):
        valores = hacer_fila(i,casillas_especiales,tamanio)
        lis.append(valores[0])   
        keys = keys + valores[1]

    return (lis,keys,tamanio)

def elijo_tablero():
    return random.randint(1,3)


def main():
    tablero=elijo_tablero()
    casillas_especiales1={"+2":["1-5","1-9","5-1","5-13","6-6","6-8","8-6","8-8","9-1","9-13","13-5","13-9"],
                    "+3":["0-3","0-11","2-6","2-8","3-0","3-7","3-14","6-2","6-12","7-3","7-11","8-2","8-12","11-0","11-14","11-7","12-6","12-8","14-3"],
                    "-3":["0-0","0-7","0-14","7-0","7-14","14-0","14-7","14-14"],
                    "-2":["1-1","1-13","2-2","2-12","12-2","12-12","13-1","13-13"],
                    "-1":["3-3","3-11","4-4","4-10","5-5","5-9","9-5","9-9","10-4","10-10","11-3","11-11"]}
        
    return hacer_tablero(casillas_especiales1,tablero)