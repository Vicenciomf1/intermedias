def cambiarIndiceAdentro(lista, posicionpadre, posicionhija, nuevovalor):
    lista[posicionpadre][posicionhija] = nuevovalor #Tomamos la lista dentro de la lista mediante la primera indexación, y luego tomamos su índice para cambiarlo
def cambiarKey(diccionario, atributo, valor):
    diccionario[atributo] = valor #Tomamos el diccionario ya obtenido, pues mediante la indexacion ya llega el diccionario como input de esta función, luego accedemos a su atributo indexándolo con la key, y reemplazamos ese valor
def cambiarKeyAdentroDeLista(diccionario, atributo, posicionLista, valor):
    diccionario[atributo][posicionLista] = valor #Accedemos al igual que en el anterior, pero ahora agregamos la posición para acceder a la lista adentro, ojo, que la primera función también podría funcionar, cambiando valores de índices por sus keys.

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
    #Puse a las funcones así por si es que se quiere cambiar el parámetro,  ponerlos como input, para que sea algo más general y reutilizable.
    #Cambiar índice de lista dentro de lista, para esto puedo ponerle inputs y definir cada parámetro de cambio
    cambiarIndiceAdentro(x,1,0,15)
    print(x)
    #Cambiar diccionario dentro de lista
    cambiarKey(estudiantes[0], 'last_name', 'Bryant')
    print(estudiantes)
    #Cambiar lista dentro de key de diccionario
    cambiarKeyAdentroDeLista(directorio_deportes, 'fútbol', 0, 'Andrés')
    # Este también serviría, cosa que haríamos sólo dos funciones para todo el ejercicio: cambiarIndiceAdentro(directorio_deportes, 'fútbol', 0, 'Andrés')
    print(directorio_deportes)
    #Cambiar diccionario dentro de lista
    cambiarKey(z[0],'y',30)
    print(z)

if __name__ == '__main__':
    run()

