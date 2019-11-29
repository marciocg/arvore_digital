import time, string

# Define uma classe com a estrutura de nó da árvore digital, usando dicionário
class ArvNode:
  filho = {}
  fimpalavra = False
  def __init__(self):
    self.filho = {}
    self.fimpalavra = False
    self.contador = 0

raiz = ArvNode()     # cria nó raiz vazio

def insere(palavra):
  atual = raiz
  for i in range(len(palavra)):
    if palavra[i] not in atual.filho:       # procura cada letra da palavra
      node = ArvNode()                   # cria nó vazio 
      atual.filho[palavra[i]] = node     # insere o nó no filho 
    else:
      node = atual.filho[palavra[i]]     # vincula o filho ao nó
    atual = node
  atual.fimpalavra = True
  atual.contador += 1

def busca(palavra,raiz):
  atual  = raiz
  for i in range(len(palavra)):
    if palavra[i] not in atual.filho:
      return {palavra : "- palavra não encontrada"}
    else:
      node = atual.filho[palavra[i]]
    atual = node
  return {palavra + " encontrada" : atual.fimpalavra,"Qt. de ocorrências" : atual.contador}


iniciots = time.process_time()
print("Lendo a base...")
base = open("dracula.txt","r+",encoding="utf8")
texto = base.read()
#print(texto)

texto = texto.translate((str.maketrans("","", string.punctuation)))

palavras = texto.split()
print("Calculando o nro. de palavras")
print("Nro. de palavras: " + str(len(palavras)))
print(">>TEMPO 1: "+str(time.process_time() - iniciots))

criats = time.process_time()
print("Criando a estrutura de dados...")
for palavra in palavras:
  insere(palavra)
print("Árvore digital criada com sucesso.")
print(">>TEMPO 2: "+str(time.process_time() - criats))

inpbusca = 0

while inpbusca != '':
  inpbusca = input("Palavra para busca (ENTER p/ sair): ")
  buscats = time.process_time()
  if inpbusca != '':
    print('>>TEMPO 3 TS inicio da busca:', buscats)
    print(busca(inpbusca,raiz))
    print(">>TEMPO 4: "+str(time.process_time() - buscats))
  else:
    print("Programa encerrado.")



















"""
insere("ABA")
insere("OBA")
insere("ABEL")
insere("ABERTO")
insere("ABRIR")
insere("ABRIL")
print(busca("ABERTO",raiz))
print(busca("ABRIR",raiz))
print(busca("ABE",raiz))
print(busca("RIR",raiz))
printArv(raiz)

"""


