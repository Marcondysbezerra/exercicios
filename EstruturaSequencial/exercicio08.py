# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

dinheiro_por_hora = float(input("Quanto você ganha por hora? "))
horas_trabalhadas_mes = float(input("Quantas horas você trabalha por dia? "))

salario = dinheiro_por_hora * horas_trabalhadas_mes

print(f"Salário mês: {salario}")