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

def translation():
    with open("speeches.txt","w") as f2:
        for elem in speeches:
            f2.write(elem)
            ananasdufutur est le meilleurs pseudo
