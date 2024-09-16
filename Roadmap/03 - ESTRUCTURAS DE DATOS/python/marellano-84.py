# Listas
my_list = ["Mau", "Juan", "Pedro", "Alex"]
print(my_list)

my_list.append("Alice")  # Inserción
print(my_list)
my_list.remove("Alex")  # Eliminación
print(my_list)
print(my_list[1])  # Acceso
my_list[1] = "Nico"  # Actualización
print(my_list)
my_list.sort()  # Ordenación
print(my_list)


# Tuplas
my_tuple = ("Mau", "Arellano", "@marellano-84", "39")
print(my_tuple[1])  # Acceso
my_tuple = tuple(
    sorted(my_tuple)
)  # Ordenación ("Sorted" ordena y retorna un objeto de tipo lista y con "tuple" casteamos a tipo tupla)
print(my_tuple)

# Sets  (se guardan desordenados y sin indice, usando "hash" y no pueden ser ordenados )
my_set = {"Mau", "Arellano", "@marellano-84", "39"}
print(my_set)
my_set.add("asdas@gmail.com")  # Inserción
print(my_set)
my_set.remove("39")  # Eliminación
print(my_set)

# Diccionario
my_dict = {"name": "Mau", 
           "surname": "Arellano", 
           "user": "@marellano-84", 
           "age": "39"
           }
print(my_dict)
my_dict["email"] = "mau.arellano@outlook.com"   # Inserción
print(my_dict)
del my_dict["surname"]      # Eliminación
print(my_dict["name"])      # Acceso
my_dict["name"] = "Mauricio"    # Actualización (cuando no existe la "key" funciona como una inserción)
print(my_dict)
my_dict = dict(sorted(my_dict.items()))     # Ordenación


"""
Desafio extra
"""
def my_agenda():

    agenda = {}

    def insert_contact():
        phone = input("Ingresa el telefono de contacto")
        if phone.isdigit() and len(phone) == 10:
            agenda[name] = phone
        else:
            print("Debes introducir un número de telefono de 10 digitos")

    while True:
        print("")
        print(" -   Agenda de contactos    - ")
        print("1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Finalizar")

        option = input("\nSelecciona una opcion: ")

        match option:
            case "1":
                name = input("Ingresa el nombre de contacto a buscar: ")
                if name in agenda:
                    print(f"El numero de telefono de {name} es {agenda[name]}")
                else:
                    print(f"El contacto {name} no existe")
            case "2":
                name = input("Ingresa el nombre de contacto: ")
                insert_contact()
            case "3":
                name = input("Ingresa el nombre de contacto a actualizar: ")
                if name in agenda:
                    insert_contact()
                else:
                    print(f"El contacto {name} no existe")
            case "4":
                name = input("Ingresa el nombre de contacto a eliminar: ")
                if name in agenda:
                    del agenda[name]
                else:
                    print(f"El contacto {name} no existe")
            case "5":
                print("Saliendo de la agenda.")
                break
            case _:
                print("Opción no valida")

my_agenda()
