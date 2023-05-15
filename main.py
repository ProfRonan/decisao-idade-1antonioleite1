print ('digite um numero')
idade = int(input('> '))

impossível = False
menor = False
maior = False
velho = False
print (idade)
if idade < 0:
    print('Impossível!')
    impossível = True
elif idade < 18: 
    print('Não precisa se alistar.')
    menor = True
elif 18 < idade < 65: # 18 < idade and idade < 65
    print('Não esqueça de votar na próxima eleição.')
    maior =True
elif idade > 65:
    print ('Vá descansar.')
    velho = True
elif not (impossível or menor or maior or velho) :
    print("Eita!")
