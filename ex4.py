nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
faltas = int(input("Digite o número de faltas: "))

media = nota1 + nota2 / 2

if media >= 7:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

if faltas > 20:
    situacao = "Aprovado por falta"

print("Média:", media)
print("Situação:", situacao)