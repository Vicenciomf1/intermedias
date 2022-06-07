def printInfo(diccionario):
    for lista in diccionario.values():
        print(f"{len(lista)} UBICACIONES")
        for elemento in lista:
            print(elemento)
        print("\n")


def run():
    dojo = {
        'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
        'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
    }
    printInfo(dojo)


if __name__ == '__main__':
    run()
