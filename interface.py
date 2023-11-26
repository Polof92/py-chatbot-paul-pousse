import main

print("Bonjour ! Vous trouverez juste en dessous toutes mes fonctionnalitées :")
def affichage():
    for i in range(6):
        print('')
#permet d'enlever le 'Patientez...' Dès que la fonction s'affiche

print('')

def menu_principal():
    print("1 - Afficher tous les mots dont le score TF-IDF est égal à 0.")
    print("2 - Afficher les mots ayant le score TF Idf le plus élevé.")
    print("3 - Afficher les mots les plus répétés par le président Chirac")
    print("4 - Aficher les noms des présidents ayant le plus parler de \"Nation\" ainsi que celui l'ayant le plus dit.")
    print("5 - Afficher le premier président à parler d'écologie/climat.")
    print("6 - Afficher les mots ayant été dit par tous les présidents.")
    print("Vous n'avez qu'à utiliser les chiffres pour choisir ce que vous voulez :", end=' ')
    selec = input()
    return selec
#affiche les fonctionnalités et permet de renvoyer la séléction

def utilisation():
    selec = menu_principal()
    choix(selec)
    retour()

def choix(selec):
    for i in range(7):
        print('')
    print('Patientez...')
    if selec == '1':
        affichage()
        print('Les mots les moins importants sont les suivants :')
        print(main.mot_pas_important(), end=', ')
    elif selec == '2':
        affichage()
        print('Les mots les plus importants sont :')
        print(main.mot_plus_important(), end=', ')
    elif selec == '3':
        affichage()
        print('Les mots les plus répétés par le président Chirac sont :')
        print(main.chirac())
    elif selec == '4':
        affichage()
        print("Voici les noms des présidents qui ont dit \'Nation\' et celui qui l'a répété le plus de fois :")
        print(main.nation())
    elif selec=='5':
        affichage()
        print("Voici le premier président a parler d'écologie:")
        print(main.ecolo_2())    
    elif selec == '6':
        affichage()
        print("Les mots ayant été dit par tous les présidents sont :")
        main.fonction_6()
#affiche les choix et renvoie la séléction
def retour():
    print(' ')
    a = input('Si vous voulez accéder au menu principal vous n\'avez qu\'à écrire : \'Retour\' : ')
    if a == 'Retour':
        utilisation()
#est a fonction qui revient en arrière

utilisation()
