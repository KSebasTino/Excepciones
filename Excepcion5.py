while True:
    try:
        a = float(input("Dividendo: "))
        b = float(input("Divisor: "))
        if a <= 0 or b <= 0:
            raise ZeroDivisionError
        print("El resultado de la división es: {}".format(a/b))
        break
    except ValueError:
        print("Error: Debe ser un número (int o float). Intente nuevamente.")
    except ZeroDivisionError:
        print("Error: Por favor, ingrese un valor mayor que CERO para ambos números. Intente nuevamente.")