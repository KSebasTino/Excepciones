while(True):
    try:
        n = float(input("Introduce un número: "))
        m = 4
        print("{}/{} = {}".format(n, m, n / m))
    except:
        print("Ocurrio un error, introduce correctamente el número")
    else:
        print("Todo funciona correctamente")
        break