salario = 1200

c1 = 200
c2 = 120

c1Atraso = 200 * 0.02
c2Atraso = 120 * 0.02

valorAtraso = c1 + c2 + c1Atraso + c2Atraso
contas = salario - valorAtraso
print(f"O seu salário depois dos descontos é: {contas:.2f}")
