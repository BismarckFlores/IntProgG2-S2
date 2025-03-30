import os
from colorama import init, Fore, Style

# Inicializar colorama
init(autoreset=True)

# Constantes
TASA_DOLAR_A_CORDOBA = 68.88
TASA_CORDOBA_A_DOLAR = 0.027
PI = 3.1416
LINE_WIDTH = 78

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def imprimir_titulo(texto):
    print(Fore.CYAN + Style.BRIGHT + "═" * LINE_WIDTH)
    print(Fore.YELLOW + Style.BRIGHT + texto.center(LINE_WIDTH))
    print(Fore.CYAN + Style.BRIGHT + "═" * LINE_WIDTH)

def pedir_entero_en_rango(mensaje, minimo, maximo):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo <= valor <= maximo:
                return valor
            else:
                print(Fore.RED + f"Por favor, ingresa un número entre {minimo} y {maximo}.")
        except ValueError:
            print(Fore.RED + "Por favor, ingresa un número entero válido.")

def pedir_real(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print(Fore.RED + "Por favor, ingresa un número decimal válido.")

def pausa():
    input(Fore.MAGENTA + "\nPresiona Enter para continuar...")

def suma_enteros():
    limpiar_pantalla()
    imprimir_titulo("SUMA DE ENTEROS")
    a = pedir_entero_en_rango("Primer número: ", -100000, 100000)
    b = pedir_entero_en_rango("Segundo número: ", -100000, 100000)
    print(Fore.GREEN + f"{a} + {b} = {a + b}")
    pausa()

def resta_enteros():
    limpiar_pantalla()
    imprimir_titulo("RESTA DE ENTEROS")
    a = pedir_entero_en_rango("Minuendo: ", -100000, 100000)
    b = pedir_entero_en_rango("Sustraendo: ", -100000, 100000)
    print(Fore.GREEN + f"{a} - {b} = {a - b}")
    pausa()

def multiplicacion_enteros():
    limpiar_pantalla()
    imprimir_titulo("MULTIPLICACIÓN DE ENTEROS")
    a = pedir_entero_en_rango("Primer factor: ", -10000, 10000)
    b = pedir_entero_en_rango("Segundo factor: ", -10000, 10000)
    print(Fore.GREEN + f"{a} * {b} = {a * b}")
    pausa()

def division_enteros():
    limpiar_pantalla()
    imprimir_titulo("DIVISIÓN DE ENTEROS")
    a = pedir_entero_en_rango("Dividendo: ", -100000, 100000)
    while True:
        b = pedir_entero_en_rango("Divisor (≠ 0): ", -100000, 100000)
        if b != 0:
            break
        print(Fore.RED + "El divisor no puede ser cero.")
    cociente = a / b
    residuo = a % b
    print(Fore.GREEN + f"{a} / {b} = {cociente}")
    print(Fore.BLUE + ("No hay residuo." if residuo == 0 else f"Residuo: {residuo}"))
    pausa()

def antecesor_sucesor():
    limpiar_pantalla()
    imprimir_titulo("ANTECESOR Y SUCESOR")
    numero = pedir_entero_en_rango("Número: ", -100000, 100000)
    print(Fore.GREEN + f"Antecesor: {numero - 1}")
    print(Fore.GREEN + f"Sucesor: {numero + 1}")
    pausa()

def area_circulo():
    limpiar_pantalla()
    imprimir_titulo("ÁREA DE UN CÍRCULO")
    radio = pedir_real("Radio del círculo (positivo): ")
    while radio <= 0:
        print(Fore.RED + "El radio debe ser mayor que 0.")
        radio = pedir_real("Radio del círculo (positivo): ")
    area = PI * radio ** 2
    print(Fore.GREEN + f"Área = {area}")
    pausa()

def conversion_monetaria():
    limpiar_pantalla()
    imprimir_titulo("CONVERSIÓN MONETARIA")
    print(Fore.WHITE + "1. Dólares a Córdobas")
    print("2. Córdobas a Dólares")
    opcion = pedir_entero_en_rango("Elige una opción (1-2): ", 1, 2)

    if opcion == 1:
        cantidad = pedir_real("Cantidad en dólares: ")
        resultado = cantidad * TASA_DOLAR_A_CORDOBA
        print(Fore.GREEN + f"{cantidad} USD = {resultado} Córdobas")
    else:
        cantidad = pedir_real("Cantidad en córdobas: ")
        resultado = cantidad * TASA_CORDOBA_A_DOLAR
        print(Fore.GREEN + f"{cantidad} Córdobas = {resultado} USD")
    pausa()

def calculo_promedio():
    limpiar_pantalla()
    imprimir_titulo("CÁLCULO DE PROMEDIO")
    cantidad = pedir_entero_en_rango("¿Cuántas notas vas a ingresar? ", 1, 100)
    notas = []
    for i in range(cantidad):
        nota = pedir_real(f"Nota {i + 1}: ")
        notas.append(nota)

    promedio = sum(notas) / cantidad
    print(Fore.CYAN + "\nNotas ingresadas:")
    for i, nota in enumerate(notas, start=1):
        print(f"  Nota {i}: {nota}")
    print(Fore.YELLOW + Style.BRIGHT + f"\nPromedio final: {promedio}")
    pausa()

def mostrar_menu():
    limpiar_pantalla()
    imprimir_titulo("MENÚ DE ACTIVIDADES - GUÍA DIDÁCTICA Nº 2")

    print(Fore.CYAN + Style.BRIGHT + "╔" + "═" * (LINE_WIDTH - 2) + "╗")
    print("║ {:<30}│ {:<43}║".format("0. Suma de enteros", "4. Antecesor y sucesor"))
    print("║ {:<30}│ {:<43}║".format("1. Resta de enteros", "5. Área de un círculo"))
    print("║ {:<30}│ {:<43}║".format("2. Multiplicación", "6. Conversión monetaria"))
    print("║ {:<30}│ {:<43}║".format("3. División", "7. Cálculo de promedio"))
    print(Fore.CYAN + Style.BRIGHT + "╠" + "═" * (LINE_WIDTH - 2) + "╣")
    print(Fore.RED + Style.BRIGHT + "║" + "  8. Salir".center(LINE_WIDTH - 2) + "║")
    print(Fore.CYAN + Style.BRIGHT + "╚" + "═" * (LINE_WIDTH - 2) + "╝")
    print(Style.RESET_ALL)

def ejecutar_actividad(opcion):
    actividades = {
        0: suma_enteros,
        1: resta_enteros,
        2: multiplicacion_enteros,
        3: division_enteros,
        4: antecesor_sucesor,
        5: area_circulo,
        6: conversion_monetaria,
        7: calculo_promedio
    }
    accion = actividades.get(opcion)
    if accion:
        accion()
    elif opcion == 8:
        print(Fore.GREEN + "Gracias por usar el programa. ¡Hasta la próxima!")
    else:
        print(Fore.RED + "Actividad no válida.")
        pausa()

def main():
    while True:
        mostrar_menu()
        opcion = pedir_entero_en_rango("Selecciona una opción (0-8): ", 0, 8)

        if opcion == 8:
            print(Fore.GREEN + "\nGracias por usar el programa. ¡Hasta la próxima!")
            break

        ejecutar_actividad(opcion)

        while True:
            respuesta = input(Fore.MAGENTA + "\n¿Deseas realizar otra actividad? (S/N): ").strip().lower()
            if respuesta in ['s', 'n']:
                break
            print(Fore.RED + "Entrada no válida. Solo se permite 'S' o 'N'.")

        if respuesta == 'n':
            print(Fore.GREEN + "\nGracias por usar el programa. ¡Hasta la próxima!")
            break

if __name__ == "__main__":
    main()
