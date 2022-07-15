#%%
name = 'John'
def func1():
    print(name)
def greet (name:str)->str:
    return f'Hello, {name}'
def main():
   # name = 'Mike'
    print(greet(name))
if __name__ == '__main__':
    main()
#%%
#import_1
def is_positive(num: float):
    if num > 0:
        return True
    elif num <= 0:
        return False
if __name__ == '__main__':
    for i in range (0, 100):
        print("I'm running a lot of times!")
#import_2
from import_1 import is_positive

def main():
    print(is_positive(1))
    
if __name__ == '__main__': 
    main()
#%%
def age():
   father_age = int(input('How old the father is ? '))
   son_age = int(input('How old the son is ? '))
   how_many_years = abs(son_age * 2 - father_age)
   print("Father had the double of the son's age",how_many_years,"ago")
age()
#%%
def area():
    length = int(input('Ingrese el valor del largo: '))
    width = int(input('Ingrese el valor del ancho: '))
    if length == width:
        calculation = length * width
        print('El area de tu cuadrado es:',calculation)
    elif length != width:
        calculation2 = 2 * (length * width)
        print('El perimetro de tu rectangulo de:',calculation2)
area()
#%%