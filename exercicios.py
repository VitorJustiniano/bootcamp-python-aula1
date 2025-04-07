import math
# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
#n1 = int(input("Digite um numero"))
#n2 = int(input("Digite um numero"))
#soma = n1 + n2
#print(soma)

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
#n = int(input("digite o numero"))
#resto_div = n % 5
#print(resto_div)

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
#n1 = int(input("digite um numero"))
#n2 = int(input("digite um numero"))
#mult = n1 * n2
#print(mult)

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
#numero1 = int(input("Digite o numero1: "))
#numero2 = int(input("Digite o numero2: "))
#divisao = numero1 // numero2

#print(divisao)

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
#n1 = int(input("digite um numero"))
#quadrado = n1 ** 2
#print(quadrado)

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
#n1 = float(input("digite um numero"))
#n2 = float(input("digite um numero"))
#soma = n1 + n2
#print(soma)
# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
#n1 = float(input("digite um numero"))
#n2 = float(input("digite um numero"))
#media = n1 + n2 / 2
#print(media)
# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
#base = float(input("digite um numero"))
#expoente = float(input("digite um numero"))
#potencia = base ** expoente
#print(potencia)
# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
#temp_celcius = float(input("digite um numero"))
#conversao = (temp_celcius * 9/5) + 32
#print(f"{temp_celcius}C é igual a {conversao}F")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
#raio_circulo = float(input("Digite o raio: "))
#area_circulo = math.pi * raio_circulo ** 2
#print(f"{area_circulo:.2f}")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
#conversao = input("digite:")
#texto_maiusculo = conversao.upper()
#print(texto_maiusculo)
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
#texto = input("digite seu nome: ")
#texto_minusculo = texto.lower()
#print(texto_minusculo)
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
#texto = input("digite a frase: ")
#texto_strip = texto.strip()
#print(texto_strip)
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
#data_usuario = input("insira uma data no formato dd/mm/aaaa: ")
#lista_dia_mes_ano = data_usuario.split("/")
#print(f"o elemento 1 é : {lista_dia_mes_ano[0]}")
#print(f"o elemento 2 é : {lista_dia_mes_ano[1]}")
#print(f"o elemento 3 é : {lista_dia_mes_ano[2]}")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
#texto1 = input("digite: ")
#texto2 = input("digite: ")
#texto_concatenado = texto1 + texto2
#print(texto_concatenado)

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
valor1 = True
valor2 = False
resultado = valor1 and valor2
print("Resultado do AND lógico:", resultado)
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
valor1 = True
valor2 = False
resultado = valor1 or valor2
print("Resultado do OR lógico:", resultado)
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
valor = bool(input("Digite um valor bool: "))
resultado = not valor
print("Resultado do NOT lógico:", resultado)

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
v1 = 5
v2 = 5
resultado = (v1 == v2)
print("Resultado da igualdade:", resultado)

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
v1 = 5
v2 = 3
resultado = (v1 != v2)
print("Resultado da igualdade:", resultado)
# #### try-except e if

# 21: Conversor de Temperatura
try:
    celsius = float(input("Digite a temperatura em celsius: "))
    farenheit = (celsius * 9/5) + 32
    print(f"{celsius}é igual a {farenheit}F")
except ValueError:
    print("Por favor, digite um número válido para a temperatura.")

# 22: Verificador de Palíndromo
entrada = input("digite uma palavra: ")
if isinstance(entrada, str):
    formatado = entrada.replace(" ", "").lower()
    if formatado == formatado[::-1]:
        print("É um palíndromo.")
    else:
        print("Não é um palíndromo.")
else:
    print("Entrada inválida. Por favor, digite uma palavra ou frase.")
# 23: Calculadora Simples
try:
    valor1 = float(input("digite o numero: "))
    valor2 = float(input("digite o numero: "))
    operador = input("Digite o operador (+, -, *, /): ")
    if operador == "+":
        resultado = valor1 + valor2
    elif operador == "-":
        resultado = valor1 - valor2
    elif operador == "*":
        resultado = valor1 * valor2
    elif operador == "/":
        resultado = valor1 / valor2
    else:
        print("Operador invalido ou divisao por zero")
    print("resultado", resultado)
except ValueError:
    print("Erro: Entrada inválida. Certifique-se de inserir números.")
    
# 24: Classificador de Números
try: 
    numero = int(input("Digite um numero: "))
    
    if numero > 0:
        print("positivo")
    elif numero < 0:
        print("negativo")
    else :
        print("zero")
    if numero % 2 == 0:
        print("par")
    else:
        print("impar")
except ValueError:
    print("Por favor, digite um número inteiro válido.")

# 25: Conversão de Tipo com Validação
entrada_lista = input("digite uma lista de numeros separados por virgula: ")
numero_str = entrada_lista.split(",")
numero_int = []
try:
    for num in numero_str:
        numero_int.append(int(num.strip()))
    print("lista de inteiros: ", numero_int)
except ValueError:
    print("Erro: certifique-se de que todos os elementos são números inteiros válidos.")