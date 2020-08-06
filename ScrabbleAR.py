from Windows import windowMenu
from Juego import mainJuego, seleccionarNivel, variablesDeJuego, partidaGuardada
from Configuracion import mainConfig
import verificarArchivos, topDiez

verificarArchivos.verificar()

window_menu = windowMenu.hacer_ventana()

while True:
    event,values = window_menu.read()
    
    #********************************* CERRAR LA VENTANA *********************************
    if event in (None,"-SALIR-"):
        break
    
    #********************************* CLICK EN JUGAR *********************************
    elif event == "-JUGAR-":
        if partidaGuardada.hay_partida_guardada(): #Si hay una partida guardada:

            if partidaGuardada.continuar_partida(): #Si quiere continuar con la partida guardada:
                #Cargo los datos de la partida guardada
                nivel, datos = partidaGuardada.obtener_datos()
                variables_juego = variablesDeJuego.cargar_variables(nivel, datos)

            else: #Si no quiere continuar con la partida guardada:
                #Guardo los datos y el nivel elegido para jugar
                nivel, datos = seleccionarNivel.seleccionar_nivel() 
                if nivel != None: variables_juego = variablesDeJuego.crear_variables(nivel,datos['letras'],datos['tiempo'])

            partidaGuardada.eliminar_partida()    
        
        else: #Si no hay una partida guardada:
            nivel, datos = seleccionarNivel.seleccionar_nivel() #Guardo los datos y el nivel elegido para jugar
            if nivel != None: variables_juego = variablesDeJuego.crear_variables(nivel,datos['letras'],datos['tiempo'])

        if nivel != None: #Si estan todos los datos para jugar:
            window_menu.Hide()
            juego_terminado, datos_de_partida = mainJuego.start_game(nivel,variables_juego)

            if juego_terminado: #Si se finalizo la partida:
                #Guardo el puntaje en TOP10
                topDiez.nuevo_puntaje(datos_de_partida)

            elif datos_de_partida[0]: #Si no se finalizo la partida y se tiene que guardar:
                partidaGuardada.guardar_partida(datos_de_partida)

        window_menu.UnHide()

    #********************************* CLICK EN CONFIGURACION *********************************
    elif event == "-CONFIGURACION-":
        window_menu.Hide()
        mainConfig.mostrar_configuracion()
        window_menu.UnHide()

window_menu.close()



