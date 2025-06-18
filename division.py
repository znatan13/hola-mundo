try:
    num1=float(input("Introduce el numerador: "))
    num2=float(input("Introduce el denomerador: "))
    resultado=num1/num2
    print("El resultado es:", resultado)
except ZerpDivisionError:
    print("Error, no se puede dividir entre cero.")
except ValueError:
    print("Error: Introduce un número válido.")
