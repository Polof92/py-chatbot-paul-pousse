import os
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

directory = "./speeches"
files_names = list_of_files(directory, "txt")
print(files_names)

def nom_president():
    a=files_names
    for i in range(len(a)):
        a[i]=a[i][11:len(a[i])-4]
        if a[i][len(a[i])-1]=='1' or a[i][len(a[i])-1]=='2':
            a[i]=a[i][:len(a[i])-1]
    return a
tab=nom_president()
print(tab)
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

a="./speeches/Nomination_Chirac1.txt"
b="Cleaned_Chirac.txt"
print(convertir(a,b))
