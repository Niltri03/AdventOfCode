



count = 0


def calc(curInt): 
    half = int(len(curInt)/2)
    return(curInt[0:half] == curInt[half:])



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
with open("Day2Input.txt", 'r') as inp: values = inp.read().split(',')
print(values)

for valor in values: 
    points = splitter(valor)
    for i in range(int(points[0]), int(points[1])+1):
        if(len(str(i)) % 2 == 0): 
            if(calc(str(i))): count += i 

print("suma: " + str(count))