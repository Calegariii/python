moeda1 = int(input("Quantidade de moedas de 1 centavo: "))
moeda5 = int(input("Quantidade de moedas de 5 centavo: "))
moeda10 = int(input("Quantidade de moedas de 10 centavo: "))
moeda25 = int(input("Quantidade de moedas de 25 centavo: "))
moeda50 = int(input("Quantidade de moedas de 50 centavo: "))
moedaReal = int(input("Quantidade de moedas de 1 real: "))

v1 = 0.01 * moeda1
v2 = 0.05 * moeda5
v3 = 0.10 * moeda10
v4 = 0.25 * moeda25
v5 = 0.50 * moeda50
v6 = 1 * moedaReal

totalReal = v1 + v2 + v3 + v4 + v5 + v6

print(f"Total poupado em reais: R${totalReal:.2f}")
