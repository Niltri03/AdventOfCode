
FILENAME = 'day1data.txt'
rotaciones = []


with open(FILENAME, 'r', encoding="utf-8") as datafile: 
        dial = 50
        retVal = 0
        for row in datafile:
            elem = ""
            for i in range(1, len(row)): 
                elem += row[i]
            giro = int(elem)
            
            print(dial)
            #Calculamos giros
            if(row[0] == 'L'):
                for i in range(0, giro):
                    dial -= 1
                    if(dial == -1): dial = 99
                    if(dial == 0): retVal += 1
            elif(row[0] == 'R'):
                for i in range(0, giro):
                    dial += 1
                    if(dial == 100): dial = 0
                    if(dial == 0): retVal += 1
            
              

        print("retVal " + str(retVal))

