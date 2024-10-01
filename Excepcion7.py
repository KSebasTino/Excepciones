class MyException(Exception):
    pass

while True:
    try:
        x = input("Ingrese un valor: ")
        raise MyException("¡Una excepción no siempre prueba la regla!")
    except MyException as e:
        print("Error: ", e)
        print("Intente nuevamente.")
    else:
        print("Valor válido: ", x)
        break

print("Sigamos adelante")