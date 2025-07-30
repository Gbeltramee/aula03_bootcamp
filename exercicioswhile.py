### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

# while input("forneça a palavra chave")!= "sair":
#     input("Palavra errada")

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.
# numero = int(input("Digite um numero entre 1 e 40"))

# while numero < 1 or numero > 40:
#     print("Numero fora do intervalo")
#     numero = int(input("Digite um numero entre 1 e 40"))


### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.
# pagina_atual = 1
# paginas_totais = 5

# while pagina_atual <= paginas_totais:
#     print(f"pagina {pagina_atual} de {paginas_totais}")
#     pagina_atual += 1

# print("Todas paginas foram processadas")


### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

# tentativas_maximas = 5
# tentativa = 1

# while tentativa <= tentativas_maximas:
#     print(f"Tentativa {tentativa} de {tentativas_maximas}")
#     # Simulação de uma tentativa de conexão
#     # Aqui iria o código para tentar conectar
#     if True:  # Suponha que a conexão foi bem-sucedida
#         print("Conexão bem-sucedida!")
#         break
#     tentativa += 1
# else:
#     print("Falha ao conectar após várias tentativas.")

### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.

# itens = [1, 2, 3, "parar", 4, 5]

# i = 0
# while i < len(itens):
#     if itens[i] == "parar":
#         print("parada encontrada, fim do fluxo")
#         break
#     print(f"processando item {itens[i]}")
#     i +=1