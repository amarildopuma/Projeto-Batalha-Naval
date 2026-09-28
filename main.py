from utils import coordenada_valida, conversor_coordernada, limpar_tela, coordenada_str
from tabuleiro import organizar_tabuleiro, gerar_tabuleiro, atirar, organizar_tabuleiro_oculto
from navios import gerar_posicoes, posicoes_disponiveis, posicionar_navio
from jogador import criar_jogador, pedir_jogada, realizar_jogada, jogador_perdeu
from menu import menu_do_jogo, selecao_do_modo, exibir_creditos
from computador import jogada_computador, criar_computador
from estatisticas import registrar_estatistica, exibir_estatisticas
from replay import registrar_jogada, salvar_replay, reproduzir_replay


def jogar_turno_humano(atacante, alvo, historico):
    limpar_tela()
    print(f"===== VEZ DE {atacante['nome'].upper()} =====\n")
    print(f"Mapa atual do {alvo['nome']}:\n")
    organizar_tabuleiro_oculto(alvo["tabuleiro"], 10)
    print()

    while True:
        jogada = pedir_jogada(atacante["nome"])
        resultado = realizar_jogada(atacante, alvo, jogada[0], jogada[1])

        if resultado == "repetida":
            print("\nPosicao repetida, escolha outra jogada.\n")
            continue

        coordenada_texto = coordenada_str(jogada[0], jogada[1])
        registrar_jogada(historico, atacante["nome"], coordenada_texto, resultado)

        if resultado == "afundou":
            print("\nVoce afundou um navio!")
        elif resultado == "acertou":
            print("\nVoce acertou um navio!")
        else:
            print("\nVoce errou (agua).")

        if jogador_perdeu(alvo):
            return True

        if resultado == "agua":
            return False

        print(f"\nVoce joga novamente! Mapa atual do {alvo['nome']}:\n")
        organizar_tabuleiro_oculto(alvo["tabuleiro"], 10)


def jogar_turno_computador(atacante, alvo, historico):
    print(f"\n===== VEZ DO {atacante['nome'].upper()} =====")

    while True:
        linha, coluna = jogada_computador(alvo["tabuleiro"])
        resultado = realizar_jogada(atacante, alvo, linha, coluna)
        coordenada_texto = coordenada_str(linha, coluna)
        registrar_jogada(historico, atacante["nome"], coordenada_texto, resultado)

        if resultado == "afundou":
            print(f"O Computador afundou um navio seu em {coordenada_texto}!")
        elif resultado == "acertou":
            print(f"O Computador acertou um navio seu em {coordenada_texto}!")
        else:
            print(f"O Computador errou em {coordenada_texto} (agua).")

        if jogador_perdeu(alvo):
            return True

        if resultado == "agua":
            input("\nPressione ENTER para continuar...")
            return False


def jogar_partida_jxj():
    historico = []
    print("==== DADOS DO JOGADOR 1 ====")
    jogador1 = criar_jogador()
    print("==== DADOS DO JOGADOR 2 ====")
    jogador2 = criar_jogador()
    print("==== O JOGO VAI COMECAR ====\n")
    input("Pressione ENTER para comecar...")

    vez_de_quem = "jogador1"
    vencedor = None
    while vencedor is None:
        if vez_de_quem == "jogador1":
            venceu = jogar_turno_humano(jogador1, jogador2, historico)
            if venceu:
                vencedor = jogador1
            else:
                vez_de_quem = "jogador2"
                input("\nPressione ENTER para passar a vez...")
        else:
            venceu = jogar_turno_humano(jogador2, jogador1, historico)
            if venceu:
                vencedor = jogador2
            else:
                vez_de_quem = "jogador1"
                input("\nPressione ENTER para passar a vez...")

    limpar_tela()
    print(f"Parabens {vencedor['nome']}, voce ganhou a batalha!!!\n")
    salvar_replay(historico)
    registrar_estatistica(jogador1, jogador2, vencedor)
    input("Pressione ENTER para voltar ao menu...")


def jogar_partida_jxc():
    historico = []
    print("==== DADOS DO JOGADOR ====")
    jogador1 = criar_jogador()
    print("==== DADOS DO COMPUTADOR ====")
    jogador2 = criar_computador()
    print("Computador gerado e navios posicionados com sucesso!")
    input("Pressione ENTER para comecar...")

    vez_de_quem = "jogador1"
    vencedor = None
    while vencedor is None:
        if vez_de_quem == "jogador1":
            venceu = jogar_turno_humano(jogador1, jogador2, historico)
            if venceu:
                vencedor = jogador1
            else:
                vez_de_quem = "computador"
        else:
            venceu = jogar_turno_computador(jogador2, jogador1, historico)
            if venceu:
                vencedor = jogador2
            else:
                vez_de_quem = "jogador1"

    limpar_tela()
    print(f"Parabens {vencedor['nome']}, voce ganhou a batalha!!!\n")
    salvar_replay(historico)
    registrar_estatistica(jogador1, jogador2, vencedor)
    input("Pressione ENTER para voltar ao menu...")


while True:
    limpar_tela()
    escolha = menu_do_jogo()

    if not escolha.isdigit():
        print("Opcao invalida.")
        input("Pressione ENTER para continuar...")
        continue

    escolha = int(escolha)

    if escolha == 1:
        limpar_tela()
        modo = selecao_do_modo()
        if not modo.isdigit():
            continue
        modo = int(modo)

        if modo == 0:
            continue
        elif modo == 1:
            limpar_tela()
            jogar_partida_jxj()
        elif modo == 2:
            limpar_tela()
            jogar_partida_jxc()
        else:
            print("Opcao invalida.")
            input("Pressione ENTER para continuar...")

    elif escolha == 2:
        limpar_tela()
        exibir_estatisticas()

    elif escolha == 3:
        limpar_tela()
        reproduzir_replay()

    elif escolha == 4:
        limpar_tela()
        exibir_creditos()

    elif escolha == 5:
        print("Ate a proxima!")
        break

    else:
        print("Opcao invalida.")
        input("Pressione ENTER para continuar...")