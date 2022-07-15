'''
Para la función definida en el siguiente código, encuentre una implementación alternativa que
permita implementar la misma función pero reduciendo las 7 líneas del cuerpo de su definición a un cuerpo
de sólo 2 líneas.

def some_function(first_word, second_word, third_word, fourth_word):
 name = first_word
 last_name = second_word
 age = third_word
 profession = fourth_word
 print('Name: ', name, last_name)
 print('Age: ', age, 'years')
 print('Profession:', profession)

'''
def some_function(first_word, second_word, third_word, fourth_word):
    return print('Name:', first_word, second_word, '\nAge:',third_word,'years','\nProfession:',fourth_word)
 