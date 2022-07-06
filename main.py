lista=[]
for i in range(5):
    numero = int(input("Introduce un número: "))
    lista.append(numero)
print(lista)

# funcion suma
def suma(lista):
    suma = 0
    for i in range(5):
        suma += lista[i] 
    return suma

# funcion promedio
def promedio(lista):
    promedio = suma(lista)/len(lista)    
    return promedio

def main():
    print("El resultado de la suma es: ", suma(lista))
    print("El resultado del promedio es: ", promedio(lista))
    

main()