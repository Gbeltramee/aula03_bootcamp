### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.

quantidade = 5
preco = 10

try:    
    if quantidade > 0 and preco > 0:
        print("Dados válidos!")
    else:
        print("Dados inválidos!")
except TypeError:
    print("Digite apenas números")


### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
# Temperatura < 18°C é 'Baixa'
# Temperatura >= 18°C e <= 26°C é 'Normal'
# Temperatura > 26°C é 'Alta'

temperatura = 40
print(f"temperatura atual: {temperatura}")
try:
    if temperatura < 18:
        classificacao = "Baixa"
    elif temperatura < 26:
        classificacao = "Normal"
    else:
        classificacao = "Alta"

    print(f"A classificação da temperatura é {classificacao}")
except TypeError:
    print("Digite apenas números.")


### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

if (log['level']) == "ERROR":
    print(log['message'])

### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

idade = 19
email = "g.beltrame2112@gmail.com"

if idade < 18 and idade > 65:
    print("Idade fora do intervalo")
elif "@" not in email or "." not in email:
    print("email invalido")
else:
    print("Dados de usuários válidos")

### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

transacao = {'valor': 12000, 'hora': 20}

if transacao['valor']>10000 or transacao['hora'] < 9 or transacao['hora']>20:
    print("Transação suspeita")
else:
    print("Transação concluída")


### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

texto = "hoje é nossa segunda aula do bootcamp, bootcamp de python"
texto_novo = texto.replace(",","")
palavras = texto_novo.split()
print(palavras)

contagem_palavras = {}

for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] +=1
    else:
        contagem_palavras[palavra] = 1
print(contagem_palavras)


### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

numeros = [7, 12, 19, 21, 50]
minimo = min(numeros)
maximo = max(numeros)

normalizados = []

for numero in numeros:
    numero_normalizado = (numero-minimo)/(maximo-minimo)
    normalizados.append(numero_normalizado)

print(normalizados)

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

usuarios = [
    {"nome": "Alice", "email": "alice@example.com"},
    {"nome": "Bob", "email": ""},
    {"nome": "Carol", "email": "carol@example.com"}
]

usuarios_validos = [usuario for usuario in usuarios if usuario["email"]]

print(usuarios_validos)

### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

numeros = range(1,11)

lista_numeros = []
for numero in numeros:
    if numero%2 == 0:
        lista_numeros.append(numero)

print(lista_numeros)

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

vendas = [
    {"categoria": "eletrônicos", "valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletrônicos", "valor": 800}
]

vendas_por_categoria = {}
for venda in vendas:
    categoria = venda["categoria"]
    valor = venda["valor"]
    if categoria in vendas_por_categoria:
        vendas_por_categoria[categoria] +=valor
    else:
        vendas_por_categoria[categoria] = valor

print(vendas_por_categoria)