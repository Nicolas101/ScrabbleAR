def main():
    """Muestra la ventana de Como Jugar
    """
    from Windows import windowComoJugar

    window = windowComoJugar.hacer_ventana()

    event,values =window.read()

    window.close()