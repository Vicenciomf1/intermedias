def cambiarIndiceAdentro(listapadre, valor, nuevovalor): #Para cambiar varios adentro, necesitamos a la lista padre, el valor a buscar, y con qué se reemplazará
    cambios = 0
    for lista in listapadre: #Entonces, para cada lista dentro de la listapadre
        for i in range(len(lista)): #Si es que los elementos de adentro de estas listas coinciden con el valor, entonces reemplázalos
            if lista[i] == valor:
                lista[i] = nuevovalor
                cambios += 1 #Y de paso registra ese cambio en un contador
            else:
                continue
    return (cambios,valor,nuevovalor) #Como es mutable la lista, el cambio no es necesario retornarlo, pero sí el contador de cambios, para que no se pierda.
def cambiarKeyEnLista(lista, atributo, valor, valornuevo): #Para cambiar el valor de la key, necesitamos la lista de diccionarios, y los atributos y valores correspondientes que, una vez coincidan, serán cambiados en valor.
    cambios = 0
    for diccionario in lista: #Recorre la lista para encontrar cada diccionario
        for key, value in diccionario.items(): #Usamos el método items para en cada contador obtener las keys y los values
            if str(key) == atributo and str(value) == valor: #Y si coinciden, cambia el valor al valor nuevo
                diccionario[atributo] = valornuevo
                cambios += 1
            else:
                continue
    return (cambios,valor,valornuevo)
def cambiarValorListaDiccionario(diccionario, atributo, valor, valornuevo):
    cambios = 0
    for key, value in diccionario.items(): #Usamos el método items para en cada contador obtener las keys y los values
        if str(key) == atributo: #Si coincide el atributo, entonces hacemos el paso extra para modificar su lista
            for indice in range(len(value)): #Si coincide el elemento con el valor, entonces reemplázalo
                if value[indice] == valor:
                    value[indice] = valornuevo
                    cambios += 1
            else:
                continue
        else:
            continue
    return (cambios,valor,valornuevo)
def cambiarDiccionarioDentroDeListaPorValorEntero(lista, valor, nuevovalor):
    cambios = 0
    for diccionario in lista:
        for key, value in diccionario.items(): #Usamos el método items para en cada contador obtener las keys y los values
            if value == valor: #Si coincide el valor, entonces modificamos por el nuevo
                diccionario[key]=nuevovalor
                cambios += 1
            else:
                continue
    return (cambios,valor,nuevovalor)
#Aquí vienen algunos reseteadores por si se quieren hacer algunas pruebas, estos devuelven a los valores a sus valores iniciales, pues como las listas y diccionarios son mutables, hay que devolverlos a su inicio para que coincidan los resultados con los del ejemplo, para no acumular cambios más que nada.
def resetearx():
    imagen = [ [5,2,3], [10,8,9] ]
    print("Tu variable ha sido reseteada a su valor inicial para proseguir con los siguientes ejercicios")
    return imagen
def resetearImagen():
    imagen = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'}
    ]
    print("Tu variable ha sido reseteada a su valor inicial para proseguir con los siguientes ejercicios")
    return imagen
def resetearDirectorio():
    imagen = {
        'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
        'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
    }
    print("Tu variable ha sido reseteada a su valor inicial para proseguir con los siguientes ejercicios")
    return imagen
def resetearZ():
    imagen = [ {'x': 10, 'y': 20} ]
    print("Tu variable ha sido reseteada a su valor inicial para proseguir con los siguientes ejercicios")
    return imagen

def run():
    x = [ [5,2,3], [10,8,9] ] 
    estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'}
    ]
    directorio_deportes = {
        'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
        'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
    }
    z = [ {'x': 10, 'y': 20} ]
    #Cambiar índice de lista dentro de lista, para esto puedo ponerle inputs y definir cada parámetro de cambio
    cambios = cambiarIndiceAdentro(x,10,15)
    print(f"Tu nueva lista es {x}, y se le hicieron {cambios[0]} cambios, de las coincidencias de {cambios[1]} a {cambios[2]}")
    #Cambiar diccionario dentro de lista
    cambios2 = cambiarKeyEnLista(estudiantes, 'last_name', 'Jordan', 'Bryant')
    print(f"Tu nueva lista es {estudiantes}, y se le hicieron {cambios2[0]} cambios, de las coincidencias de {cambios2[1]} a {cambios2[2]}")
    #Cambiar lista dentro de key de diccionario
    cambios3 = cambiarValorListaDiccionario(directorio_deportes, 'fútbol', 'Messi', 'Andrés')
    print(f"Tu nuevo diccionario es {directorio_deportes}, y se le hicieron {cambios3[0]} cambios, de las coincidencias de {cambios3[1]} a {cambios3[2]}")
    #Cambiar diccionario dentro de lista
    cambios4 = cambiarDiccionarioDentroDeListaPorValorEntero(z,20,30)
    print(f"Tu nueva lista es {z}, y se le hicieron {cambios4[0]} cambios, de las coincidencias de {cambios4[1]} a {cambios4[2]}")

if __name__ == '__main__':
    run()
