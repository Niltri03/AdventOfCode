

false = False
true = True
count = 0


def calc(curInt): 
    
    
    for block in range(2, int(len(curInt)/2)+1):
        
        if(len(curInt) % block == 0): 
            referencia = curInt[:block]
            bloques = int(len(curInt)/block)
            secciones = []
            for i in range(1, bloques): secciones.append(curInt[block*i:block*i+block])
            print(str(curInt) + " se divide en " + str(referencia) + " y ")
            print(secciones)

    for i in range(1, len(curInt)): 
        if(curInt[i] != curInt[0]): return false
    print("hit impar: " + str(curInt))
    return true



def splitter(valor):
    aux = -1
    for i in range(0, len(valor)): 
        if(valor[i] == '-'): 
            aux= i 
            break
    retval = []
    retval.append(valor[0:i])
    retval.append(valor[i+1:])
    return retval


with open("Day2Test.txt", 'r') as inp: values = inp.read().split(',')
print(values)

for valor in values: 
    points = splitter(valor)
    for i in range(int(points[0]), int(points[1])+1):
        if(calc(str(i))): count += i 

print("suma: " + str(count))