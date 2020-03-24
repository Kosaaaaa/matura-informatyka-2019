potegi = [3 ** i for i in range(11)]
counter = 0
with open('./Dane_PR2/liczby.txt', 'r') as fileInput:
    for line in fileInput.readlines():
        line = int(line)
        if line in potegi:
            counter += 1

with open('wyniki4.txt', 'w') as fileOutput:
    fileOutput.write(f'4.1:\n{counter} \n')