while True:
    try:
        a = int(input("Ingrese un valor para a: "))
        b = int(input("Ingrese un valor para b: "))
        if a < 0 or b < 0:
            raise ZeroDivisionError
        print("El resultado de la división es: {}".format(a/b))
        break
    except ZeroDivisionError:
        print("Error: Por favor, ingrese un valor válido (mayor o igual a 0) para ambos números.")