TESTDATA = "Day3Test.txt"
DATA = "Day3Data.txt"


#muy mejorable, podrias ignorar todos los valores inferiores al max
def maxval(pila):
    maxV = 0
    for i in range(0, len(pila)-1):
        for j in range(i+1, len(pila)):
            cur = int(pila[j])
            cur += int(pila[i])*10
            if(cur > maxV): 
                maxV = cur
    #print(maxV)
    return maxV


with open(DATA, 'r') as datos: 
    suma = 0
    for dato in datos:
        pila = dato[:-1]
        suma += maxval(pila)
    print("suma total: " + str(suma))