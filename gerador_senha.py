import random

array_caracteres = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","ç","z","x","c","v","b","n","m","1","2","3","4","5","6","7","8","9","0","!","@","#","$","%","&","*"]
senha_gerada = []

def gerador_de_senha(array_caracteres, senha_gerada):
    while len(senha_gerada) < 20:
        caracter_aleatorio = random.choice(array_caracteres)
        senha_gerada.append(caracter_aleatorio)
    return ("".join(senha_gerada))


print(gerador_de_senha(array_caracteres, senha_gerada))


