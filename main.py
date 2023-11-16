import os
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names
# donne le nom des fichiers qui sont dans speeches

directory = "./speeches"
files_names = list_of_files(directory, "txt")
print(files_names)
#appel de la fonction 

def nom_president():
    a=files_names
    for i in range(len(a)):
        a[i]=a[i][11:len(a[i])-4]
        if a[i][len(a[i])-1]=='1' or a[i][len(a[i])-1]=='2':
            a[i]=a[i][:len(a[i])-1]
    return a
tab=nom_president()
print(tab)
#créer une liste avec le nom des présidents 


def prenom(a):
    for i in range(len(a)):
        if a[i]=="Chirac":
            a[i]="Jacques"
        if a[i]=="Giscard dEstaing":
            a[i]="Valérie"
        if a[i]=="Hollande":
            a[i]="FrançoisH"
        if a[i]=="Macron":
            a[i]="Emmanuel"
        if a[i]=="Mitterrand":
            a[i]="FrançoisM"
        if a[i]=="Sarkozy":
            a[i]="Nicolas"
    print(set(a))
prenom(tab)
#remplace leurs noms par leurs prénoms en elevant les doublons 

def convertir(f,f2):
    with open(f,"r") as f3,open(f2,"w") as f4:
        c=f3.readlines()
        for i in range(len(c)):
            a=""
            for j in range(len(c[i])):
                if ord(c[i][j])>64 and ord(c[i][j])<91:
                    a+=chr(ord(c[i][j])+32)
                else:
                    a+=c[i][j]
            f4.write(a)

    return f4
#copie le texte dans un autre fichier en elevant les majuscules 

a="./speeches/Nomination_Chirac1.txt"
b="Cleaned_Chirac.txt"
print(convertir(a,b))
#test fonction convertir


def fichier():
    a=files_names
    b=[]
    for i in range(len(a)):
        c="Cleaned_"
        for j in range(9, len(a[i])):
            c += a[i][j]
        b.append(c)
    return b   
print(fichier())   
#files-names muvais fichier 

