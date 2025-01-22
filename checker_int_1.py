# Ce programme à pour but de vérifier si une variable (qui sera la valeur entré par l'utilisateur via un input) est divisible ou non
# Un nombre divisé par x est dit divisible si son quotient est un nombre entier
# Exemple : 10/2 = 5 divisible /// 10/4 = 2.5 non divisible

# Rappel des conditions pour qu'une année soit bisextile: 
# 1. Divisible par 4, mais pas par 100 → c'est une année bissextile.
# 2. Divisible par 400 → c'est une année bissextile (même si elle est divisible par 100).
# Conlusion : au moins une des 2 conditions doit etre VRAI pour que l'année soit bisextile

numbertest = 1

condition_1 = None

print(type(condition_1))

if type(numbertest) == int:
    condition_1 = True
else:
    condition_1 = False

print(condition_1)
