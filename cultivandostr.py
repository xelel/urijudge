while True:

    num_str = int(input())
    string = list()
    if num_str == 0:
        break

    for i in range(num_str):
        entrada = str(input())
        string.append(entrada)

    string = iter(string)
    count = set()
    try:
        str_geradora = next(string)
        count.add(str_geradora)
        str_filha = next(string)
        # se a string cresce a partir da extremidade obrigatoriamente o ultimo ou o primeiro caractere deve estar contido na filha
        # se a string é originada a partir do meio voce deve checar apenas se a filha é uma substring da mae
        if str_geradora.endswith()
        for s in string:
            pass
    finally:
        print(count)
        print(len(count))
