Algoritmo Ejercicio3
	
	//Variables
	Definir deuda Como Entero
	Definir deuda_total Como Real
	a�os = 5
	interes = 0.05
	
	//Ingreso de datos
	Escribir "Usted esta aplicando a un prestamo de 5 a�os con un interes anual del 3%"
	Escribir "De cuanto desea que sea el prestamo en dolares: "
	Leer deuda
	
	//Operaci�n
	deuda_total = deuda
	Repetir
		deuda_total = deuda_total + (deuda_total * interes)
		a�os = a�os - 1
	Hasta Que a�os = 0
	
	//Resultados
	Escribir "Al cabo de 5 a�os usted tendra que pagar un monto de: $", deuda_total
	
FinAlgoritmo
