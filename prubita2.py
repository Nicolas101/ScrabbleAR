import time
inicio = time.monotonic()
fin = inicio + 30
#cont = 0 el tema del cont es para ver si cuando salgo y guardo me puedo quedar con el tiempo que faltaba para seguir desps
ok = True
while (time.monotonic()<fin):
    #if cont == 3:
    #  break
    #cont += 1
    if (fin-time.monotonic()<=15)and(ok):
        print('quedan 15 segundos')
        ok = False
    time.sleep(5)
#lo_que_quedaba = fin-time.monotonic()
#print(lo_que_quedaba)
print('fin')
