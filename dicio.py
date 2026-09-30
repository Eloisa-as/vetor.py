idades = {'Analice': "16" , "Larissa" : "15" , "André" : "17"}
print (idades)
print (idades['Larissa'])

cidades = {'Lara' : "Lavras" ,'Elisa' : "Luis Gomes" , "Evilly" : "Cachoeira dos Indios" , "Eloisa" : "Cajazeiras"}
print(cidades)
print(cidades['Lara'])

cidadesnome= {'Lara' : "Lavras" ,'Elisa' : "Luis Gomes" , "Evilly" : "Cachoeira dos Indios" , "Eloisa" : "Cajazeiras"}
print(cidadesnome)
print('A cidade de Lara é:')
print(cidadesnome ['Lara'])

cidadesnomeidade= {'Lara' : ['16' , 'Lavras'] ,'Elisa' : ["Luis Gomes" , "15"], "Evilly" : ["Cachoeira dos Indios" , '16'] , "Eloisa" : ["Cajazeiras" , '15']}
print(cidadesnomeidade)
print('A cidade de Lara é:')
print(cidadesnomeidade['Lara'][1])
print('A idade de Lara é:')
print(cidadesnomeidade['Lara'][0])
