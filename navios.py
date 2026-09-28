import random

def gerar_posicoes(linha, coluna, tamanho_dos_navios, direcao):
    navio=[]
    if direcao == 1:#vertical
        for i in range(tamanho_dos_navios):
            navio.append((linha+i,coluna))
    if direcao == 2:#horizontal 
        for i in range(tamanho_dos_navios):
            navio.append((linha,coluna+i))
    return navio

def posicoes_disponiveis(tabuleiro, navio):
    for posicao in navio:
        if (posicao[0] > (len(tabuleiro)-1)
        or posicao[1] > (len(tabuleiro)-1)):
            return False
        elif tabuleiro[posicao[0]][posicao[1]] != '~':
            return False
    return True

def posicionar_navio(tabuleiro, tamanho_do_tabuleiro):
    navios = []

    loop = 0
    while loop < 4:
        linha = random.randint(0, tamanho_do_tabuleiro-1)
        coluna = random.randint(0, tamanho_do_tabuleiro-1)
        direcao = random.randint(1, 2)
        navio = gerar_posicoes(linha, coluna, 2, direcao)
        if posicoes_disponiveis(tabuleiro, navio):
            for posicao in navio:
                tabuleiro[posicao[0]][posicao[1]] = 'N'
            navios.append({"tamanho": 2, "posicao": navio, "atingidos": []})
            loop += 1

    loop = 0
    while loop < 2:
        linha = random.randint(0, tamanho_do_tabuleiro-1)
        coluna = random.randint(0, tamanho_do_tabuleiro-1)
        direcao = random.randint(1, 2)
        navio = gerar_posicoes(linha, coluna, 4, direcao)
        if posicoes_disponiveis(tabuleiro, navio):
            for posicao in navio:
                tabuleiro[posicao[0]][posicao[1]] = 'N'
            navios.append({"tamanho": 4, "posicao": navio, "atingidos": []})
            loop += 1

    return tabuleiro, navios