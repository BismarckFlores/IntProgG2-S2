print("Usted está aplicando a un préstamo de 5 años con un interés anual del 3%.")

#Pedir al usuario el monto del préstamo y validar la entrada
while True:
    try:
        monto_prestamo = float(input("Digite la cantidad del préstamo en dólares: "))
        if monto_prestamo <= 0:
            print("Por favor, ingrese un monto mayor a cero.")
            continue
        break
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número.")
        
# Parámetros del préstamo
interes_anual = 0.03
periodo_años = 5

# Cálculo del monto total a pagar con interés compuesto
monto_total = monto_prestamo * ((1 + interes_anual) ** periodo_años)

# Mostrar el resultado
print(f"\nEl monto total a pagar al final del período es de ${monto_total:,.2f} dólares.\n")