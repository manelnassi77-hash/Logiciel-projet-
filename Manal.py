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
}

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




