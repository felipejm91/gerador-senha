import gera_senha
import continua

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

    if formato == 1:
        gera_senha.maiusc(qtd_caracteres)
        op = continua.continua()
    elif formato == 2:
        gera_senha.minusc(qtd_caracteres)
        op = continua.continua()
    elif formato == 3:
        gera_senha.num(qtd_caracteres)
        op = continua.continua()
    elif formato == 4:
        gera_senha.maiMin(qtd_caracteres)
        op = continua.continua()
    elif formato == 5:
        gera_senha.alfanum(qtd_caracteres)
        op = continua.continua()
    elif formato == 6:
        gera_senha.alfacar(qtd_caracteres)
        op = continua.continua()

print("Volte sempre!")