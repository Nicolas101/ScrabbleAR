def mostrar_configuracion():   
    from Configuracion import windowConfig
    window_config = windowConfig.hacer_ventana((1000,600))

    while True:
        event, values = window_config.read()
        if event in (None,"-BACK-"):
            break

    window_config.close()

if __name__ == "__main__":
    mostrar_configuracion()   