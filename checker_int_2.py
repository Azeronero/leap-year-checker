# Update : J'ai ajouté un input pour récupere l'année de l'utilisateur, 
# et j'ai crée une fonction qui vérifie si le nombre est entier (divisible) ou float (non divisible)
# remarque elle ne vérifie que si il y a un point dans le nombre et si oui x sera faux
# et l'utilisateur peux ajouter des lettres et des caractères spéciaux

# Ce programme à pour but de vérifier si une variable (qui sera la valeur entré par l'utilisateur via un input) est divisible ou non
# Un nombre divisé par x est dit divisible si son quotient est un nombre entier
# Exemple : 10/2 = 5 divisible /// 10/4 = 2.5 non divisible

# Rappel des conditions pour qu'une année soit bisextile: 
# 1. Divisible par 4, mais pas par 100 → c'est une année bissextile.
# 2. Divisible par 400 → c'est une année bissextile (même si elle est divisible par 100).
# Conlusion : au moins une des 2 conditions doit etre VRAI pour que l'année soit bisextile

numbertest = input("Veuillez entrer une année : ") # ici on récupère l'année que l'utilisateur entre, et on l'a convertit en int car la valeur des input de base sont en STR

print(type(numbertest)) # on vérifie si le type est bien un entier

# condition_1 = True # on crée la variable condition 1 qui se doit d'être un nombre entier

def checker_int(numbertest):
    x = None
    caractere = "."
    if caractere in numbertest:
        x = False
    else:
        x = True
    print(numbertest)
    return x




condition_final = checker_int(numbertest)

print(f"La condition est : {condition_final}")
