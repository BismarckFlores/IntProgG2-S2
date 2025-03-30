import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def suma_enteros():
    limpiar_pantalla()
    print("-" * 73)
    print("Has seleccionado la actividad de: Suma de enteros")
    print("-" * 73)
    a = int(input("Digite el primer valor a sumar: "))
    b = int(input("Digite el segundo valor a sumar: "))
    c = a + b
    print(f"La suma de {a} y {b} es {c}")
    print(f"{a} + {b} = {c}")
    print("-" * 73)
    input("Enter para continuar")

def resta_enteros():
    limpiar_pantalla()
    print("-" * 73)
    print("Has seleccionado la actividad de: Resta de enteros")
    print("-" * 73)
    a = int(input("Digite el minuendo: "))
    b = int(input("Digite el sustraendo: "))
    c = a - b
    print(f"La diferencia de {a} y {b} es {c}")
    print(f"{a} - {b} = {c}")
    print("-" * 73)
    input("Enter para continuar")

def multiplicacion_enteros():
    limpiar_pantalla()
    print("-" * 73)
    print("Has seleccionado la actividad de: Multiplicación de enteros")
    print("-" * 73)
    a = int(input("Digite el primer factor o multiplicado: "))
    b = int(input("Digite el segundo factor o multiplicador: "))
    c = a * b
    print(f"El producto de {a} y {b} es {c}")
    print(f"{a} * {b} = {c}")
    print("-" * 73)
    input("Enter para continuar")

def division_enteros():
    limpiar_pantalla()
    print("-" * 73)
    print("Has seleccionado la actividad de: División de enteros")
    print("-" * 73)
    a = int(input("Digite el dividendo: "))
    b = int(input("Digite el divisor: "))
    c = a / b
    d = a % b
    print(f"El cociente de {a} y {b} es {c}")
    print(f"{a} / {b} = {c}")
    if d == 0:
        print("Esta división no tiene residuo")
    else:
        print(f"El residuo de la división es {d}")
    print("-" * 73)
    input("Enter para continuar")

def antecesor_sucesor():
    limpiar_pantalla()
    print("-" * 73)
    print("Has seleccionado la actividad de: Antecesor y sucesor de un número")
    print("-" * 73)
    a = int(input("Digite el número del cual quieres saber el antecesor y sucesor: "))
    b = a - 1
    c = a + 1
    print(f"El antecesor es {b} y el sucesor es {c}")
    print("-" * 73)
    input("Enter para continuar")

def area_circulo():
    limpiar_pantalla()
    print("-" * 73)
    print("Has seleccionado la actividad de: Cálculo del área de un círculo")
    print("-" * 73)
    a = float(input("Digite el radio del círculo: "))
    b = 3.1416 * a ** 2
    print(f"El área del círculo es {b}")
    print("-" * 73)
    input("Enter para continuar")

def conversion_monetaria():
    while True:
        limpiar_pantalla()
        print("-" * 73)
        print("Has seleccionado la actividad de: Conversión monetaria")
        print("-" * 73)
        print("Selecciona qué tipo de conversión quieres hacer")
        print("0 - Dólar a Córdoba")
        print("1 - Córdoba a Dólar")
        a = int(input())
        if a in [0, 1]:
            break

    if a == 0:
        b = float(input("¿Cuántos Dólares quieres cambiar a Córdobas? "))
        print("-" * 73)
        c = b * 68.88
        print(f"{b} Dólares son {c} Córdobas")
    else:
        b = float(input("¿Cuántos Córdobas quieres cambiar a Dólares? "))
        print("-" * 73)
        c = b * 0.027
        print(f"{b} Córdobas son {c} Dólares")
    print("-" * 73)
    input("Enter para continuar")

def calculo_promedio():
    limpiar_pantalla()
    print("-" * 73)
    print("Has seleccionado la actividad de: Cálculo del promedio de un estudiante")
    print("-" * 73)
    cantidad = int(input("¿Cuántas notas vas a ingresar? "))
    notas = []
    suma = 0

    for i in range(cantidad):
        nota = float(input(f"Ingresa la nota {i + 1}: "))
        notas.append(nota)
        suma += nota

    promedio = suma / cantidad
    print("-" * 73)
    print("Notas ingresadas:")
    for i in range(cantidad):
        print(f"Nota {i + 1}: {notas[i]}")
    print(f"Promedio: {promedio}")
    print("-" * 73)
    input("Enter para continuar")

def main():
    continuar = "Y"
    while continuar.upper() == "Y":
        while True:
            limpiar_pantalla()
            print("-" * 73)
            print("En este archivo están almacenadas todas las actividades de la Guía Didáctica N° 2")
            print("-" * 73)
            print("Dependiendo de la actividad que quieras ejecutar, coloca un número del 0 al 7")
            print("0 - Suma | 1 - Resta")
            print("2 - Multiplicación | 3 - División")
            print("4 - Antecesor/Sucesor | 5 - Área del círculo")
            print("6 - Conversión monetaria | 7 - Cálculo de promedio")
            print("-" * 73)
            try:
                actividad = int(input("Selecciona una opción: "))
                if 0 <= actividad <= 7:
                    break
            except ValueError:
                continue

        if actividad == 0:
            suma_enteros()
        elif actividad == 1:
            resta_enteros()
        elif actividad == 2:
            multiplicacion_enteros()
        elif actividad == 3:
            division_enteros()
        elif actividad == 4:
            antecesor_sucesor()
        elif actividad == 5:
            area_circulo()
        elif actividad == 6:
            conversion_monetaria()
        elif actividad == 7:
            calculo_promedio()

        while True:
            limpiar_pantalla()
            continuar = input("¿Deseas ejecutar alguna otra actividad? (Y/N): ")
            if continuar.upper() in ["Y", "N"]:
                break

    print("Gracias por usar el programa. ¡Hasta la próxima!")

if __name__ == "__main__":
    main()