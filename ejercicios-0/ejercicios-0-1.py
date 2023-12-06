#Primeros ejercicios para agarrale la mano de nuevo a este mundo de la programacion y tambien ir practicando un poco python. Dia 27 de noviembre de 2023, miami, florida, 33141  

#1 De 2 numeros saber cual es el mayor. 

#a = input('ingresa 1 numero: ')
#b = input('ingresa otro numero y te voy a devolver cual es el mayor: ')

def obtener_mayor(a, b):
    if a > b :
        return a
    elif a < b:
        return b
    else:
        return print('los numeros que me pasaste son iguales hermano, fijate si no podes ser tan pelotudo') 

#print(obtener_mayor(a, b))

#-------------------------------------------------------------------------------------------------------------------# 

#2 Crea una variable numerica y si esta entre 0 y 10 mostra un mensaje indicandolo 

#variable_numerica = input('Escribi un numero rey, porfavor: ')

def single_num (variable_numerica):
    if int(variable_numerica) <= 10:
        return print('la variable que me pasaste se encuentra entre el 0 y el 10')
    elif int(variable_numerica) > 10:
        return print(f'la variable que me pasaste es {variable_numerica} y dejame decirte que elejiste uno de los peores numeros que lei en mi vida, gracias por participar. Espero no verte nunca mas por aqui. Gracias')
    else: 
        return print('no puedo creer que seas tan hijo de re mil culiadora y mandarme letras cuando te estoy pidiendo numeros hermano')
    
#single_num(int(variable_numerica)) 

#3 Mostrar con un while los nuermos del 1 al 100. 


def contador_while ():
        numeros = 0
        while numeros != 100:
            print(f'el numero ahora es: {numeros}')
            numeros = numeros + 1
        return print('ya llegamos a 100 ')

contador_while()

def contador_for ():
        for i in range(100):
            print(f'el numero ahora es: {i}')
            i = i + 1
        return print('ya llegamos a 100 ')

contador_for()
    
  
