import random

maiusculo = ["A","B","C","D","E","F","G", "H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
minusculo = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numeros = [1,2,3,4,5,6,7,8,9,0]
caracter = ["!","@","#","$",".",",",";","?","*","&","_"]
maiuscMinusc = ["A","B","C","D","E","F","G", "H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
                "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
alfanumerico = ["A","B","C","D","E","F","G", "H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
                "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
                1,2,3,4,5,6,7,8,9,0]
alfacaracter = ["A","B","C","D","E","F","G", "H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
                "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
                1,2,3,4,5,6,7,8,9,0,
                "!","@","#","$",".",",",";","?","*","&","_"]

senha = []


def maiusculo(qtd_caracteres):
    """Gera senha apenas com caracteres maiúsculos"""
    for i in range(0, qtd_caracteres):
        senha.append(random.choice(maiusculo))
    return senha


def minusculo(qtd_caracteres):
    """Gera senha apenas com caracteres minúsculos"""
    for i in range(0, qtd_caracteres):
        senha.append(random.choice(minusculo))
    return senha


def numerico(qtd_caracteres):
    """Gera senha apenas com caracteres numéricos"""
    for i in range(0, qtd_caracteres):
        senha.append(random.choice(numeros))
    return senha


def maiuscMinusc(qtd_caracteres):
    """Gera senha apenas com caracteres maiúsculos e minúsculos"""
    for i in range(0, qtd_caracteres):
        senha.append(random.choice(maiuscMinusc))
    return senha


def alfanumerico(qtd_caracteres):
    """Gera senha com caracteres maiúsculos, minúsculos e numéricos"""
    for i in range(0, qtd_caracteres):
        senha.append(random.choice(alfanumerico))
    return senha


def alfacaracter(qtd_caracteres):
    """Gera senha com caracteres maiúsculos, minúsculos, numéricos e caractéres especiais"""
    for i in range(0, qtd_caracteres):
        senha.append(random.choice(alfacaracter))
    return senha
