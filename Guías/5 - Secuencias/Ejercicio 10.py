'''
El cifrado César es un tipo de cifrado de mensajes que se basa en intercambiar unas letras por otras,
segun un desplazamiento, como se muestra en la figura a continuación:

En este cifrado, se toman todas las letras que se van a utilizar, por ejemplo, de la A a la Z y de la a a la z.
Luego, se define una rotación, un número que utilizaremos para desplazar cada letra, por ejemplo, en la
figura es 3. De ese modo, la A se convertirá en una D, la B en E, la C en F, la X en A, la Y en B y la Z en C.

Implemente dos funciones, una para cifrar y una para descifrar un mensaje. Para probar el funcionamiento,
considere que decipher(cipher(msg)) devuelve el mensaje original. La siguiente tabla contiene
ejemplos de cifrados.
'''
def cipher(msg,lugares):
    new_msg = ''
    for i in msg:
        if i .isupper():
            msg_crip = chr((ord(i) + lugares - 65) % 26 + 65)
            new_msg += msg_crip
        elif i .islower():
            msg_crip = chr((ord(i) + lugares - 97) % 26 + 97)
            new_msg += msg_crip
        else:
            new_msg += i
    return new_msg

def decipher(msg,lugares):
    new_msg = ''
    for i in msg:
        if i .isupper():
            msg_crip = chr((ord(i) - lugares - 65) % 26 + 65)
            new_msg += msg_crip
        elif i .islower():
            msg_crip = chr((ord(i) - lugares - 97) % 26 + 97)
            new_msg += msg_crip
        else:
            new_msg += i
    return new_msg
