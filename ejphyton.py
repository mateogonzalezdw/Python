def EJ1():
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))
    print("La suma de", numero1, "más", numero2, "es igual a", (numero1 + numero2))

#EJ1()

def EJ2():
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))
    numero3 = int(input("Ingrese el tercer número: "))
    numero4 = int(input("Ingrese el cuarto número: "))
    print("La suma de", numero1, "más", numero2, "más", numero3, "más", numero4, "es igual a", (numero1 + numero2 + numero3 + numero4))

#EJ2()

def EJ3():
    base = float(input("Ingrese la base del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))
    
    print("La superficie del rectángulo es de",base*altura,"cm2")

#EJ3()

def EJ4():
    lado = float(input("Ingrese el lado del cuadrado con decimales: "))
    print("La superficie del cuadrado es de",lado*2,"cm2")

#EJ4()

def EJ5():
    segundos = int(input("Ingrese los segundos: "))
    minutos = int(input("Ingrese los minutos: "))
    horas = int(input("Ingrese las horas: "))

    print("En total son",segundos+minutos*60+horas*60*60,"segundos")

#EJ5()

def EJ6():
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))

    print("La superficie del triángulo es de",1/2*base*altura,"cm2")

#EJ6()

def EJ7():
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))
    numero3 = float(input("Ingrese el tercer número: "))
    numero4 = float(input("Ingrese el cuarto número: "))
    numero5 = float(input("Ingrese el quinto número: "))
    numero6 = float(input("Ingrese el sexto número: "))

    print("El promedio es",(numero1+numero2+numero3+numero4+numero5+numero6)/6)

#EJ7()

def EJ8():
    parcial = float(input("Ingrese el número parcial: "))
    total = float(input("Ingrese el número total: "))
    
    print(parcial,"representa un",(parcial/total)*100,"porciento del número total")

#EJ8()

def EJ9():
    fecha = int(input("Ingrese una fecha en formato numérico DDMMAAAA: "))
    dia = fecha//1000000
    mes = (fecha//10000)%100
    año = fecha%10000

    print("Día: ",dia)
    print("Mes: ",mes)
    print("Año: ",año)
    
#EJ9()

def EJ10():
    exP = float(input("Nota de exámenes parciales: "))
    TP = float(input("Nota de trabajos prácticos: "))
    exI =  float(input("Nota de exámen integrador: "))

    print("La nota final es",(exP*0.3+TP*0.2+exI*0.5))

#EJ10()

def EJ11():
    salario = 5500
    Avendidos = int(input("Cantidad de autos vendidos: "))
    Avalor = int(input("Valor del auto: "))

    print("El salario total es: ",salario+Avendidos*200+Avalor*0.05)

#EJ11()

  
