def f():
    while True:
        try:
            x = int(input("Ingrese un número: "))
            print("Número válido: ", x)
            break
        except ValueError as e:
            print("La función tiene :-) ", e)

try:
    f()
except Exception as e:
    print("Error inesperado: ", e)

print("Sigamos adelante")