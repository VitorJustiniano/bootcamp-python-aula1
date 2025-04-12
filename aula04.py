from typing import Dict, Any

#Exercícios de Listas e Dicionários
#Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.

#lista = [1,2,3,4,5,6,7,8,9,10]
#for numero in lista:
    #if numero > 0 and numero < 11:
        #numero = numero ** 2
        #print(numero)

#for numero in lista:     versao simplificada
    #print(numero ** 2)

#Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".

#lista = ["Python", "Java", "C++", "JavaScript"]

#lista.remove("C++")
#lista.append("Ruby")
#print(lista)


#Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.

#livro = {"titulo": "1984", "autor": "George Orwell", "ano": 1949}
#for chave, valor in livro.items():
    #print(f"{chave}: {valor}")


#livro_01:Dict[str, Any] = {
    #"Titulo": "Game of Thrones",
    #"Autor": "Estagiario",
    #"Ano": 2005
#}
#livro_02:Dict[str, Any] = {
    #"Titulo": "Game of Thrones2",
    #"Autor": "Estagiario",
    #"Ano": 2007
#}

#lista_livros = []

#lista_livros.append(livro_01)
#lista_livros.append(livro_02)

#print(lista_livros)

#lista_livros_usando_dict:dict = {
    #"livro_01": {"Titulo": "Game of Thrones",
    #"Autor": "Estagiario",
    #"Ano": 2005},

    #"livro_02":{"Titulo": "Game of Thrones2",
    #"Autor": "Estagiario",
    #"Ano": 2007}
#}

#print(lista_livros_usando_dict["livro_01"]["Titulo"])

#Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.

#def contar_caracteres(s):
    #contagem = {}
    #for caractere in s:
        #contagem[caractere] = contagem.get(caractere, 0) + 1
    #return contagem
#print(contar_caracteres("engenharia de dados"))

#Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.

#lista = ["maçã", "banana", "cereja"]
#precos = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
#total = sum(precos[item] for item in lista)
#print(f"Preço total: {total}")


#6. Eliminação de Duplicatas
#Objetivo: Dada uma lista de emails, remover todos os duplicados.

#lista = ["vitor@hotmail.com","carlos@gmail.com","luis@gotmail.com","carlos@gmail.com"]
#email_unicos = list(set(lista))
#print(email_unicos)


#7. Filtragem de Dados
#Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
#idades = [22, 15, 30, 17, 18]
#idades_validas = []
#for idade in idades:
    #if idade >= 18:
        #idades_validas.append(idade)

#print(idades_validas)

#8. Ordenação Personalizada
#Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.
#pessoas = [
    #{"nome": "Alice", "idade": 30},
    #{"nome": "Bob", "idade": 25},
    #{"nome": "Carol", "idade": 20}
#]
#pessoas.sort(key=lambda pessoa: pessoa["nome"])

#print(pessoas)

#9. Agregação de Dados
#Objetivo: Dado um conjunto de números, calcular a média.

#numeros = [1,4,5,8,10]
#media = sum(numeros)/ len(numeros)
#print("media: ", media)

#10. Divisão de Dados em Grupos
#Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.
#lista = [1,2,4,7,8,9,10]
#lista_par = []
#lista_impar = []
#for numero in lista:
   #if numero % 2 == 0:
        #lista_par.append(numero)
    #else:
        #lista_impar.append(numero)
#print(lista_par)
#print(lista_impar)



#Exercícios com Dicionários
#11. Atualização de Dados
#Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.

#produtos = [
    #{"id": 1, "nome": "Teclado", "preço": 100},
    #{"id": 2, "nome": "Mouse", "preço": 80},
    #{"id": 3, "nome": "Monitor", "preço": 300}
#]
#for produto in produtos:
    #if produto["id"] == 2:
        #produto["preco"] = 90

#print(produtos)

#12. Fusão de Dicionários
#Objetivo: Dados dois dicionários, fundi-los em um único dicionário.

#chaves iguais faz desta forma

#dicionario1 = {
    #"nome": "vitor",
    #"sobrenome": "justiniano",
    #"idade": 21
#}

#dicionario2 = {
    #"nome": "pedro",
    #"sobrenome": "zan",
    #"idade": 20
#}
#dicionario3 = {}
#dicionario3 = [dicionario1,dicionario2]
#print(dicionario3)

#chaves diferentes faz desta forma
#dicionario1 = {"a": 1, "b": 2}
#dicionario2 = {"c": 3, "d": 4}

#dicionario_fundido = {**dicionario1, **dicionario2}

#print(dicionario_fundido)


#13. Filtragem de Dados em Dicionário
#Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.

#estoque = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}
#estoque_filtrado = {}
#for produto in estoque:
    #if estoque[produto] > 0:
        #estoque_filtrado[produto] = estoque[produto]
#print(estoque_filtrado)


#14. Extração de Chaves e Valores
#Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.

#dicionario = {"a": 1, "b": 2, "c": 3}
#chaves = list[dicionario.keys()]
#valores = list[dicionario.values()]
#print(chaves)
#print(valores)


#15. Contagem de Frequência de Itens
#Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.
texto = "engenharia de dados"
frequencia = {}

for caractere in texto:
    if caractere in frequencia:
        frequencia[caractere] += 1
    else:
        frequencia[caractere] = 1
print(frequencia)



#Exercícios de Funções
#16.Escreva uma função que receba uma lista de números e retorne a soma de todos os números.
#17.Crie uma função que receba um número como argumento e retorne True se o número for primo e False caso contrário.
#18.Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.
#19.Implemente uma função que receba dois argumentos: uma lista de números e um número. A função deve retornar todas as combinações de pares na lista que somem ao número dado.
#20.Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas


