#variables
x_metros = int(input("Dime la cantidad de metros de ancho: "))
y_metros = int(input("Dime la cantidad de metros de largo: "))

#calculos
area = x_metros * y_metros
ladrillos_necesarios = area * 20

#resultado
print(f'Para llenar una area de {area} metros cuadrados se necesitan {ladrillos_necesarios} ladrillos')