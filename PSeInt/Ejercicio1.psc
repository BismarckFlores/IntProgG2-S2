Algoritmo Ejercicio1
	//Variables
	Definir nombre, apellido, nombre_completo Como Caracter
	Definir edad, edad_dias Como Entero;
	Definir peso, peso_kg Como Real;
	
	//Ingreso de datos
	Escribir "Ingresa los siguientes datos"
	Escribir "Nombre"
	Leer nombre
	Escribir "Apellido"
	Leer apellido
	Escribir "Edad"
	Leer edad
	Escribir "Peso"
	Leer peso
	
	//Operación
	nombre_completo = Concatenar(apellido, " ")
	nombre_completo = Concatenar(nombre_completo, nombre)
	edad_dias = edad * 365
	peso_kg = peso / 2.204
	
	//Resultados
	Escribir "Nombre completo ", nombre_completo
	Escribir "Edad en dias ", edad_dias
	Escribir "Peso en Kg ", peso_kg
	
FinAlgoritmo
