q = []
p = []
total = 0
vendas = int(input("Digite a quantidade de vendas: "))

for n in range (vendas):
    quant = int(input("Digite a quantidade de produto: "))
    q.append(quant)
    preco = float(input("Digite o preço do produto : "))
    p.append(preco)
    total += quant * preco

print(f'lista das quantidades: {q}')
print(f'lista dos preços: {p}')

print(f'faturamento mensal: {total}')

