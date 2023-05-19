import gera_senha, continua, imprime_senha

op = 1

while op != 0:
    print("*"*24)
    print("*** GERADOR DE SENHA ***")
    print("*"*24)

    print("\nQuantos caracteres quer na sua senha? ")
    qtd_caracteres = int(input("=> "))

    print("\nEscolha uma formato de senha:"
          "\n1) - AAA\n"
          "2) - aaa\n"
          "3) - 111\n"
          "4) - AaAa\n"
          "5) - Aa1\n"
          "6) - Aa1@")
    formato = int(input("=> "))

    senha = []

    if formato == 1:
        senha = gera_senha.maiusculo(qtd_caracteres)
        imprime_senha.imprime(senha)
        op = continua.continua()

    elif formato == 2:
        senha = gera_senha.minusculo(qtd_caracteres)
        imprime_senha.imprime(senha)
        op = continua.continua()

    elif formato == 3:
        senha = gera_senha.numerico(qtd_caracteres)
        imprime_senha.imprime(senha)
        op = continua.continua()

    elif formato == 4:
        senha = gera_senha.maiuscMinusc(qtd_caracteres)
        imprime_senha.imprime(senha)
        op = continua.continua()

    elif formato == 5:
        senha = gera_senha.alfanumerico(qtd_caracteres)
        imprime_senha.imprime(senha)
        op = continua.continua()


    elif formato == 6:
        senha = gera_senha.alfacaracter(qtd_caracteres)
        imprime_senha.imprime(senha)
        op = continua.continua()


print("Volte sempre!")