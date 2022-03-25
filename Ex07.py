#NicksOMaisBrabo
valor = input ("Digite um número inteiro entre 0 a 99: ")
inteiro = int(valor)

if inteiro > 99:
    print ("Número inválido: ")
else: 
    dezena = inteiro // 10
    unidade = inteiro % 10

    print ("Dezenas: ", dezena)
    print ("Unidades: ", unidade)
#NicksOMaisBrabo