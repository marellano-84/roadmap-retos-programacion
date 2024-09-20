"""
Recursividad
"""

# def countdown(number: int):     # Ejemplo unicamente explicativo
#     if number >= 0:
#         print(number)
#         countdown(number - 1)

# countdown(100)

"""
Desafio extra
"""

# Factorial con recursividad
# def factorial(number: int) -> int:
#     if number < 0:
#         print("Los numeros negativos no son validos")
#         return 0
#     elif number == 0:
#         return 1
#     else:
#         return number * factorial(number - 1)
    
# print(factorial(5))

# Fibonacci con recursividad
def fibonacci(number: int) -> int:
    if number <= 0:
        print("El número tiene que ser mayor que 0")
        return 0
    elif number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)

print(fibonacci(8))