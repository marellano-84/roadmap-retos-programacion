"""
Operaciones
"""
s1 = "Hola"
s2 = "Python"

# Concatenación
print(s1 + ", " + s2 + "!")

# Repetición
print(s1 * 4)

# Indexación
print(s1[3])

# Longitud
print(len(s2))

# Slicing (porción)
print(s2[2:6])  # Indice de inicio : indice final (omite el indice final asi que debe ser "fin + 1")
print(s2[2:])
print(s2[2:len(s2)])
print(s2[0:2])
print(s2[:2])

# Busqueda
print("a" in s1)
print("i" in s1)

# Reemplazo
print(s1.replace("o", "a"))

# División
print(s2.split("t"))

# Mayusculas, minusculas, titulo y letra capital
print(s1.upper())   # Mayuscula
print(s1.lower())   # Minuscula
print("primera letra de cada palabra en mayusculas".title())
print("capital".capitalize())

# Eliminación de espacios al principio y al final
print(" mauricio arellano ".strip() + "@example.com")

# Busqueda al principio y al final
print(s1.startswith("Ho"))
print(s1.startswith("Py"))
print(s1.endswith("la"))
print(s1.endswith("thon"))

s3 = "Mauricio Arellano @example"

# Busqueda de posición
print(s3.find("mauricio"))
print(s3.find("Mauricio"))
print(s3.find("M"))
print(s3.lower().find("m"))

# Busqueda de ocurrencias
print(s3.lower().count("m"))

# Formateo
print("Saludo: {}, lenguaje: {} !".format(s1, s2))

# Interpolación
print(f"Saludo: {s1}, lenguaje: {s2}")

# Transformación en lista  de caracteres
print(list(s3))

# Transformación de lista a cadena
li = [s1, ", ", s2, "!"]
print("".join(li))

# Transformación numérica
s4 = "123456"
s4 = int(s4)
print(s4)

s5 = "123456.123"
s5 = float(s5)
print(s5)

# Comprobaciones
s4 = "123456"
print(s1.isalnum())
print(s4.isalpha())
print(s4.isnumeric())


"""
Desafio extra
"""
def check(word1, word2: str):

    # Palindromos
    print(f"{word1} es un palíndromo?: {word1 == word1[::-1]}")
    print(f"{word2} es un palíndromo?: {word2 == word2[::-1]}")

    # Anagramas
    print(f"{word1} es anagrama de {word2}?: {sorted(word1) == sorted(word2)}")

    # Isogramas
    print(f"{word1} y {word2} son isogramas?: {len(word1) == len(set(word1))}")
    print(f"{word1} y {word2} son isogramas?: {len(word2) == len(set(word2))}")

check("anilina", "python")