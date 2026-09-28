import json
import os

CAMINHO_ESTATISTICAS = "data/estatisticas.json"

def registrar_estatistica(jogador1, jogador2, vencedor):
    os.makedirs("data", exist_ok=True)
    if os.path.exists(CAMINHO_ESTATISTICAS):
        with open(CAMINHO_ESTATISTICAS, "r") as arquivo:
            historico = json.load(arquivo)
    else:
        historico = []

    registro = {
        "jogador1": {"nome": jogador1["nome"], "jogadas": jogador1["jogadas"], "acertos": jogador1["acertos"]},
        "jogador2": {"nome": jogador2["nome"], "jogadas": jogador2["jogadas"], "acertos": jogador2["acertos"]},
        "vencedor": vencedor["nome"],
    }
    historico.append(registro)

    with open(CAMINHO_ESTATISTICAS, "w") as arquivo:
        json.dump(historico, arquivo, indent=2)

def exibir_estatisticas():
    if not os.path.exists(CAMINHO_ESTATISTICAS):
        print("Nenhuma partida registrada ainda.\n")
        input("Pressione ENTER para voltar ao menu...")
        return

    with open(CAMINHO_ESTATISTICAS, "r") as arquivo:
        historico = json.load(arquivo)

    total_partidas = len(historico)
    total_jogadas = 0
    total_acertos = 0
    for partida in historico:
        total_jogadas += partida["jogador1"]["jogadas"] + partida["jogador2"]["jogadas"]
        total_acertos += partida["jogador1"]["acertos"] + partida["jogador2"]["acertos"]

    print("===== ESTATISTICAS GERAIS =====")
    print(f"Partidas registradas: {total_partidas}")
    print(f"Total de jogadas: {total_jogadas}")
    print(f"Total de acertos: {total_acertos}")
    print("================================\n")
    input("Pressione ENTER para voltar ao menu...")