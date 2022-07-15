'''
Programar una función que retorne True si un password (string) cumple con los siguientes
requisitos:
Tiene que tener por lo menos una letra minúscula.
Tiene que tener por lo menos una letra mayúscula.
Tiene que tener por lo menos un número.
Tiene que tener por lo menos un signo no alfanumérico (p.ej. ! ó $).
Tiene que tener entre 8 y 31 caracteres.
'''
contra = input('Ingrese la contraseña: ')
def password(contra: str) -> bool:
    M,m,num,sig, = 0,0,0,0
    if len(contra) >= 8 and len(contra) <= 31:
        for i in contra:
            if i.islower() == True:
                m += 1
            if i.isupper() == True:
                M += 1
            if i.isnumeric() == True:
                num += 1
            if i.isalnum() == False:
                sig += 1
        if m > 0 and M > 0 and num > 0 and sig > 0:
            return True
        else:
            return False
    else:
        return False
print(password(contra))
                
                
                