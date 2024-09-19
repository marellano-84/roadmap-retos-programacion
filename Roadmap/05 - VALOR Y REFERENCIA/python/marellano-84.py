"""
Valor y referencia
"""

# Tipos de datos por valor  (cada que se asigna/cambia un valor a una variable se crea una nueva)
a = 10
b = 20
print(a)
print(b)
b = a     # Copiamos el valor de "a" en "b" y esto no altera la variable "a"
print(b)

# Tipos de datos por referencia
my_list_a = [10, 20]
my_list_b = [30, 40]
print(my_list_a)
print(my_list_b)
my_list_b = my_list_a   # Esto asigna la posición en memoria, es decir, tanto la lista "b" como la lista "a" son la misma lista
my_list_b.append(50)    # Al añadir algo a la lista "b" se añade a la lista "a" ya que ambas estan siendo referenciadas a la misma posicion en memoria
print(my_list_b)
print(my_list_a)

# Funciones con datos por valor
my_int_c = 10

def my_int_func(my_int: int):
    my_int = 20
    print(my_int)

my_int_func(my_int_c)
print(my_int_c)

# Funciones con datos por referencia
def my_list_func(my_list: list):
    my_list.append(30)
    print(my_list)

my_list_c = [10, 20]
my_list_func(my_list_c)
print(my_list_c)

"""
Desafio extra
"""
def func_por_valor(a, b: int):
    temp = a
    a = b
    b = temp
    return a, b

a = 5
b = 3
print(func_por_valor(a, b))
print(a)
print(b)

def func_por_referencia(c, d: list):
    copia = c
    c = d
    d = copia
    d.append(12)
    return c, d

c = [10, 20]
d = [30, 40]
print(c, d)
print(func_por_referencia(c, d))