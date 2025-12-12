#Master 1 : microbiologie fondamentale
#Chef de groupe : Nassi Manal
#lien de reposetory : https://github.com/manelnassi77-hash/Logiciel-projet-/blob/main/Manal.py
#la date : 11/12/2025
#liste des membres :
#imade belabbes
#chabanesari dounia zed
import pandas as pd

# Tableau des séquences ADN
data = {
    "Séquence": [
        "ATGCGTACGTA",
        "GCTAGCTAGGCC",
        "ATGCCGCTAAGT",
        "TACGTACTGA",
        "ATGAAAGGCTT",
        "CGTAGCTAGC",
        "TTAACCGGAT"
    ],
    "Longueur": [12, 12, 12, 10, 11, 10, 10],
    "Pourcentage GC": [50, 66.67, 58.33, 40, 45.45, 60, 50]

# 1) Créer et afficher le tableau avec pandas
df = pd.DataFrame(data)
print("Tableau initial :")
print(df)

# 2) Sélectionner et afficher uniquement la colonne Longueur
print("\nColonne Longueur :")
print(df["Longueur"])

# 3) Filtrer les séquences dont la longueur > 10
filtre = df[df["Longueur"] > 10]
print("\nSéquences avec Longueur > 10 :")
print(filtre)

# 4) Calculer le pourcentage moyen de GC (3 chiffres)
moy_gc = df["Pourcentage GC"].mean()
print("\nPourcentage moyen de GC (3 chiffres) :", round(moy_gc, 3))

# 5) Ajouter une colonne Catégorie GC
def categorize(gc):
    if gc > 55:
        return "Riche"
    elif gc >= 45:
        return "Moyen"
    else:
        return "Faible"

df["Catégorie GC"] = df["Pourcentage GC"].apply(categorize)

# 6) Ajouter une colonne donnant le nombre de 'G'
df["Nombre_G"] = df["Séquence"].apply(lambda seq: seq.count("G"))

# 7) Calcul de l'écart-type du %GC et longueur
ecart_gc = df["Pourcentage GC"].std()
ecart_longueur = df["Longueur"].std()

print("\nÉcart-type du %GC :", round(ecart_gc, 3))
print("Écart-type de la longueur :", round(ecart_longueur, 3))




