from random import choice
import imprime_senha

maiusculo = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

minusculo = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

caracter = ["!", "@", "#", "$", ".", ",", ";", "?", "*", "&", "_"]

maiuscMinusc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
                "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

alfanumerico = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
                "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

alfacaracter = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
                "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                1, 2, 3, 4, 5, 6, 7, 8, 9, 0,
                "!", "@", "#", "$", ".", ",", ";", "?", "*", "&", "_"]


def maiusc(qtd_caracteres):
    """Gera senha apenas com caracteres maiúsculos"""
    senha = []
    for i in range(0, qtd_caracteres):
        senha.append(choice(maiusculo))
    imprime_senha.imprime(senha)


def minusc(qtd_caracteres):
    """Gera senha apenas com caracteres minúsculos"""
    senha = []
    for i in range(0, qtd_caracteres):
        senha.append(choice(minusculo))
    imprime_senha.imprime(senha)


def num(qtd_caracteres):
    """Gera senha apenas com caracteres numéricos"""
    senha = []
    for i in range(0, qtd_caracteres):
        senha.append(choice(numeros))
    imprime_senha.imprime(senha)


def maiMin(qtd_caracteres):
    """Gera senha apenas com caracteres maiúsculos e minúsculos"""
    senha = []
    for i in range(0, qtd_caracteres):
        senha.append(choice(maiuscMinusc))
    imprime_senha.imprime(senha)


def alfanum(qtd_caracteres):
    """Gera senha com caracteres maiúsculos, minúsculos e numéricos"""
    senha = []
    for i in range(0, qtd_caracteres):
        senha.append(choice(alfanumerico))
    imprime_senha.imprime(senha)


def alfacar(qtd_caracteres):
    """Gera senha com caracteres maiúsculos, minúsculos, numéricos e caractéres especiais"""
    senha = []
    for i in range(0, qtd_caracteres):
        senha.append(choice(alfacaracter))
    imprime_senha.imprime(senha)
