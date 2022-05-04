import random

grupoA = []
grupoB = []
grupoC = []

pote1 = {'Flamengo': 'RJ',
         'Vasco': 'RJ',
         'Botafogo': 'RJ',
         'Santos': 'SP',
         'Palmeiras': 'SP',
         'Corinthians': 'SP',
         'Cruzeiro': 'MG',
         'Atletico': 'MG',
         'America': 'MG'}

lista1 = ['Flamengo', 'Vasco', 'Botafogo', 'Santos', 'Palmeiras', 'Corinthians', 'Cruzeiro', 'Atletico', 'America']

numeropote2 = random.sample(range(0, 9), 9)
print(numeropote2)

grupoA = [lista1[(numeropote2[0])]]
grupoB = [lista1[(numeropote2[1])]]
grupoC = [lista1[(numeropote2[2])]]

if pote1[lista1[(numeropote2[0])]] != pote1[lista1[(numeropote2[3])]]:
    grupoA.append(lista1[(numeropote2[3])])
elif pote1[lista1[(numeropote2[1])]] != pote1[lista1[(numeropote2[3])]]:
    grupoB.append(lista1[(numeropote2[3])])
else:
    grupoC.append(lista1[(numeropote2[3])])

if len(grupoA) < 2 and pote1[lista1[(numeropote2[0])]] != pote1[lista1[(numeropote2[4])]]:
    grupoA.append(lista1[(numeropote2[4])])
elif pote1[lista1[(numeropote2[1])]] != pote1[lista1[(numeropote2[4])]] and len(grupoB) < 2:
    grupoB.append(lista1[(numeropote2[4])])
elif pote1[lista1[(numeropote2[2])]] != pote1[lista1[(numeropote2[4])]] and len(grupoC) < 2:
    grupoC.append(lista1[(numeropote2[4])])
else:
    grupoA.append(lista1[(numeropote2[4])])

if len(grupoA) < 2 and pote1[lista1[(numeropote2[0])]] != pote1[lista1[(numeropote2[5])]]:
    grupoA.append(lista1[(numeropote2[5])])
elif pote1[lista1[(numeropote2[1])]] != pote1[lista1[(numeropote2[5])]] and len(grupoB) < 2:
    grupoB.append(lista1[(numeropote2[5])])
elif pote1[lista1[(numeropote2[2])]] != pote1[lista1[(numeropote2[5])]] and len(grupoC) < 2:
    grupoC.append(lista1[(numeropote2[5])])
elif pote1[lista1[(numeropote2[0])]] != pote1[lista1[(numeropote2[5])]]:
    grupoA.append(lista1[(numeropote2[5])])
else:
    grupoB.append(lista1[(numeropote2[5])])

if pote1[grupoA[0]] != pote1[lista1[(numeropote2[6])]] and pote1[grupoA[1]] != pote1[lista1[(numeropote2[6])]] and len(
        grupoA) < 2:
    grupoA.append(lista1[(numeropote2[6])])
elif pote1[grupoB[0]] != pote1[lista1[(numeropote2[6])]] and pote1[grupoB[1]] != pote1[
    lista1[(numeropote2[6])]] and len(grupoB) < 2:
    grupoB.append(lista1[(numeropote2[6])])
elif pote1[lista1[(numeropote2[2])]] != pote1[lista1[(numeropote2[6])]] and len(grupoC) < 2:
    grupoC.append(lista1[(numeropote2[6])])
elif pote1[lista1[(numeropote2[0])]] != pote1[lista1[(numeropote2[6])]] and pote1[grupoA[1]] != pote1[
    lista1[(numeropote2[6])]]:
    grupoA.append(lista1[(numeropote2[6])])
else:
    grupoB.append(lista1[(numeropote2[6])])

print(grupoA)
print(grupoB)
print(grupoC)
