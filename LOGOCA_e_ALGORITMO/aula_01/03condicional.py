# Condicional simples 1 ou 2 no máximo.
idade = 16 

if idade >= 18:
    print("pode obter a CNH")
else :
    print("não pode obter a CNH")

    # Condicional aninhada / composta.
    media = 8.5 

    if media == 10:
        print("nota máxima! Parabéns")
    elif  media >= 9:
        print("ótimo")
    elif media >= 8:
        print("Bom!")
    elif media >= 7:
        print("Na media")
    elif media >= 5:
        print("A baixo da media") 

        # operadores lógicos

        valor = 84

        if valor >= 0 and valor <= 100:
            print("o valor está entre 0 e 100")
        else:
            print("o valor não está entre 0 e 100")

            total = 400
            formaPagamento = " a prazo"

        if total >= 100 and formaPagamento == "a vista":
            print("valor a pagar Rs"+str(total * 0.9))

        else:
            print("o total a pagar Rs"+str(total))
            
               