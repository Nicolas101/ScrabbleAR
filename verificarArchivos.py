def verificar():
    """Verifica que existan los archivos necesarios para que el programa funcione
    """
    import os
    import json

    def crear_archivo_facil(ubicacion_archivo):
        """Crea el archivo facil.json
        """
        import json
        
        archivo = open(ubicacion_archivo,'w')

        dic_fichas = {'A':{'puntuacion':1,'cantidad':11},'B':{'puntuacion':3,'cantidad':3},'C':{'puntuacion':2,'cantidad':4},
                    'D':{'puntuacion':2,'cantidad':4},'E':{'puntuacion':1,'cantidad':11},'F':{'puntuacion':4,'cantidad':2},
                    'G':{'puntuacion':2,'cantidad':2},'H':{'puntuacion':4,'cantidad':2},'I':{'puntuacion':1,'cantidad':6},
                    'J':{'puntuacion':6,'cantidad':2},'K':{'puntuacion':8,'cantidad':1},'L':{'puntuacion':1,'cantidad':4},
                    'M':{'puntuacion':3,'cantidad':3},'N':{'puntuacion':1,'cantidad':5},'Ñ':{'puntuacion':8,'cantidad':1},
                    'O':{'puntuacion':1,'cantidad':8},'P':{'puntuacion':3,'cantidad':2},'Q':{'puntuacion':8,'cantidad':1},
                    'R':{'puntuacion':1,'cantidad':4},'S':{'puntuacion':1,'cantidad':7},'T':{'puntuacion':1,'cantidad':4},
                    'U':{'puntuacion':1,'cantidad':6},'V':{'puntuacion':4,'cantidad':2},'W':{'puntuacion':8,'cantidad':1},
                    'X':{'puntuacion':8,'cantidad':1},'Y':{'puntuacion':4,'cantidad':1},'Z':{'puntuacion':10,'cantidad':1}}

        tiempo = 7

        datos = [{'letras':dic_fichas,
                'tiempo':tiempo}]
        
        json.dump(datos,archivo,indent=4)

        archivo.close()

    def crear_archivo_medio(ubicacion_archivo):
        """Crea el archivo medio.json
        """
        import json
        
        archivo = open(ubicacion_archivo,'w')

        dic_fichas = {'A':{'puntuacion':1,'cantidad':11},'B':{'puntuacion':3,'cantidad':3},'C':{'puntuacion':2,'cantidad':4},
                    'D':{'puntuacion':2,'cantidad':4},'E':{'puntuacion':1,'cantidad':11},'F':{'puntuacion':4,'cantidad':2},
                    'G':{'puntuacion':2,'cantidad':2},'H':{'puntuacion':4,'cantidad':2},'I':{'puntuacion':1,'cantidad':6},
                    'J':{'puntuacion':6,'cantidad':2},'K':{'puntuacion':8,'cantidad':1},'L':{'puntuacion':1,'cantidad':4},
                    'M':{'puntuacion':3,'cantidad':3},'N':{'puntuacion':1,'cantidad':5},'Ñ':{'puntuacion':8,'cantidad':1},
                    'O':{'puntuacion':1,'cantidad':8},'P':{'puntuacion':3,'cantidad':2},'Q':{'puntuacion':8,'cantidad':1},
                    'R':{'puntuacion':1,'cantidad':4},'S':{'puntuacion':1,'cantidad':7},'T':{'puntuacion':1,'cantidad':4},
                    'U':{'puntuacion':1,'cantidad':6},'V':{'puntuacion':4,'cantidad':2},'W':{'puntuacion':8,'cantidad':1},
                    'X':{'puntuacion':8,'cantidad':1},'Y':{'puntuacion':4,'cantidad':1},'Z':{'puntuacion':10,'cantidad':1}}

        tiempo = 10

        datos = [{'letras':dic_fichas,
                'tiempo':tiempo}]
        
        json.dump(datos,archivo,indent=4)

        archivo.close()

    def crear_archivo_dificil(ubicacion_archivo):
        """Crea el archivo dificil.json
        """
        import json
        
        archivo = open(ubicacion_archivo,'w')

        dic_fichas = {'A':{'puntuacion':1,'cantidad':11},'B':{'puntuacion':3,'cantidad':3},'C':{'puntuacion':2,'cantidad':4},
                    'D':{'puntuacion':2,'cantidad':4},'E':{'puntuacion':1,'cantidad':11},'F':{'puntuacion':4,'cantidad':2},
                    'G':{'puntuacion':2,'cantidad':2},'H':{'puntuacion':4,'cantidad':2},'I':{'puntuacion':1,'cantidad':6},
                    'J':{'puntuacion':6,'cantidad':2},'K':{'puntuacion':8,'cantidad':1},'L':{'puntuacion':1,'cantidad':4},
                    'M':{'puntuacion':3,'cantidad':3},'N':{'puntuacion':1,'cantidad':5},'Ñ':{'puntuacion':8,'cantidad':1},
                    'O':{'puntuacion':1,'cantidad':8},'P':{'puntuacion':3,'cantidad':2},'Q':{'puntuacion':8,'cantidad':1},
                    'R':{'puntuacion':1,'cantidad':4},'S':{'puntuacion':1,'cantidad':7},'T':{'puntuacion':1,'cantidad':4},
                    'U':{'puntuacion':1,'cantidad':6},'V':{'puntuacion':4,'cantidad':2},'W':{'puntuacion':8,'cantidad':1},
                    'X':{'puntuacion':8,'cantidad':1},'Y':{'puntuacion':4,'cantidad':1},'Z':{'puntuacion':10,'cantidad':1}}

        tiempo = 12

        datos = [{'letras':dic_fichas,
                'tiempo':tiempo}]
        
        json.dump(datos,archivo,indent=4)

        archivo.close()

    lis_archivos = ['Facil.json','Medio.json','Dificil.json']
    dir_actual = os.getcwd()
    for archivo in lis_archivos:
        #intenta leer los archivos de lis_archivos, si alguno no existe lo crea
        try:
            ubicacion_archivo = (dir_actual+'\\Data\\Files\\'+archivo)
            f = open(ubicacion_archivo,'r')
            f.close()
        except FileNotFoundError:
            if archivo == 'Facil.json':
                crear_archivo_facil(ubicacion_archivo)
            elif archivo == 'Medio.json':
                crear_archivo_medio(ubicacion_archivo)
            elif archivo == 'Dificil.json':
                crear_archivo_dificil(ubicacion_archivo)