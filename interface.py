import time
bonjour = "Bonjour ! Vous trouverez juste en dessous toutes mes fonctionnalitées :"
for i in range(len(bonjour)):
    print(bonjour[i], end='')
    time.sleep(0.11)
print(' ')
print("1 - Afficher tous les mots dont le score TF-IDF est égal à 0.")
print("2 - Afficher les mots ayant le score TF Idf le plus élevé.")
print("3 - Afficher les mots les plus répétés par le président Chirac")
print("4 - Aficher les noms des présidents ayant le plus parler de \"Nation\" ainsi que celui l'ayant le plus dit.")
print("5 - Afficher le premier président à parler d'écologie/climat.")
print("6 - Afficher les mots ayant été dit par tous les présidents.")
print("Vous n'avez qu'à utiliser les chiffres pour choisir ce que vous voulez :", end=' ')
selec = input()


#Selction 1
if selec == '1':
    for i in range(len(M)):
        for j in range(len(M[i])):
            print(M[i][j], end=',')
        print()
elif selec == '6':
    main.py.fonction_6()
