import random

numeropote1 = random.sample(range(1, 8), 7)
numeropote2 = random.sample(range(0, 8), 8)
numeropote3 = random.sample(range(0, 8), 8)
numeropote4 = random.sample(range(0, 8), 8)

pote1 = {'Brasil': 'CMB', 'Catar': 'AFC', 'Bélgica': 'UEFA', 'França': 'UEFA', 'Argentina': 'CMB', 'Inglaterra': 'UEFA',
         'Espanha': 'UEFA', 'Portugal': 'UEFA'}
# print(pote1)
lista1 = ['Catar', 'Brasil', 'Bélgica', 'França', 'Argentina', 'Inglaterra', 'Espanha', 'Portugal']
# print(lista1)

# print(numeropote1)
lista2 = ['Holanda', 'Alemanha', 'Dinamarca', 'México', 'Estados Unidos', 'Suíça', 'Uruguai', 'Croácia']
pote2 = {'Holanda': 'UEFA', 'Alemanha': 'UEFA', 'Dinamarca': 'UEFA', 'México': 'CONCACAF',
         'Estados Unidos': 'CONCACAF', 'Suíça': 'UEFA', 'Uruguai': 'CMB', 'Croácia': 'UEFA'}
lista3 = ['Senegal', 'Irã', 'Japão', 'Sérvia', 'Polônia', 'Coreia do Sul', 'Marrocos', 'Tunísia']
pote3 = {'Senegal': 'CAF', 'Irã': 'AFC', 'Japão': 'AFC', 'Sérvia': 'UEFA', 'Polônia': 'UEFA',
         'Coreia do Sul': 'AFC', 'Marrocos': 'CAF', 'Tunísia': 'CAF'}

lista4 = ['Canadá', 'Equador', 'Arábia Saudita', 'Gana', 'Camarões', 'Europeu', 'AsiaCMB', 'OFCConcacaf']
pote4 = {}
# print(numeropote2)
grupoA = [[(lista1[0])], [lista2[(numeropote2[0])]],[lista3[numeropote3[0]]],[lista4[numeropote4[0]]]]
print(grupoA)
grupoB = [[lista1[(numeropote1[0])]], [lista2[(numeropote2[1])]],[lista3[numeropote3[1]]],[lista4[numeropote4[1]]]]
print(grupoB)
grupoC = [[lista1[(numeropote1[1])]], [lista2[(numeropote2[2])]],[lista3[numeropote3[2]]],[lista4[numeropote4[2]]]]
print(grupoC)
grupoD = [[lista1[(numeropote1[2])]], [lista2[(numeropote2[3])]],[lista3[numeropote3[3]]],[lista4[numeropote4[3]]]]
print(grupoD)
grupoE = [[lista1[(numeropote1[3])]], [lista2[(numeropote2[4])]],[lista3[numeropote3[4]]],[lista4[numeropote4[4]]]]
print(grupoE)
grupoF = [[lista1[(numeropote1[4])]], [lista2[(numeropote2[5])]],[lista3[numeropote3[5]]],[lista4[numeropote4[5]]]]
print(grupoF)
grupoG = [[lista1[(numeropote1[5])]], [lista2[(numeropote2[6])]],[lista3[numeropote3[6]]],[lista4[numeropote4[6]]]]
print(grupoG)
grupoH = [[lista1[(numeropote1[6])]], [lista2[(numeropote2[7])]],[lista3[numeropote3[7]]],[lista4[numeropote4[7]]]]
print(grupoH)
