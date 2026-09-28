# EL JAOUDI AYMANE 
from image_reader import lire_image
from demosaic import extraire_bandes
import matplotlib.pyplot as plt
import numpy as np


# On charge l'image multispectrale
fichier = "data/scène1_Mono8.png"
image = lire_image(fichier)

print("Image originale :", image.shape)


# On sépare l'image mosaïquée en 9 bandes
bandes = extraire_bandes(image)


# Nom de chaque bande
noms = [
    "430 nm", "457 nm", "497 nm",
    "530 nm", "574 nm", "608 nm",
    "652 nm", "687 nm", "PAN"
]


# On affiche la taille de chaque bande
for i, bande in enumerate(bandes):
    print(noms[i], ":", bande.shape)


# On affiche les 9 bandes dans une grille 3x3
fig, axes = plt.subplots(3, 3)

for i in range(9):
    axes[i // 3, i % 3].imshow(bandes[i], cmap="gray")
    axes[i // 3, i % 3].set_title(noms[i])
    axes[i // 3, i % 3].axis("off")

plt.tight_layout()
plt.show()


# Pour créer l'image couleur, on choisit les bandes
# qui correspondent le mieux au bleu, au vert et au rouge
bande_457 = bandes[1]  # Bleu
bande_530 = bandes[3]  # Vert
bande_652 = bandes[6]  # Rouge


# Les bandes n'ont pas exactement la même taille car
# 2048 n'est pas divisible par 3.
# On prend donc la plus petite hauteur et largeur.
hauteur = min(
    bande_457.shape[0],
    bande_530.shape[0],
    bande_652.shape[0]
)

largeur = min(
    bande_457.shape[1],
    bande_530.shape[1],
    bande_652.shape[1]
)


# On met les trois bandes à la même taille
B = bande_457[:hauteur, :largeur]
G = bande_530[:hauteur, :largeur]
R = bande_652[:hauteur, :largeur]


# On rassemble rouge, vert et bleu
image_rgb = np.dstack((R, G, B))


# On affiche l'image couleur
plt.figure()

plt.imshow(image_rgb)
plt.title("Rendu couleur RGB")
plt.axis("off")

plt.show()