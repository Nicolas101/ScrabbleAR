def calcular_puntaje_final(puntaje_maquina,restar_maquina,puntaje_usuario,restar_usuario):
    """Resta al usuario y la maquina el valor de las fichas que les quedaron y devuelve el ganador
    """
    total_usuario = puntaje_usuario-restar_usuario
    total_maquina = puntaje_maquina-restar_maquina
    
    if (total_usuario>total_maquina):
        ganador = 'Usuario'
    elif (total_maquina>total_usuario):
        ganador = 'Maquina'
    else:
        ganador = 'Empate'

    return [ganador, total_maquina, total_usuario]

def main(puntaje_maquina,restar_maquina,letras_maquina, puntaje_usuario,restar_usuario,letras_usuario,game_over_text):

    from Windows import windowPartidaTerminada,windowJuegoFinal
    window = windowPartidaTerminada.hacer_ventana(letras_maquina,letras_usuario,game_over_text)

    event, values = window.read()
    #Clickea si o si sobre Calcular puntaje

    ganador,total_maquina,total_usuario = calcular_puntaje_final(puntaje_maquina,restar_maquina,puntaje_usuario,restar_usuario)

    if ganador == "Usuario":
        window_final = windowJuegoFinal.hacer_ventana(r"Data\Images\Juego\Partida-terminada\Ventana-final\ganaste.png",total_maquina,puntaje_maquina,restar_maquina,total_usuario,puntaje_usuario,restar_usuario)
    elif ganador == "Maquina":
        window_final = windowJuegoFinal.hacer_ventana(r"Data\Images\Juego\Partida-terminada\Ventana-final\perdiste.png",total_maquina,puntaje_maquina,restar_maquina,total_usuario,puntaje_usuario,restar_usuario)
    else: 
        window_final = windowJuegoFinal.hacer_ventana(r"Data\Images\Juego\Partida-terminada\Ventana-final\empate.png",total_maquina,puntaje_maquina,restar_maquina,total_usuario,puntaje_usuario,restar_usuario)

    event_final, values_final = window_final.read()

    window_final.close()
    window.close()

    return total_usuario


