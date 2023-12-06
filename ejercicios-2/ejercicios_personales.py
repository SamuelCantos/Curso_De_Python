#repitiendo los ejercicios pero esta vez a mi manera y sin verlos resueltos


# pedir la edad de los companeros que vinieron hoy a clase y ordenar los datos de mayor a menor 

companeros = []
def sort_companeros(cantidad_compas):
    for i in range (cantidad_compas):
        nombre = input('ingrese el nombre del compa: ')
        edad = int(input('ingrese la edad del compa: '))
        companero = (nombre, edad)
        companeros.append(companero)
    companeros.sort(key=lambda x:x[1])
    profesor = companeros[-1][0]
    asistente = companeros[0][0]
    return print(f'el profesor seria:{profesor} y el asistente seria: {asistente}')
 
#sort_companeros(3)

#crear una funcion que despues de pasarle un numero te devuelva todos los numeros primos hasta llegar a si mismo

def es_primo (num):
    print('entro')
    # iteramos el numero para buscar que sea divisible solamente por si mismo y por 1
    for i in range(2,num-1):
        if num % i == 0:
            return False
        return True

def primos_hasta (num):
    #creamos una lista vacia para guardar los numeros primos que se vayan encontrando
    numeros = []
    #iteramos desde el 0 al numero para buscar cuales son primos llamando a la funcion es_primo
    for i in range (num + 1):
        resultado = es_primo(i)
        #si la funcion es_primo da true en alguno de los numeros lo agregamos a la lista, de lo contrario no se agrega
        if resultado == True:
           numeros.append(i)
    return print(numeros)

primos_hasta(17)
           
    
    
        



        
        
   
