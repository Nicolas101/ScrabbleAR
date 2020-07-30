def hacer_ventana(diccionario,categoria,clave):
    import PySimpleGUI as sg
    
    
    lis_values=[1,2,3,4,5,6,7,8,9,10,11]
    layout=[
        [sg.Text('A'),sg.Listbox(lis_values,key='A',default_values=[diccionario['A'][clave]]),sg.Text('B'),sg.Listbox(lis_values,key='B',default_values=[diccionario['B'][clave]]),sg.Text('C'),sg.Listbox(lis_values,key='C',default_values=[diccionario['C'][clave]])],
        [sg.Text('D'),sg.Listbox(lis_values,key='D',default_values=[diccionario['D'][clave]]),sg.Text('E'),sg.Listbox(lis_values,key='E',default_values=[diccionario['E'][clave]]),sg.Text('F'),sg.Listbox(lis_values,key='F',default_values=[diccionario['F'][clave]])],
        [sg.Text('G'),sg.Listbox(lis_values,key='G',default_values=[diccionario['G'][clave]]),sg.Text('H'),sg.Listbox(lis_values,key='H',default_values=[diccionario['H'][clave]]),sg.Text('I'),sg.Listbox(lis_values,key='I',default_values=[diccionario['I'][clave]])],
        [sg.Text('J'),sg.Listbox(lis_values,key='J',default_values=[diccionario['J'][clave]]),sg.Text('K'),sg.Listbox(lis_values,key='K',default_values=[diccionario['K'][clave]]),sg.Text('L'),sg.Listbox(lis_values,key='L',default_values=[diccionario['L'][clave]])],
        [sg.Text('M'),sg.Listbox(lis_values,key='M',default_values=[diccionario['M'][clave]]),sg.Text('N'),sg.Listbox(lis_values,key='N',default_values=[diccionario['N'][clave]]),sg.Text('Ñ'),sg.Listbox(lis_values,key='Ñ',default_values=[diccionario['Ñ'][clave]])],
        [sg.Text('O'),sg.Listbox(lis_values,key='O',default_values=[diccionario['O'][clave]]),sg.Text('P'),sg.Listbox(lis_values,key='P',default_values=[diccionario['P'][clave]]),sg.Text('Q'),sg.Listbox(lis_values,key='Q',default_values=[diccionario['Q'][clave]])],
        [sg.Text('R'),sg.Listbox(lis_values,key='R',default_values=[diccionario['R'][clave]]),sg.Text('S'),sg.Listbox(lis_values,key='S',default_values=[diccionario['S'][clave]]),sg.Text('T'),sg.Listbox(lis_values,key='T',default_values=[diccionario['T'][clave]])],
        [sg.Text('U'),sg.Listbox(lis_values,key='U',default_values=[diccionario['U'][clave]]),sg.Text('V'),sg.Listbox(lis_values,key='V',default_values=[diccionario['V'][clave]]),sg.Text('W'),sg.Listbox(lis_values,key='W',default_values=[diccionario['W'][clave]])],
        [sg.Text('X'),sg.Listbox(lis_values,key='X',default_values=[diccionario['X'][clave]]),sg.Text('Y'),sg.Listbox(lis_values,key='Y',default_values=[diccionario['Y'][clave]]),sg.Text('Z'),sg.Listbox(lis_values,key='Z',default_values=[diccionario['Z'][clave]])],
        [sg.Button('Ok'),sg.Button('Cancelar')]
    ]

    return sg.Window(categoria,layout)

