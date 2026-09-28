import random
from tabuleiro import gerar_tabuleiro
from navios import posicionar_navio

def jogada_computador(tabuleiro_alvo):
    while True:
        linha = random.randint(0, len(tabuleiro_alvo) - 1)
        coluna = random.randint(0, len(tabuleiro_alvo) - 1)
        if tabuleiro_alvo[linha][coluna] in ('~', 'N'):
            return linha, coluna

def criar_computador():
    tabuleiro = gerar_tabuleiro(10)
    tabuleiro, navios = posicionar_navio(tabuleiro, 10)
    computador = {"nome": "Computador", "tabuleiro": tabuleiro, "navios": navios, "acertos": 0, "jogadas": 0}
    return computador