from Windows import windowMenu
from Juego import mainJuego, selecNivel
from Configuracion import mainConfig
import verificarArchivos, topDiez, partidaGuardada

verificarArchivos.verificar()

window_menu = windowMenu.hacer_ventana((1000,600))

while True:
    event,values = window_menu.read()
    if event in (None,"-SALIR-"):
        break

    elif event == "-PLAY-":
        window_menu.Hide()
        partida_guardada = partidaGuardada.hay_partida_guardada()
        if not partida_guardada:
            nivel, datos = selecNivel.seleccionar_nivel()
        else:
            nivel, datos = partidaGuardada.obtener_datos()
        juego_terminado, datos_de_partida = mainJuego.start_game(nivel,datos,partida_guardada)
        if juego_terminado:
            topDiez.nuevo_puntaje(datos_de_partida)
        elif datos_de_partida[0]:#si se debe guardar la partida el primer elemento va a ser true
            partidaGuardada.guardar_partida(datos_de_partida)
            print('ando')
        window_menu.UnHide()

    elif event == "-CONFIG-":
        window_menu.Hide()
        mainConfig.mostrar_configuracion()
        window_menu.UnHide()

window_menu.close()



