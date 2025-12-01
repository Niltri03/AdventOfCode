
FILENAME = 'data1.txt'
rotaciones = []


def calculaGiro(stPos, grados): 
    endPos = stPos + grados
    if (endPos >= 100):
         endPos -= 100
    elif(endPos <= 0):
        endPos += 100
    return endPos


with open(FILENAME, 'r', encoding="utf-8") as datafile: 
        curfile = 0
        for row in datafile:
            elem = ""
            for i in range(1, len(row)): 
                elem += row[i]
            if(row[0] == 'L'): #hacia atrás
                rotaciones.append(-int(elem))
            else:#hacia adelante
                rotaciones.append(int(elem))
            print(rotaciones[curfile])
            curfile += 1
dial = 50
retVal = 0
for giro in rotaciones:
    dial += giro
    while(dial > 100): 
        dial -= 100
    while(dial < 0):
        dial += 100
    if(dial == 0 or dial == 100): 
        retVal += 1
        dial = 0
    print(dial)

print("retVal " + str(retVal))

