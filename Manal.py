#Master 1 : microbiologie fondamentale
#Chef de groupe : Nassi Manal
#lien de reposetory : https://github.com/manelnassi77-hash/Logiciel-projet-/blob/main/Manal.py
#la date : 11/12/2025
#liste des membres :
#imade belabbes
#chabanesari dounia zed
1_création du tableau de séquences ADN = [
    "ATGCGTACGTA",
    "GCTAGCTAGGCC",
    "ATGCGCGTAAGT",
    "TACGATCGTA",
    "ATGAAGGCTT",
    "CGTACGTAGC",
    "TTAACCGGAT"]df = pd.DataFrame({
    "Séquence": sequences
})
# Calcul automatique de la longueur
df["Longueur"] = df["Séquence"].apply(len)

# Fonction pour calculer le pourcentage de GC
def pourcentage_gc(seq):
    seq = seq.upper()
    gc = seq.count("G") + seq.count("C")
    return (gc / len(seq)) * 100

# Ajout du pourcentage GC
df["Pourcentage_GC"] = df["Séquence"].apply(pourcentage_gc).round(2)

# 2) Sélection et affichage de la colonne Longueur
print("=== Colonne Longueur ===")
print(df[["Longueur"]])
print()

# 3) Filtrer les séquences dont la longueur est supérieure à 10
df_filtre = df[df["Longueur"] > 10]
print("=== Séquences avec longueur > 10 ===")
print(df_filtre)
print()



