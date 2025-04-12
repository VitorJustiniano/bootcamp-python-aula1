from typing import Dict, List
#colocar typehint, colocar funcao e colocar dicionarios

#colocar input e oq ele pedir para por dentro de uma funcao de cadastro e colocar a tipagem dela
#um algo mais colocar ela dentro de um while para cada vez que rodar esse programa ele adicionar uma lista dentro de um dicionario

#usuarios   /   bonus     cada vez que rodar vai salvar o bonus dentro de um lugar


CONSTANT_BONUS = 1000
usuarios: List[Dict[str,float]] = []

def cadastrar_usuario() -> Dict[str,float]:
    nome_valido = False
    salario_valido = False
    bonus_valido = False

    while nome_valido is not True:
        try:
            # Verifica se o nome está vazio
            nome = input("Digite seu nome ")
            if len(nome) == 0:
                raise ValueError("O nome não pode estar vazio.")
            # Verifica se há números no nome
            elif nome.isdigit():
                raise ValueError("O nome não deve conter números.")
            elif nome.isspace():
                print("voce digitou so o espaco")
            else:
                nome_valido = True
                print("Nome válido:", nome)
        except ValueError as e:
            print(e)

    while salario_valido is not True:
        try:    
            salario = float(input("Digite seu salario: "))
            if salario < 0:
                print("Por favor, digite um valor positivo para o salário.")
            else:    
                salario_valido = True
        except ValueError:
            print("Entrada inválida para o salário. Por favor, digite um número.")
    while bonus_valido is not True:
        try:   
            bonus = float(input("Digite seu bonus: "))
            if bonus < 0:
                print("Por favor, digite um valor positivo para o bônus.")
            else:    
                bonus_valido = True
        except ValueError:
            print("Entrada inválida para o bônus. Por favor, digite um número.")

    valor_kpi = CONSTANT_BONUS + salario * bonus

    print(f"Seu KPI é: {valor_kpi:.2f}")
    print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus:.2f}.")

    return {
        "nome": nome,
        "salario": salario,
        "bonus": bonus,
        "kpi": valor_kpi
    }

while True:
    usuario = cadastrar_usuario()
    usuarios.append(usuario)

    continuar = input("Deseja cadastrar outro usuário? (s/n): ").strip().lower()
    if continuar != 's':
        break

# Mostrar todos os cadastros
print("\n Lista de usuários cadastrados:")
for indice, item in enumerate(usuarios, start=1):
    print(f"{indice}. Nome: {item['nome']} | Salário: R${item['salario']:.2f} | Bônus: {item['bonus']:.2f} | KPI: R${item['kpi']:.2f}")
