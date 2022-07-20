def array_diff(a,b):
    new_array = []
    for x in a:
        if x not in b:
            new_array.append(x)
    return new_array