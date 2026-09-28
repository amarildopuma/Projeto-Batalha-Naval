# Batalha Naval - Amarildo Junior

Projeto individual da disciplina de Programação em Python (CEFET-MG, Campus Divinópolis),
professor Guido Pantuza. Implementação do sistema de Batalha Naval em modo texto, seguindo
o Documento de Requisitos fornecido pelo professor.

## Como executar

Requisitos: Python 3.10 ou superior.

```bash
python main.py
```

O jogo abre um menu principal com as opções de nova partida, estatísticas, replay,
créditos e sair.

## Estrutura do projeto

```
BatalhaNaval/
├── main.py           # Loop principal do jogo e menu
├── menu.py           # Telas de menu e créditos
├── tabuleiro.py       # Criação, exibição (normal e oculta) e lógica de tiro
├── navios.py          # Geração de posições e posicionamento automático da frota
├── jogador.py         # Criação de jogador, leitura e validação de jogadas
├── computador.py       # Jogada automática do computador
├── estatisticas.py     # Registro e exibição de estatísticas de partidas
├── replay.py           # Registro e reprodução do histórico de jogadas
├── utils.py            # Conversão/validação de coordenadas, limpeza de tela
├── data/               # Arquivos gerados (estatísticas e replay em JSON)
└── README.md
```

## Regras implementadas

- Tabuleiro de 10x10 posições para cada jogador (colunas A-J, linhas 1-10).
- Dois tipos de navio: pequeno (2 posições) e grande (4 posições).
- Frota por jogador: 4 navios pequenos + 2 navios grandes (16 casas ocupadas no total).
  Essa quantidade não é especificada pelo enunciado; foi uma decisão de projeto para
  equilibrar desafio e duração da partida em um tabuleiro 10x10.
- Navios posicionados automaticamente (aleatório), na horizontal ou vertical, sem
  sobreposição e sem ultrapassar os limites do tabuleiro.
- Antes de cada partida, o jogador pode conferir o mapa gerado e optar por gerar outro.
- Coordenadas informadas no formato Letra+Número (ex.: C5), com validação de formato,
  limites (A-J, 1-10) e jogadas repetidas (rejeitadas sem consumir a rodada).
- Ao acertar ou afundar um navio, o jogador tem direito a uma nova jogada na mesma vez.
- Dois modos de jogo: Jogador x Computador (computador joga de forma aleatória, evitando
  repetir posições) e Dois Jogadores.
- O tabuleiro do adversário é exibido ocultando os navios ainda não atingidos.
- Estatísticas: cada partida registra jogadas e acertos dos dois jogadores e o vencedor,
  salvos em `data/estatisticas.json`. O menu exibe totais agregados de todas as partidas.
- Replay: cada jogada da última partida é registrada em `data/ultimo_replay.json` e pode
  ser reproduzida jogada a jogada.

## Decisões de projeto

- Cada jogador é representado por um dicionário (`nome`, `tabuleiro`, `navios`, `acertos`,
  `jogadas`), evitando duplicar lógica entre jogador 1, jogador 2 e computador.
- Cada navio é um dicionário (`tamanho`, `posicao`, `atingidos`); um navio é considerado
  afundado quando `len(atingidos) == tamanho`.
- As funções de exibição do tabuleiro (`organizar_tabuleiro` e `organizar_tabuleiro_oculto`)
  apenas leem a matriz e imprimem; a lógica de jogo nunca depende do que é impresso.

## Limitações conhecidas

- Interface em modo texto (sem interface gráfica).
- IA do computador é puramente aleatória (não há estratégia de perseguição após um acerto).
