import re
cmd_prompt = int(input("Digite um numero de [ 1 a 52 ]: "))
def matriz(n):
    Alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    camadas = []
    camada_temporaria = []
    formula = 2 * n + 1
    for i in range(n):
        camada_temporaria.insert(i, Alfabeto[i])
        camada_temporaria.insert(-i, Alfabeto[i])
        c = camada_temporaria.copy()
        while len(c) < formula:
            c.insert(i, Alfabeto[i])
        camadas.append(c)
    meio = camadas[n-1].copy()
    meio.pop(n)
    meio.insert(n, '*')
    for camada in camadas:
        print(re.sub('[^a-zA-Z]', ' ', str(camada)))
    print(re.sub('[^a-zA-Z-*]', ' ', str(meio)))
    camadas.reverse()
    for camada in camadas:
        print(re.sub('[^a-zA-Z]', ' ', str(camada)))
if 1  <= cmd_prompt and cmd_prompt <= 52:
    print()
    matriz(cmd_prompt)
else:
    print("Numero invalido, por favor digite um numero valido de 1 a 52")