CONSTANT_BONUS = 1000

nome = input("Digite seu nome ")

salario = float(input("Digite seu salario: "))

bonus = float(input("Digite seu bonus: "))

valor_kpi = CONSTANT_BONUS + salario * bonus

print(f"Parabens {nome} voce possui um bonus de {valor_kpi}")

