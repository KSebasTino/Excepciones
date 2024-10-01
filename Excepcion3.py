while True:
    x = int(input("Ingrese un valor para x (debe ser menor o igual a 5): "))
    if x > 5:
        print("Error: x no debería ser mayor a 5. Intente nuevamente.")
    else:
        print("Valor de x válido: {}".format(x))
        break