"""
Funciones definidas por el usuario
"""

# Simple
def saludo():
    print("Hola, Python!")

saludo()

# Funciones con retorno
def return_greet():
    return "Hola, Python!"

print(return_greet())

# Con un argumento
def arg_greet(name):
    print(f"Hola, {name}!")

arg_greet("mau")

# Con argumentos
def args_greet(greet, name):
    print(f"{greet}, {name}!")

args_greet("Hi", "Mau")

# Con argumentos por defecto
def default_arg_greet(name="Python"):
    print(f"Hola, {name}!")

default_arg_greet()

# Con retorno de varios valores
def multiple_return():
    return "Hi", "Python"

greet, name = multiple_return()     # capturamos los valores retornados en 2 variables
print(greet)
print(name)

# con un numero variable de argumentos
def variable_arg_greet(*names):     # El asterisco le indica a la función que puede recibir mas de un argumento (estos deben de ir separados por comas)
    for name in names:
        print(f"Hola, {name}")

variable_arg_greet("Python", "Mau", "Comunidad")

# con un numero variable de argumentos pero con palabra clave
def variable_key_arg_greet(**names):     
    for key, value in names.items():
        print(f"{value} ({key})!")

variable_key_arg_greet(
    language="Python",
    name="Mauricio",
    alias="Mau",
    age=39
)

"""
Funciones dentro de funciones
"""

def outer_function():
    def inner_function():
        print("Función interna: Hola, Python!")
        inner_function()

outer_function()

"""
Funciones del lenguaje (Built_in)
"""

print(len("Mauricio"))
print(type(36))
print("Mauricio".upper())


"""
Variables locales y globales (Ambito o scope)
"""

global_variable = "Python"

def hello_python():
    local_var = "Hola"
    print(f"{local_var}, {global_variable}")

print(global_variable)
# print(local_var)    No se puede acceder desde fuera de la funcion donde fue declarada

hello_python()

"""
Desafio extra
"""

def print_numbers(text_1, text_2)-> int:
    count = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(text_1 + text_2)
        elif number % 3 == 0:
            print(text_1)
        elif number % 5 == 0:
            print(text_2)
        else:
            print(number)
            count += 1
    return count

print(print_numbers("fizz", "Buzz"))