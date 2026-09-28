def menu_do_jogo():
    print("===============================")
    print("\nBATALHA NAVAL - AMARILDO JUNIOR\n")
    print("===============================")
    print("1- Nova Partida")
    print("2- Ver Estatisticas")
    print("3- Assistir replay da ultima partida")
    print("4- Creditos")
    print("5- Sair")
    return input("Digite a opcao desejada: ")

def selecao_do_modo():
    print(" Selecione o modo de jogo:")
    print("1- Jogador x Jogador")
    print("2- Jogador x Computador")
    print("0- Voltar ao menu principal  ")
    return input("Escolha o modo de jogo: ")

def exibir_creditos():
    print("===============================")
    print("BATALHA NAVAL - AMARILDO JUNIOR")
    print("Desenvolvido por Amarildo Junior")
    print("CEFET-MG - Campus Divinopolis")
    print("Disciplina: Programacao em Python")
    print("Professor: Guido Pantuza")
    print("===============================\n")
    input("Pressione ENTER para voltar ao menu...")