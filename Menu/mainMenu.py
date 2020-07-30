def mostrar_menu():

    from Menu import windowMenu
    window_menu = windowMenu.hacer_ventana((1000,600))

    from Juego import mainJuego,selecNivel
    from Configuracion import mainConfig

    while True:
        event,values = window_menu.read()
        if event in (None,"-SALIR-"):
            break

        elif event == "-PLAY-":
            window_menu.Hide()
            nivel, datos = selecNivel.seleccionar_nivel()
            mainJuego.start_game(nivel,datos)
            window_menu.UnHide()

        elif event == "-CONFIG-":
            window_menu.Hide()
            mainConfig.mostrar_configuracion()
            window_menu.UnHide()

    window_menu.close()

if __name__ == "__main__":
    mostrar_menu()
