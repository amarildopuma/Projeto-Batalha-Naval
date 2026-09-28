from utils import coordenada_valida, conversor_coordernada, limpar_tela
from tabuleiro import organizar_tabuleiro, gerar_tabuleiro, atirar
from navios import gerar_posicoes, posicoes_disponiveis, posicionar_navio

def criar_jogador():
    nome = input("Digite o nome do jogador: ")
    desejo = 2
    while desejo != 1:
        tabuleiro = gerar_tabuleiro(10)
        tabuleiro, navios = posicionar_navio(tabuleiro, 10)
        print("\n")
        organizar_tabuleiro(tabuleiro, 10)
        desejo = 2
        while desejo != 0 and desejo != 1:
            print("\n")
            desejo = int(input("Digite 1 se você quer esse mapa, ou 0 para gerar outro mapa: "))
            print("\n")

    jogador = {"nome": nome, "tabuleiro": tabuleiro, "navios": navios, "acertos": 0, "jogadas": 0}
    return jogador

def pedir_jogada(nome):
    jogada = input(f"Digite a sua jogada {nome} (ex: c7): ")
    while not coordenada_valida(jogada):
        jogada = input("Digite uma jogada valida!! (ex: c7): ")
    return conversor_coordernada(jogada)

def realizar_jogada(atacante, alvo, linha, coluna):
    if (alvo["tabuleiro"][linha][coluna] == 'X'
    or alvo["tabuleiro"][linha][coluna] == 'O'):
        return "repetida"
    else:
        resultado = atirar(alvo["tabuleiro"], alvo["navios"], linha, coluna)
        if resultado == "afundou":
            atacante["acertos"] += 1
            atacante["jogadas"] += 1
            return "afundou"
        elif resultado == "acertou":
            atacante["acertos"] += 1
            atacante["jogadas"] += 1
            return "acertou"
        elif resultado == "agua":
            atacante["jogadas"] += 1
            return "agua"

def jogador_perdeu(jogador):
    for navio in jogador["navios"]:
        if len(navio["atingidos"]) != navio["tamanho"]:
            return False
    return True
