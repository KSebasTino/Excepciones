while True:
    try:
        x = float(input("Ingrese un número: "))
        inverse = 1.0 / x
        print("La inversa es:", inverse)
        break
    except ValueError:
        print("Debe ser un int o float. Intente de nuevo.")
    except ZeroDivisionError:
        print("No se puede dividir por cero. Intente de nuevo.")