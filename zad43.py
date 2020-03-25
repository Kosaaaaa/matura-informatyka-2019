def GCD(a,b):
    while a%b != 0:
        r = a%b
        a = b
        b = r
    return b
numbers = []
with open('./Dane_PR2/liczby.txt', 'r') as fileInput:
    for line in fileInput.readlines():
        numbers.append(int(line.rstrip()))

N = len(numbers)        
dividerMax = 0
firstNumMax = 0
lengthMax = 0

for j in range(N-1):
    length = 1
    firstNum = numbers[j]
    localGCD = numbers[j]
    for i in range(j+1, N):
        n = GCD(localGCD, numbers[i])
        if n > 1:
            localGCD = n
            length += 1
        if n==1 or i == N-1:
            if lengthMax < length:
                dividerMax = localGCD
                lengthMax = length
                firstNumMax = firstNum
            break
print(firstNumMax, lengthMax, dividerMax)
with open('wyniki4.txt', 'a', encoding='utf-8') as fileOutput:
    fileOutput.write('4.3: \n')
    fileOutput.write(f'Pierwsza liczba: {firstNumMax} \n')
    fileOutput.write(f'Długość ciągu: {lengthMax} \n')
    fileOutput.write(f'Dzielnik: {dividerMax} \n')
