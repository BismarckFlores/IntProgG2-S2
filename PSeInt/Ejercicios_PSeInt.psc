Proceso Ejercicios_PSeInt
	Definir actividad Como Entero;
	Definir continuar Como Cadena;
	Repetir
		Limpiar Pantalla;
		Repetir
			Escribir 'En este archivo de PSeInt estan almacenadas todas las actividades de la Gu�a Did�ctica N� 2';
			Escribir '-------------------------------------------------------------------------';
			Escribir 'Dependiendo de la actividad que quiras ejecutar coloca un numero del 0 al 7';
			Escribir '-------------------------------------------------------------------------';
			Escribir '0 - Suma de dos n�meros enteros', ' 1 - Resta de dos n�meros enteros';
			Escribir '2 - Multiplicaci�n de dos n�meros enteros', ' 3 - Divisi�n entre dos n�meros enteros';
			Escribir '4 - Antecesor y sucesor de un n�mero', ' 5 - C�lculo del �rea de un c�rculo';
			Escribir '6 - Conversi�n monetaria', ' 7 - C�lculo del promedio de un estudiante';
			Escribir '-------------------------------------------------------------------------';
			Leer actividad;
		Hasta Que actividad>=0 Y actividad<=7
		Segun actividad Hacer
			0:
				Suma_enteros();
			1:
				Resta_enteros();
			2:
				Multiplicacion_enteros();
			3:
				Division_enteros();
			4:
				Antecesor_sucesor();
			5:
				Area_circulo();
			6:
				Conversion_monetaria();
			7:
				Calculo_promedio();
		FinSegun
		Repetir
			Limpiar Pantalla;
			Escribir 'Deseas ejecutar alguna otra actividad';
			Escribir 'Y / N';
			Leer continuar;
		Hasta Que continuar='Y' O continuar='N' O continuar='y' O continuar='n'
	Hasta Que continuar='N' O continuar='n'
	Escribir 'Gracias por usar el programa. �Hasta la pr�xima!';
FinProceso

SubAlgoritmo Suma_enteros
	Definir a, b, c Como Entero;
	Definir temp Como Cadena;
	Limpiar Pantalla;
	Escribir '-------------------------------------------------------------------------';
	Escribir 'Has seleccionado la actividad de: Suma de enteros';
	Escribir '-------------------------------------------------------------------------';
	Escribir 'Digite el primer valor a sumar';
	Leer a;
	Escribir 'Digite el primer valor a sumar';
	Leer b;
	Escribir '-------------------------------------------------------------------------';
	c <- a+b;
	Escribir 'La suma de ', a, ' y ', b, ' es ', c;
	Escribir a, ' + ', b, ' = ', c;
	Escribir '-------------------------------------------------------------------------';
	Escribir 'Enter para continuar';
	Leer temp;
FinSubAlgoritmo

SubAlgoritmo Resta_enteros
	Definir a, b, c Como Entero;
	Definir temp Como Cadena;
	Limpiar Pantalla;
	Escribir '-------------------------------------------------------------------------';
	Escribir 'Has seleccionado la actividad de: Resta de enteros';
	Escribir '-------------------------------------------------------------------------';
	Escribir 'Digite el minuendo';
	Leer a;
	Escribir 'Digite el sustraendo';
	Leer b;
	Escribir '-------------------------------------------------------------------------';
	c <- a-b;
	Escribir 'La diferencia de ', a, ' y ', b, ' es ', c;
	Escribir a, ' - ', b, ' = ', c;
	Escribir '-------------------------------------------------------------------------';
	Escribir 'Enter para continuar';
	Leer temp;
FinSubAlgoritmo

SubAlgoritmo Multiplicacion_enteros
	Definir a, b, c Como Entero;
	Definir temp Como Cadena;
	Limpiar Pantalla;
	Escribir '-------------------------------------------------------------------------';
	Escribir 'Has seleccionado la actividad de: Multiplicaci�n de enteros';
	Escribir '-------------------------------------------------------------------------';
	Escribir 'Digite el primer factor o multiplicado';
	Leer a;
	Escribir 'Digite el segundo factor o multiplicador';
	Leer b;
	Escribir '-------------------------------------------------------------------------';
	c <- a*b;
	Escribir 'El producto de ', a, ' y ', b, ' es ', c;
	Escribir a, ' * ', b, ' = ', c;
	Escribir '-------------------------------------------------------------------------';
	Escribir 'Enter para continuar';
	Leer temp;
FinSubAlgoritmo

SubAlgoritmo Division_enteros
	Definir a, b Como Entero;
	Definir c, d Como Real;
	Definir temp Como Cadena;
	Limpiar Pantalla;
	Escribir '-------------------------------------------------------------------------';
	Escribir 'Has seleccionado la actividad de: Divisi�n de enteros';
	Escribir '-------------------------------------------------------------------------';
	Escribir 'Digite el dividendo';
	Leer a;
	Escribir 'Digite el divisor';
	Leer b;
	Escribir '-------------------------------------------------------------------------';
	c <- a/b;
	d <- a MOD b;
	Escribir 'El cociente de ', a, ' y ', b, ' es ', c;
	Escribir a, ' - ', b, ' = ', c;
	Si d<0 Entonces
		Escribir 'Esta divisi�n no tiene residuo';
	SiNo
		Escribir 'El residuo de la divisi�n es ', d;
	FinSi
	Escribir '-------------------------------------------------------------------------';
	Escribir 'Enter para continuar';
	Leer temp;
FinSubAlgoritmo

SubAlgoritmo Antecesor_sucesor
	Definir a, b, c Como Entero;
	Definir temp Como Cadena;
	Limpiar Pantalla;
	Escribir '-------------------------------------------------------------------------';
	Escribir 'Has seleccionado la actividad de: Antecesor y sucesor de un n�mero';
	Escribir '-------------------------------------------------------------------------';
	Escribir 'Digite el n�mero del cual quieres saber el antecesor y sucesor';
	Leer a;
	Escribir '-------------------------------------------------------------------------';
	b <- a-1;
	c <- a+1;
	Escribir 'El antecesor es ', b, ' y el sucesor es ', c;
	Escribir '-------------------------------------------------------------------------';
	Escribir 'Enter para continuar';
	Leer temp;
FinSubAlgoritmo

SubAlgoritmo Area_circulo
	Definir a, b Como Real;
	Definir temp Como Cadena;
	Limpiar Pantalla;
	Escribir '-------------------------------------------------------------------------';
	Escribir 'Has seleccionado la actividad de: C�lculo del �rea de un c�rculo';
	Escribir '-------------------------------------------------------------------------';
	Escribir 'Digite el radio de el circulo';
	Leer a;
	Escribir '-------------------------------------------------------------------------';
	b <- pi*a^2;
	Escribir 'El area del circulo es ', b;
	Escribir '-------------------------------------------------------------------------';
	Escribir 'Enter para continuar';
	Leer temp;
FinSubAlgoritmo

SubAlgoritmo Conversion_monetaria
	Definir a, b, c Como Real;
	Definir temp Como Cadena;
	Repetir
		Limpiar Pantalla;
		Escribir '-------------------------------------------------------------------------';
		Escribir 'Has seleccionado la actividad de: Conversi�n monetaria';
		Escribir '-------------------------------------------------------------------------';
		Escribir 'Seleciona que tipo de conversi�n quieres hacer';
		Escribir '0 - Dolar a C�rdoba';
		Escribir '1 - C�rdoba a Dolar';
		Leer a;
	Hasta Que a>=0 Y a<=1
	Segun a Hacer
		0:
			Escribir 'Cuantos Dolares quieres cambiar a C�rdobas';
			Leer b;
			Escribir '-------------------------------------------------------------------------';
			c <- b*68.88;
			Escribir b, ' Dolares son ', c, 'C�rdobas';
		1:
			Escribir 'Cuantos C�rdobas quieres cambiar a Dolares';
			Leer b;
			Escribir '-------------------------------------------------------------------------';
			c <- b*0.027;
			Escribir b, ' C�rdobas son ', c, 'Dolares';
	FinSegun
	Escribir '-------------------------------------------------------------------------';
	Escribir 'Enter para continuar';
	Leer temp;
FinSubAlgoritmo

SubAlgoritmo Calculo_promedio
	Definir cantidad, i Como Entero;
	Definir notas, suma, promedio Como Real;
	Definir temp Como Cadena;
	Escribir '-------------------------------------------------------------------------';
	Escribir 'Has seleccionado la actividad de: C�lculo del promedio de un estudiante';
	Escribir '-------------------------------------------------------------------------';
	Escribir '�Cuantas notas vas a ingresar?';
	Leer cantidad;
	Dimensionar notas(100);
	suma <- 0;
	Para i<-1 Hasta cantidad Con Paso 1 Hacer
		Escribir 'Ingresa la nota ', i, ':';
		Leer notas[i];
		suma <- suma+notas[i];
	FinPara
	promedio <- suma/cantidad;
	Escribir '-------------------------------------------------------------------------';
	Escribir 'Notas ingresadas: ';
	Para i<-1 Hasta cantidad Con Paso 1 Hacer
		Escribir 'Nota ', i, ': ', notas[i];
	FinPara
	Escribir 'Promedio: ', promedio;
	Escribir '-------------------------------------------------------------------------';
	Escribir 'Enter para continuar';
	Leer temp;
FinSubAlgoritmo
