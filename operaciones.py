import math

def suma():
    a = int(input("a: "))
    b = int(input("b: "))
    res = a + b
    print (str(res))
    
def resta():
    a = int(input("a: "))
    b = int(input("b: "))
    res = a - b
    print (str(res))

def multiplicacion():
    a = int(input("a: "))
    b = int(input("b: "))
    res = a * b
    print (str(res))

def division():
    a = int(input("a: "))
    b = int(input("b: "))
    if b == 0: print (str("no se puede dividir por cero"))
    else:
        res = a / b
        print (str(res))
        
def iva():
    res3 = 0
    a = int(input("precio de la cena: "))
    res1 = a - (a * 0.14)
    res2 = a * 0.14
    res3 = res1 + res2
    print ("subtotal: " + str(res1))
    print ("IVA: " + str(res2))
    print ("total: " + str(res3))
    
def areaCirculo():
    a = int(input("radio: "))
    print ("el area es: " + str(round(math.pi * a * a)))

def aypCuadrado():
    a = int(input("lado: "))
    print ("el area es: " + str(a * a))
    print ("el perimetro es: " + str(4 * a))

def aypTriangulo():
    a = int(input("lado 1: "))
    b = int(input("lado 2: "))
    c = int(input("lado 3: "))
    s = (a + b + c) / 2
    x = round(s * (s - a) * (s - b) * (s - c))
    area = round(math.sqrt(x))
    perimetro = a + b + c
    print("el area es: " + str(area))
    print("el perimetro es: " + str(perimetro))

def imc():
    a = float(input("ingrese su peso (kg): "))
    b = float(input("ingrese su estatura (m): "))
    imc = a / (b * b)
    print ("indice de masa corporal: " + str(imc))
    if imc < 16: print ("Infrapeso: Delgadez Severa")
    if imc > 16.00 and imc < 16.99: print ("Infrapeso: Delgadez moderada")
    if imc > 17.00 and imc < 18.49: print ("Infrapeso: Delgadez aceptable")
    if imc > 18.50 and imc < 24.99: print ("Peso Normal")
    if imc > 25.00 and imc < 29.99: print ("Sobrepeso")
    if imc > 30.00 and imc < 34.99: print ("Obeso: Tipo I")
    if imc > 35.00 and imc < 39.99: print ("Obeso: Tipo II")
    if imc > 40: print ("Obeso: Tipo III")

def frase():
    frase= str(input("Ingrese una frase: "))
    print (frase.upper())
    print (frase.lower())
    print (frase.capitalize())
    print (frase.replace(" ",""))
    
def menu():
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Cena")
    print("6. Area de un circulo")
    print("7. Area y perimetro de un cuadrado")
    print("8. Area y perimetro de un triangulo")
    print("9. indice de masa corporal")
    print("10. frase")
    print("11. Salir")
    

def opciones():
    opcion = int(input("elija una opcion: "))
    if opcion == 1: suma()
    if opcion == 2: resta()
    if opcion == 3: multiplicacion()
    if opcion == 4: division()
    if opcion == 5: iva()
    if opcion == 6: areaCirculo()
    if opcion == 7: aypCuadrado()
    if opcion == 8: aypTriangulo()
    if opcion == 9: imc()
    if opcion == 10: frase()
    if opcion == 11: exit()

menu()
opciones()