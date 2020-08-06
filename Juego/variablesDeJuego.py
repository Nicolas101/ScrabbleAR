def crear_variables(nivel, letras, tiempo_limite):
    """Crea y retorna todas las variables para la partida 
    """
    from Juego.Clases.BolsaFichas import crear_bolsa
    from Juego.Clases.Tablero import crear_tablero
    from Juego.Clases.FilaDeFichas import crear_fichas
    from Juego.Clases.Jugador import Jugador
    from Juego.Clases.Maquina import Maquina
    from Juego.Clases.Timer import Timer
    from Windows import windowJuego
    import random
    
    variables = {}

    variables["Bolsa_de_fichas"] = crear_bolsa(letras)

    variables["Tablero"] = crear_tablero(variables["Bolsa_de_fichas"])

    variables["Fichas_jugador"] = crear_fichas(variables["Bolsa_de_fichas"].letras_random(7),False)
    variables["Fichas_maquina"] = crear_fichas(variables["Bolsa_de_fichas"].letras_random(7),True)

    variables["Usuario"] = Jugador()
    variables["Maquina"] = Maquina()

    variables["Timer"] = Timer(tiempo_limite)

    variables["Turno"] = random.randint(0,1) # 0: turno del usuario // 1: turno del oponente

    if variables["Turno"] == 0 :
        variables["Confirmar_habilitado"] = True
        variables["Cambiar_habilitado"] = True
    else:
        variables["Confirmar_habilitado"] = False
        variables["Cambiar_habilitado"] = False

    tipos_verbos = ['VB','VBD','VBG','VBN','VBP','VBZ']
    tipos_adjetivos = ['DT','JJ','JJR','JJS','RB','RBR','RBS']

    if nivel == '-DIFICIL-':
        variables["Clases_validas"] = random.choice([tipos_verbos,tipos_adjetivos])
    elif nivel == '-MEDIO-':
        variables["Clases_validas"] = tipos_verbos+tipos_adjetivos
    else:
        variables["Clases_validas"] = None

    variables["Window_juego"] = windowJuego.hacer_ventana(
        variables["Tablero"].getLayout(),
        variables["Fichas_jugador"].getLayout(),
        variables["Fichas_maquina"].getLayout(),
        variables["Usuario"].getPuntaje(),
        variables["Maquina"].getPuntaje(),
        "","",
        nivel,
        variables["Clases_validas"])

    return variables
    

def cargar_variables(datos):
    """Carga y retorna las variables de la partida con los datos guardados anteriormente
    """
    from Juego.Clases.Timer import Timer
    from Windows import windowJuego
    variables = {}

    variables["Bolsa_de_fichas"] = datos[1]

    variables["Tablero"] = datos[2]

    variables["Fichas_jugador"] = datos[3]
    variables["Fichas_maquina"] = datos[4]

    variables["Usuario"] = datos[5]
    variables["Maquina"] = datos[6]
        
    variables["Timer"] = Timer(datos[9],datos[7],datos[8])

    variables["Turno"] = datos[10]

    variables["Confirmar_habilitado"] = datos[11]
    variables["Cambiar_habilitado"] = datos[12]

    variables["Clases_validas"] = datos[13]

    variables["Window_juego"] = windowJuego.hacer_ventana(
        variables["Tablero"].getLayoutActualizado(),
        variables["Fichas_jugador"].getLayoutActualizado(),
        variables["Fichas_maquina"].getLayoutActualizado(),
        variables["Usuario"].getPuntaje(),
        variables["Maquina"].getPuntaje(),
        variables["Usuario"].getPalabras(),
        variables["Maquina"].getPalabras(),
        datos[14],
        variables["Clases_validas"]
    )

    return variables