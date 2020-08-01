from Windows import windowMenu
from Juego import mainJuego, selecNivel
from Configuracion import mainConfig
import topDiez
import verificarArchivos

verificarArchivos.verificar()

window_menu = windowMenu.hacer_ventana((1000,600))

while True:
    event,values = window_menu.read()
    if event in (None,"-SALIR-"):
        break

    elif event == "-PLAY-":
        window_menu.Hide()
        nivel, datos = selecNivel.seleccionar_nivel()
        juego_terminado, datos_de_partida = mainJuego.start_game(nivel,datos)
        if juego_terminado:
            topDiez.nuevo_puntaje(datos_de_partida)
            pass
        else:
            if datos_de_partida[0]:#si se debe guardar la partida el primer elemento va a ser true
                #guardar_partida()
                pass
            pass
        window_menu.UnHide()

    elif event == "-CONFIG-":
        window_menu.Hide()
        mainConfig.mostrar_configuracion()
        window_menu.UnHide()

window_menu.close()



