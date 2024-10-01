class Error(Exception):
    """Clase base para otras excepciones"""
    pass

class ValueTooSmallError(Error):
    """Aumenta cuando el valor de entrada es demasiado pequeño"""
    pass

class ValueTooLargeError(Error):
    """Aumenta cuando el valor de entrada es demasiado grande"""
    pass

class InvalidInputError(Error):
    """Aumenta cuando el valor de entrada no es un número"""
    pass

# Necesitas adivinar este número
number = 10

# El usuario adivina un número hasta que lo acierta
while True:
    try:
        i_num = int(input("Ingrese un número: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        print("¡Felicidades! Lo adivinaste.")
        break
    except ValueError:
        raise InvalidInputError
    except ValueTooSmallError:
        print("Este valor es demasiado pequeño, inténtelo de nuevo.")
        print()
    except ValueTooLargeError:
        print("Este valor es demasiado grande, inténtelo de nuevo.")
        print()
    except InvalidInputError:
        print("Error: El valor de entrada no es un número. Inténtelo de nuevo.")
        print()