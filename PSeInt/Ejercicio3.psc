Algoritmo Ejercicio3
	
	//Variables
	Definir deuda, plazo Como Entero;
	Definir deuda_total, interes Como Real;
	plazo <- 5;
	interes <- 0.05;
	
	//Ingreso de datos
	Escribir "Usted esta aplicando a un prestamo de 5 a�os con un interes anual del 3%";
	Escribir "De cuanto desea que sea el prestamo en dolares: ";
	Leer deuda;
	
	//Operaci�n
	deuda_total <- deuda;
	Repetir
		deuda_total <- deuda_total + (deuda_total * interes);
		plazo <- plazo - 1;
	Hasta Que plazo = 0
	
	//Resultados
	Escribir "Al cabo de 5 a�os usted tendra que pagar un monto de: $", deuda_total;
	
FinAlgoritmo
