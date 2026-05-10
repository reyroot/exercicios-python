valor_compra = float(input("Digite o valor da compra: "))
cliente_vip = input("Cliente VIP? (s/n): ")

desconto = 0

if valor_compra > 100:
    desconto = 10

if valor_compra > 200:
    desconto = 20

if cliente_vip == "s":
    desconto = desconto + 5

valor_final = valor_compra - desconto

print("Desconto aplicado:", desconto)
print("Valor final:", valor_final)