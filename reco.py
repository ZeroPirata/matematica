def taylor(x):
    somador = 1
    i = 1
    R = x * 3.1415/180
    b = 1
    menosUm = -1

    while i <= x :       
        b = b * (2*i-1) * (2*i)
        somador = somador + menosUm * R **(2*i)/b
        menosUm = -1*menosUm
        i+=1
    print(f'{somador:.3f}')
    
inteiro = int(input('Digite o numero: '))
taylor(inteiro)
