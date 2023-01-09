modo = ''
resultado = ''

modo = input("Digite 1 para Criptografar \n ou 2 para Descriptogragar\n")


if (modo == '1'):
    texto = input("Insira o texto para encriptar: \n")

    for i in range (0, len(texto)):
        resultado = resultado + chr(ord(texto[i])+2)
        print(resultado)
        resultado = ''

if (modo == '2'):
    texto = input("Insira o texto para dencriptar: \n")

    for i in range (0, len(texto)):
        resultado = resultado + chr(ord(texto[i])-2)
        print(resultado)
        resultado = ''