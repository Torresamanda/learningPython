# pessoas = {'nome': 'Amanda', 'idade': 22, 'sexo': 'F'}

#remover
# del pessoas['sexo']

#modificar
# pessoas['nome'] = 'Patricia'

#adicionar
# pessoas['peso'] = 56.5

# print(f'A {pessoas["nome"]} tem {pessoas["idade"]} anos')

# print(pessoas.keys())

# print(pessoas.values())

# print(pessoas.items())

# for k in pessoas.keys():
#     print(k)

# for k in pessoas.values():
#     print(k)

# for k, v in pessoas.items():
#     print(f'{k} = {v}')

# brasil = []
# estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

# brasil.append(estado1)
# brasil.append(estado2)

# print(brasil[0]['uf'])

estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())

for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()

