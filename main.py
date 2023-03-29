idade = input("digite um número:\n ")

if idade.isnumeric():
    idade = int(idade)
    if idade < 0:
        print("impossível!")
    elif idade < 18:
        print("não precisa se alistar.")
    elif 18 < idade < 65:
        print("Não esqueça de votar na próxima eleição.")
    elif idade > 65:
        print("Vá descançar.")
else:
    print  ("eita!")
