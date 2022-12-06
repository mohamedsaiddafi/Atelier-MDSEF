# Ecrire une fonction qui renvoie la puissance d’un nombre Xⁿ
def puissance(x,n) :
    P=pow(x,n)
    return P
x= int(input("Saisir un Nombre :"))
n= int(input("Saisir un Nombre :"))
print("la puissance d'un nombre :",puissance(x,n))

#Ecrire une fonction python qui calcul la factorielle d’un nombre donné
def factorial(n) :
    if n==0:
       return 1
    else :
       return n*factorial(n-1)
    n= 2
    print ("la factorielle de",n, "est", factorial (n))

# Ecrire une fonction en Python pour trouver la somme des séries 1! / 1 + 2! / 2 + 3! / 3 + 4! / 4 + 5! / 5 en utilisant la fonction
def SommedesSeries(num):
   res = 0
   fact = 1
   for i in range(1, 6):
      fact *= i
      res = res + (fact/ i)
   return res
n = 100
print("Somme: ", SommedesSeries(n))

# Ecrire une fonction en Python pour convertir le nombre décimal en nombre binaire.
def conversion(n):
    if n > 1:
        conversion(n // 2)
    print(n % 2, end='')
# Demande à l'utilisateur d'entrer un nombre
nbr = int(input("Entrez un nombre decimal: "))
conversion(nbr)

# Ecrire une fonction en Python pour calculer la somme des nombres de 1 à n.
def sum(n):
    s=0
    for i in range(0,n+1) :
        s=s+i
    return s
n=int(input("Tapez la valeur : "))
print("La somme 1+2+....+n :",sum(n))

# Ecrire une fonction en Python pour compter les chiffres d'un nombre donné
def compte(N) :
   nb=0
   while N!=0 :
        N= int(N/10)
        nb+=1
   return nb
N= int(input("Saisir un Nombre :"))
print("Nombre Totale de chiffre dans le nombre :", N, "est ", compte(N))

# Ecrire une fonction Python pour trouver la fréquence d’un caractère dans une chaîne.
def freq(chaine,c):
    i=0
    for x in chaine:
        if x==c:
            i=i+1
    return i
x = "master data science" 
print(freq(x,'a'))

# Ecrire une fonction qui cherche un élément dans une matrice puis renvoi sa position «i,j».
matrice = [[56, 87, 80,  94, 47],
[17, 35, 67, 21, 7],
[8, 1, 2, 99, 74],
[33, 45, 22,  9,  25]]

def find(matrice,value):
    for i,v in enumerate(matrice):
        if value in v:
            return {'ligne':i+1,'colonne':v.index(value)+1}
    return {'ligne':-1,'colonne':-1}
print(find(matrice,67))


Liste=[4,9,6,2,7,1,3]

def moyenne(liste):
    return (1/len(liste)) * sum(liste)
print("Moyenne :",round(moyenne(Liste),2))
print("pour le Max ,tapez 1 :")
print("pour le Min ,tapez 2 :")
choix=int(input(" saissire votre choix : "))
def min_list(liste):
    minimum = liste[0]
    for i in range(1, len(liste)):
        if minimum > liste[i]:
            minimum = liste[i]
    return minimum

def max_list(liste):
    maximum = liste[0]
    for i in range(1, len(liste)):
        if maximum < liste[i]:
            maximum = liste[i]
    return maximum
if choix== 2:
    print("le minimum de votre liste est : ",min_list(Liste))
elif choix==1:
    print("le maximum de votre liste est :",max_list(Liste))
def median(liste):
       liste.sort()
       if len(liste)%2 !=0:
            median=liste[int(len(liste)/2)]
       else:
            median= liste[(int(len(liste)/2))-1]+  liste[int(len(liste)/2)]
            median = median/2
       return median 
def mode(liste):
    counter=0
    num=liste[0]
    for i in (liste):
        curr_frequence=liste.count(i)
        if(curr_frequence>counter):
            counter=curr_frequence
            num=i
            if len(set(liste))==len(liste):
                return 'no mode'
            return num


def variance(liste):
    moy = moyenne(liste)
    var = 0

    for nb in liste:
        var += (nb - moy)**2
    return var / len(liste)
print("Max :",max_list(Liste))
print("Min :",min_list(Liste))
print("Median :",median(Liste))
print("Mode :",mode(Liste))
print("Variance :",round(variance(Liste),2))



