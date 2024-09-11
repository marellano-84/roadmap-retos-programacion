"""
Operadores
"""

# Operadores Aritméticos
print(f"Suma: 8 + 4 = {8+4}")
print(f"Resta: 12 - 5 = {12-5}")
print(f"Multiplicación: 4 * 15 = {4*15}")
print(f"División: 8 / 4 = {8/4}")
print(f"Módulo: 10 % 3 = {10%3}")
print(f"Exponente: 8 ** 2 = {8**4}")
print(f"División Entera: 10 // 3 = {10//3}")

# Operadores de comparación
print(f"Igualdad: 10 == 3 es {15 == 4}")
print(f"Desigualdad: 12 != 6 es {12 != 6}")
print(f"Mayor que: 10 > 3 es {10 > 3}")
print(f"Menor que: 10 < 3 es {10 < 3}")
print(f"Mayor o igual que: 10 >= 10 es {10 >= 10}")
print(f"Menor o igual que: 10 < 3 es {10 <= 3}")

# Operadores lógicos
print(f"AND &&: 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4}")
print(f"OR ||: 10 + 3 == 14 and 5 - 1 == 4 es {10 + 3 == 14 and 5 - 1 == 4}")
print(f"NOT !: not 10 + 3 == 14 es {not 10 + 3 == 14}")

# Operadores de asignación
my_number = 11  #asignación
print(my_number)
my_number += 1  # suma y asignación
print(my_number)
my_number -= 1  # resta y asignación
print(my_number)
my_number *= 4  # multiplicación y asignación
print(my_number)
my_number /= 2  # división y asignación
print(my_number)
my_number %= 3  # módulo y asignación
print(my_number)
my_number **= 2  # exponente y asignación
print(my_number)
my_number //= 2  # división entera y asignación
print(my_number)

# Operadores de identidad
my_new_number = my_number   # compara si dos objetos son iguales 
print(f"my_number is my_new_number es {my_number is my_new_number}")
print(f"my_number is not my_new_number es {my_number is not my_new_number}")

# Operadores de pertenencia
print(f"La letra 'u' esta en  'mau' = {'u' in 'mau'}")
print(f"La letra 'b' esta en  'mau' = {'b' not in 'mau'}")

# Operadores de bit
a = 10  # 1010
b = 4   # 0011
print(f"AND: 10 & 4 = {10 & 4}")    # 0010
print(f"OR: 10 | 4 = {10 | 4}")     # 1011
print(f"XOR: 10 ^ 4 = {10 ^ 4}")    # 1001
print(f"NOT: ~10 = {~10}")
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}")      # 0010
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}")    # 101000

"""
Estructuras de control
"""

# Condicionales
my_string = "mau"
if my_string == "mau":
    print("my_string es mau")
elif my_string == "mauricio":
    print("my_string es mauricio")
else:
    print("my_string no es 'mau' ni 'mauricio'")
# Iterativas
for i in range(11):
    print(i)

i = 0
while i <= 10:
    print(i)
    i += 1

# Manejo de excepciones
try:
    print(10 / 0)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")

"""
Ejercicio Extra
"""

"""for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)"""