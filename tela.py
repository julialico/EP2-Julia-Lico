RESET = '\033[0m'
VERDE = '\033[92m'
VERMELHO = '\033[91m'
AMARELO = '\033[93m'
CIANO = '\033[96m'
AZUL = '\033[94m'
NEGRITO = '\033[1m'
 
 
def escreve(texto, cor=RESET):
    print(cor + texto + RESET)
 
 
def escreveerro(texto):
    escreve(texto, VERMELHO)
 
 
def escrevesucesso(texto):
    escreve(texto, VERDE)
 
 
def escreveaviso(texto):
    escreve(texto, AMARELO)
 
 
def escreveinfo(texto):
    escreve(texto, CIANO)
 
 
def escrevepremio(valorpremio):
    if valorpremio >= 500000:
        cor = NEGRITO + VERMELHO
    elif valorpremio >= 100000:
        cor = NEGRITO + AMARELO
    elif valorpremio >= 30000:
        cor = NEGRITO + CIANO
    else:
        cor = NEGRITO + VERDE
 
    texto = 'PREMIO ATUAL: R$ ' + formatamoeda(valorpremio)
    escreve(texto, cor)
 
 
def formatamoeda(valor):
    textovalor = str(valor)
    invertido = textovalor[::-1]
    partes = []
    inicio = 0
    while inicio < len(invertido):
        partes.append(invertido[inicio:inicio + 3])
        inicio = inicio + 3
    resultado = '.'.join(partes)
    return resultado[::-1]
 
 
def exibemanual():
    escreve('==========================================', AZUL)
    escreve('           JOGO DA FORTUNA DESSOFT         ', AZUL + NEGRITO)
    escreve('==========================================', AZUL)
    escreveinfo('Responda as perguntas corretamente para aumentar seu premio!')
    escreveinfo('A cada pergunta existem 4 alternativas: A, B, C ou D.')
    escreveinfo('Voce tambem pode digitar:')
    escreveinfo('  PULA  -> pula para outra pergunta (tem 3 pulos no total)')
    escreveinfo('  AJUDA -> elimina 1 ou 2 alternativas erradas (tem 2 ajudas no total)')
    escreveaviso('Se errar uma resposta, voce perde TUDO e o jogo acaba!')
    escreveaviso('Ao acertar, voce sempre pode escolher parar e sair com o premio conquistado.')
    escreve('==========================================', AZUL)
 
 
def exibeestado(nomejogador, premioatual, pulosrestantes, ajudasrestantes):
    escreve('')
    escreve('Jogador: ' + nomejogador, CIANO)
    escrevepremio(premioatual)
    escreveinfo('Pulos restantes: ' + str(pulosrestantes) + ' | Ajudas restantes: ' + str(ajudasrestantes))