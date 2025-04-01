Algoritmo Ejercico2
	
	//Variables
	Definir x_metros, y_metros, area, ladrillos_necesarios Como Entero
	ladrillos_metro = 20
	
	//Ingreso de datos
	Escribir "Cuantos metros de ancho quieres que sea tu muro"
	Leer x_metros
	Escribir "Cuantos metros de alto quieres que sea tu muro"
	Leer y_metros
	
	//Operación
	area = x_metros * y_metros
	ladrillos_necesarios = area * ladrillos_metro
	
	//Resultados
	Escribir "Para llenar un area de " area " metros cuadrados se necesitan " ladrillos_necesarios " ladrillos"
	
FinAlgoritmo
