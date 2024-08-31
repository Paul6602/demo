def digitos(n):
        if n<10:
            return 1
        else:
            return 1 + digitos(n/10)
numero=int(input("Ingresa un número: "))
print("la cantidad de digitos es:",digitos(numero)
print("modificacion con git")
print("otro cambio para el tercer commit")
