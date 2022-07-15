'''
 En ciertos casos resulta necesario interrumpir abruptamente un programa cuando queda
atrapado en un ciclo infinito. ¿Cómo puede interrumpirse un programa desde la consola de Python
interactivo? Pruebe interrumpir el siguiente programa (no lo corra antes de saber cómo terminar un
programa).
import time
'''
import time
counter = 0
while True:
 counter += 1
 print("I'm Mr. Meeseeks, look at me", '!' * counter)
 time.sleep(1)
 
 