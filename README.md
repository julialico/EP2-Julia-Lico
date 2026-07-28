# EP2-Julia-Lico
Exercício Programa 2 - Dessoft (DP férias)
# 🎮 Jogo da Fortuna DesSoft

O **Jogo da Fortuna DesSoft** é um jogo de perguntas e respostas desenvolvido em **Python**, inspirado em programas de perguntas e premiações, como o *Quem Quer Ser Um Milionário?*. O jogador deve responder corretamente a uma sequência de perguntas de dificuldade crescente para acumular prêmios em dinheiro, podendo decidir entre continuar jogando para ganhar mais ou encerrar a partida levando o prêmio conquistado.

## 📖 Sobre o jogo

O objetivo do jogo é responder corretamente a **9 perguntas**, divididas em três níveis de dificuldade:

- 🟢 Fácil
- 🟡 Médio
- 🔴 Difícil

Cada resposta correta aumenta o prêmio do jogador. Entretanto, caso uma resposta seja respondida incorretamente, o jogador perde todo o valor acumulado e a partida termina.

Durante o jogo, o participante conta com recursos estratégicos para aumentar suas chances de vitória.

## 🎯 Objetivo

O objetivo do projeto é simular um jogo de perguntas utilizando conceitos fundamentais de programação em Python, como:

- Manipulação de listas e dicionários;
- Validação de dados;
- Estruturas de repetição;
- Estruturas condicionais;
- Funções;
- Entrada e saída de dados pelo terminal.

## 🕹️ Como jogar

Ao iniciar o jogo:

1. Digite seu nome.
2. Leia as instruções exibidas na tela.
3. Para cada pergunta, escolha uma das opções:
   - **A**
   - **B**
   - **C**
   - **D**

Além das respostas, existem dois comandos especiais:

### PULA

Troca a pergunta atual por outra do mesmo nível.

- Disponível **3 vezes** durante a partida.

### AJUDA

Revela uma ou duas alternativas que certamente estão erradas.

- Disponível **2 vezes** durante toda a partida.
- Só pode ser utilizada uma vez por pergunta.

Após cada resposta correta, o jogador pode escolher entre:

- **CONTINUAR** jogando para tentar um prêmio maior;
- **PARAR** e sair com o valor já conquistado.

Se errar qualquer pergunta:

- O jogo termina imediatamente;
- Todo o prêmio acumulado é perdido.

## 💰 Premiação

As perguntas seguem a seguinte sequência de prêmios:

| Pergunta | Prêmio |
|----------|--------:|
| 1 | R$ 1.000 |
| 2 | R$ 5.000 |
| 3 | R$ 10.000 |
| 4 | R$ 30.000 |
| 5 | R$ 50.000 |
| 6 | R$ 100.000 |
| 7 | R$ 300.000 |
| 8 | R$ 500.000 |
| 9 | **R$ 1.000.000** |

---

# ▶️ Como executar

## Pré-requisitos

É necessário possuir o **Python 3** instalado.

Para verificar, digite no terminal:

```bash
python --version
```

ou

```bash
python3 --version
```

## Executando o jogo

Abra um terminal na pasta do projeto e execute:

```bash
python jogo.py
```

Caso seu sistema utilize o comando `python3`:

```bash
python3 jogo.py
```

## Estrutura do projeto```
.
├── jogo.py
├── funcoes.py
├── tela.py
├── baseperguntas.py
└── README.md

### jogo.py

Arquivo principal do projeto.

Responsável por:

- iniciar o jogo;
- controlar toda a partida;
- validar a base de perguntas;
- controlar prêmios;
- controlar pulos e ajudas;
- receber as respostas do jogador;
- verificar vitória ou derrota.


### funcoes.py

Contém todas as funções auxiliares utilizadas pelo jogo.

Entre elas:

- transformação da base de perguntas por nível;
- validação das perguntas;
- sorteio de perguntas;
- sorteio de perguntas inéditas;
- geração do texto das perguntas;
- geração das ajudas.


### tela.py

Responsável pela interface do terminal.

Possui funções para:

- exibir mensagens coloridas;
- mostrar o manual;
- mostrar o estado atual da partida;
- exibir o prêmio atual;
- formatar valores monetários.


### baseperguntas.py

Armazena toda a base de perguntas do jogo.

Cada pergunta é representada por um dicionário contendo:

- título;
- nível de dificuldade;
- alternativas;
- resposta correta.