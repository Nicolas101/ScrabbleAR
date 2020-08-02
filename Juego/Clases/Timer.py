import time

class Timer():
    """
    """
    def __init__(self,limite,segundos=0,minutos=0):
        self._inicio = None 
        self._segundos = segundos
        self._minutos = minutos
        self._limite = limite
        self._hora_pausada = None
        self._termine = None
        self._ultima_actualizacion = None

    def iniciarTimer(self):
        self._inicio = time.time() - self._segundos
        self._termine = False

    def actualizarTimer(self):
        self._segundos = int(time.time() - self._inicio) - self._minutos*60
        if self._segundos == 60:
            self._minutos += 1
            self._segundos = 00
        if self._minutos == self._limite:
            self._termine = True
        self._ultima_actualizacion = time.time()

    def tiempoActual(self):
        """Retorna el tiempo actual del timer
        """
        return str(self._minutos)+":"+str(self._segundos)

    def termino(self):
        return self._termine

    def pausar(self):
        self._hora_pausada = time.time()

    def reanudar(self):
        self._inicio += time.time() - self._hora_pausada

    def ajustarTiempo(self):
        if time.time() - self._ultima_actualizacion != 0.0:
            time.sleep(time.time() - self._ultima_actualizacion)

    def getSegundos(self):
        return self._segundos

    def getMinutos(self):
        return self._minutos

    def getTiempoLimite(self):
        return self._limite