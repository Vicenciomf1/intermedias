def iterateDictionary(lista):
    for diccionario in lista: #Recorre la lista para encontrar cada diccionario
        a='' #Creamos esta string solita para que nos quede todo en una sola línea en vez de en dos.
        for key, value in diccionario.items(): #Usamos el método items para en cada contador obtener las keys y los values
            a+=f"{key} - {value}, " #Y los vamos concatenando de a poquito
        print(a[:-2]) #Al final, quedará un resto de coma y espacio, que lo eliminamos fácilmente con un slice.
def iterateDictionary2(key_name, some_list):
    for diccionario in some_list: #Saca cada diccionario de la lista
        for key, value in diccionario.items(): #Separamos cada pay key-valor en dos contadores
            if key == key_name: #Si el contador de la key coincide con el nombre, entonces printea el valor del par clave-valor
                print(value)

def run():
    estudiantes = [
            {'first_name':  'Michael', 'last_name' : 'Jordan'},
            {'first_name' : 'John', 'last_name' : 'Rosales'},
            {'first_name' : 'Mark', 'last_name' : 'Guillen'},
            {'first_name' : 'KB', 'last_name' : 'Tonel'}
        ]
    iterateDictionary2('last_name', estudiantes) 

if __name__ == '__main__':
    run()

