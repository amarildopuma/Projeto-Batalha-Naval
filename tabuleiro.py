import random

def gerar_tabuleiro(tamanho):
    tabuleiro = []
    for i in range(tamanho):
        linha_atual = []
        for j in range(tamanho):
            linha_atual.append('~')
        tabuleiro.append(linha_atual)

    return tabuleiro

def organizar_tabuleiro(tabuleiro, tamanho):
    print("   A B C D E F G H I J")
    for i in range(tamanho):
        print(f"{i + 1:>2}", end=" ")
        for j in range(tamanho):
            print(tabuleiro[i][j], end=" ")
        print()
    return tabuleiro

def atirar(tabuleiro, navios, linha, coluna):
    if tabuleiro[linha][coluna] == 'N':
        tabuleiro[linha][coluna] = 'X'

        for navio in navios:
            if(linha,coluna) in navio["posicao"]:
                navio["atingidos"].append((linha,coluna))
                if len(navio["atingidos"]) == navio["tamanho"]:
                    return "afundou"
                else:
                    return "acertou"


    elif tabuleiro[linha][coluna] == '~':
        tabuleiro[linha][coluna] = 'O'
        return "agua"

def organizar_tabuleiro_oculto(tabuleiro, tamanho):
    print("   A B C D E F G H I J")
    for i in range(tamanho):
        print(f"{i + 1:>2}", end=" ")
        for j in range(tamanho):
            celula = tabuleiro[i][j]
            if celula == 'N':
                celula = '~'
            print(celula, end=" ")
        print()