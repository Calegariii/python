anoNascimento = int(input("Digite o ano de nascimento: "))
anoAtual = int(input("Digite o ano atual: "))

idadeAnos = anoAtual - anoNascimento
idadeMeses = idadeAnos * 12
idadeDias = idadeAnos * 365
idadeSemanas = idadeAnos * 52

print("-" * 25)

print(f"Sua idade em anos: {idadeAnos}")
print(f"Sua idade em meses: {idadeMeses}")
print(f"Sua idade em dias: {idadeDias}")
print(f"Sua idade em semanas: {idadeSemanas}")

print("-" * 25)







