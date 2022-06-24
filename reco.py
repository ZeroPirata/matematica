import re


def taylor(x):
    somador = 1
    i = 1
    R = x * 3.1415/180
    b = 1
    menosUm = -1
    while i <= x:
        b = b * (2*i-1) * (2*i)
        somador = somador + menosUm * R ** (2*i)/b
        menosUm = -1*menosUm
        i += 1
    result = []
    toString = str(somador)
    if int(toString[5]) <= 6:
        for i in range(5):
            result.append(toString[i])
    if int(toString[5]) >= 7:
        maiorQueSete = somador + 0.001
        toString = str(maiorQueSete)
        for i in range(5):
            result.append(toString[i])
    print(re.sub("[^0-1-2-3-4-5-6-7-8-9-.]", "", str(result)))


inteiro = int(input('Digite o numero: '))
taylor(inteiro)
