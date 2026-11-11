config = {"tema": "escuro","fonte": 12}
config.update({"fonte": 14,"idioma": "pt-Brasil"})
removido = config.pop("tema")
print(len(config))

valores = [2,4,6]
dobros = []

for v in valores:
    dobros.append(v*2)

dobros.insert(1, 5)
print(dobros[2])

estoque = {"maçã": 10, "banana": 5, "laranja": 8}
produtos_em_alta = 0
for frutas, qtd in estoque.items():
    if qtd>5:
        produtos_em_alta = produtos_em_alta + 1
print(produtos_em_alta)

boletim = {}
for n in range(3):
    nome = str(input('Nome do aluno: '))
    nota = float(input("Nota do aluno: "))
    boletim.update({nome: nota})
for nome, nota in boletim.items():
    print(nome,'tirou', nota)

