def persistence(n):
    times = 0
    while(n >= 10):
    # Se itera hasta obtener 1 solo dígito llevando el conteo con la variable times
        result = 1
        n_str = str(n)
        for x in n_str:
            result = result * int(x)
        n = result
        times += 1
    return times