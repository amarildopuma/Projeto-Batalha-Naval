import json
import os

CAMINHO_REPLAY = "data/ultimo_replay.json"

def registrar_jogada(historico, jogador_nome, coordenada, resultado):
    historico.append({"jogador": jogador_nome, "coordenada": coordenada, "resultado": resultado})

def salvar_replay(historico):
    os.makedirs("data", exist_ok=True)
    with open(CAMINHO_REPLAY, "w") as arquivo:
        json.dump(historico, arquivo, indent=2)

def reproduzir_replay():
    if not os.path.exists(CAMINHO_REPLAY):
        print("Nenhum replay disponivel ainda.\n")
        input("Pressione ENTER para voltar ao menu...")
        return

    with open(CAMINHO_REPLAY, "r") as arquivo:
        historico = json.load(arquivo)

    print("Reproduzindo replay da ultima partida...\n")
    for i, jogada in enumerate(historico, start=1):
        print(f"Jogada {i:02}/{len(historico)} - {jogada['jogador']} - {jogada['coordenada']} - {jogada['resultado']}")
        input("[ENTER] Proxima jogada")
    print("\nFim do replay.\n")
    input("Pressione ENTER para voltar ao menu...")