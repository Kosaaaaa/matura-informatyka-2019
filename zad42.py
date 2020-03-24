def silnia(liczba:str):
    silnieCyfr = []
    for cyfra in liczba:
        cyfra = int(cyfra)
        silnia = 1
        # if cyfra == 0:
        #     silnieCyfr.append(silnia)
        #     continue
        for i in range(1,cyfra+1):
            silnia *= i
        silnieCyfr.append(silnia)
    sumaSilni = sum(silnieCyfr)
    if sumaSilni == int(liczba):
        #print('rowna')
        return True
    #print('suma', sumaSilni)
    return False

counter = 0
poprawneSilnie = []
with open('./Dane_PR2/liczby.txt', 'r') as fileInput:
    for line in fileInput.readlines():
        if silnia(line.rstrip()):
            counter += 1
            # poprawneSilnie.append(int(line))
            poprawneSilnie.append(line)

with open('wyniki4.txt', 'a') as fileOutput:
    fileOutput.write('4.2: \n')
    fileOutput.writelines(poprawneSilnie)
