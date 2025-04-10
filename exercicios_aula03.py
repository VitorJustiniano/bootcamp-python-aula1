import random


### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.

quantidade = 40
preco = 20

if quantidade > 0 and preco > 0:
    print("valores validos")
else:
    print("valores invalidos")

### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

temperatura = 0
if temperatura < 18:
    print("baixa")
elif temperatura <= 25:
    print("alta")
else: 
    print("normal")

### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

log = {'timestamp': '2021-06-23 10:00:00','level': 'ERROR','message': 'Falha na conexão'}
if log["level"] == 'ERROR':
    print(log["message"])

### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

try:
    idade = int(input("digite sua idade: "))
    email = input("digite email: ")

    if idade >= 18 and idade <= 65:
        print("idade valida")
    else:
        raise ValueError("Idade fora da faixa permitida (18-65).")
    
    if "@" not in email or len(email.strip()) == 0:
        raise ValueError("E-mail inválido! Deve conter '@' e não pode estar vazio.")
    else:
        print("email válido:", email)
except ValueError as e:
    print(e)

### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

transacao = {'valor': 12000, 'hora': 20}
if transacao["valor"] > 10000 or transacao["hora"] < 9 or transacao["hora"]> 18:
    print("transação suspeita")


### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

texto = "hoje e nossa segunda aula do bootcamp , bootcamp de python"
novo_texto = texto.replace(",","")
palavras = novo_texto.split(" ")
print(palavras)
contagem_palavras = {}
for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] = +1
    else:
        contagem_palavras[palavra] = 1

### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

numeros = [5, 10, 15]

minimo = min(numeros)
maximo = max(numeros)

# Passo 2: criar nova lista com os números normalizados
normalizados = []
for numero in numeros:
    normalizado = (numero - minimo) / (maximo - minimo)
    normalizados.append(normalizado)

# Exibir resultado
print("Lista original:", numeros)
print("Lista normalizada:", normalizados)

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

# Lista de usuários (cada um é um dicionário)
usuarios = [
    {'nome': 'Ana', 'email': 'ana@gmail.com'},
    {'nome': 'Bruno'},  # falta o email
    {'nome': 'Carla', 'email': 'carla@hotmail.com'},
    {'email': 'daniel@outlook.com'}  # falta o nome
]

# Verifica quais usuários estão com dados faltando
print("Usuários com dados faltando:")

for usuario in usuarios:
    if 'nome' not in usuario or 'email' not in usuario:
        print(usuario)


### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.
numeros = [2, 5, 7, 9, 10, 12, 18]

for numero in numeros:
    if numero % 2 == 0:
        print("numero par: ", numero)

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

vendas = [
    {'categoria': 'Frutas', 'valor': 100},
    {'categoria': 'Verduras', 'valor': 50},
    {'categoria': 'Frutas', 'valor': 75},
    {'categoria': 'Laticínios', 'valor': 200},
    {'categoria': 'Frutas', 'valor': 25},
    {'categoria': 'Verduras', 'valor': 60}
]

totais_cada_categoria = {}

for venda in vendas:
    categoria = venda["categoria"]
    valor = venda["valor"]

    if categoria in totais_cada_categoria:
        totais_cada_categoria[categoria] += valor
    else:
        totais_cada_categoria[categoria] = valor

# Mostrar os totais por categoria
print("Total de vendas por categoria:")
for catego, total in totais_cada_categoria.items():
    print(f"{catego}: R$ {total}")

### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.
print("Digite algo( ou 'sair' para encerrar)")
entrada = ""
while entrada != "sair":
    entrada = input("Entrada: ")

    if entrada != "sair":
        print("Você digitou:", entrada)

print("Programa encerrado.")


### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.
min_valor = 1
max_valor = 10

while True:
    try:
        numero = int(input(f"digite um numero entre {min_valor} e {max_valor}: "))
        if numero >= min_valor and numero <= max_valor:
            print("numero valido: ", numero)
            break
        else:
            print("Número fora do intervalo. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

# Simulando páginas de uma API (cada item é uma "página" com dados)
paginas = [
    ["produto1", "produto2", "produto3"],
    ["produto4", "produto5"],
    [],  # Página vazia indica que acabou
]

pagina_atual = 0

# Loop até encontrar uma página vazia
while True:
    dados = paginas[pagina_atual]

    if not dados:
        print("Fim das páginas. Nenhum dado restante.")
        break

    print(f"Processando página {pagina_atual + 1}:")
    for item in dados:
        print(" -", item)

    pagina_atual += 1

### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

max_tentativas = 5
tentativas = 0

conectado = False

while tentativas < max_tentativas and not conectado:
    print(f"Tentativa {tentativas + 1} de conexão...")
    
    # Simulando sucesso aleatório (só para treino)
    if random.choice([True, False]):
        print("Conexão bem-sucedida!")
        conectado = True
    else:
        print("Falha na conexão.")
        tentativas += 1

if not conectado:
    print("Número máximo de tentativas atingido. Conexão não estabelecida.")


### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.

dados = [10, 20, 30, 40, "FIM", 50, 60]

for item in dados:
    if item == "FIM":
        print("Parada encontrada. Encerrando processamento.")
        break
    print("Processando item:", item)