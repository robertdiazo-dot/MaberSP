import random

# Función 1: Generar un número aleatorio entre 1 y 100
def numero_aleatorio():
    return random.randint(1, 100)

# Función 2: Elegir una fruta al azar
def fruta_aleatoria():
    frutas = ["Manzana", "Pera", "Plátano", "Naranja", "Uva"]
    return random.choice(frutas)

# Función 3: Lanzar un dado
def lanzar_dado():
    return random.randint(1, 6)

# Pruebas
print("Número aleatorio:", numero_aleatorio())
print("Fruta aleatoria:", fruta_aleatoria())
print("Resultado del dado:", lanzar_dado())