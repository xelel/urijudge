from math import trunc

num_str = int(input())
valores_cripto = list()


for i in range(num_str):

    entrada = str(input())
    cripto1_str = ''
    cripto2_str = ''
    for l in entrada:
        if 65 <= ord(l) <= 90 or 97 <= ord(l) <= 122:
            letra_deslocada = ord(l)+3
            cripto1_str += chr(letra_deslocada)
        else:
            cripto1_str += l
    cripto1_str = cripto1_str[::-1]
    tamanho_str = len(cripto1_str)
    meio_str = trunc(tamanho_str/2)

    for indice, letra in enumerate(cripto1_str):
        if indice >= meio_str:
            deslocamento = ord(letra)-1
            cripto2_str += chr(deslocamento)
        else:
            cripto2_str += letra

    valores_cripto.append(cripto2_str)

for val in valores_cripto:
    print(val)
