while True:
    numero_entrada = list()
    entrada = list(map(str, input().split()))
    if entrada == ['0', '0']:
        break
    for i in entrada[1]:
        numero_entrada.append(int(i))

    num_saida = list(filter(lambda x: x != int(entrada[0]), numero_entrada))

    if num_saida.count(0) == len(num_saida):
        print(0)

    else:
        print(*num_saida, sep='')
