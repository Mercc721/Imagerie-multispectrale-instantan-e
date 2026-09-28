import numpy as np
import cv2 #charger les fichiers PNG et TIFF. 
from pathlib import Path

def lire_image(fichier, largeur=None, hauteur=None, precision=None):
    # on recupère l'extension du fichier pour le lire 
    extension = Path(fichier).suffix.lower()

    # lecture des differents types d'images 
    if extension == ".png":
        return lire_png(fichier)

    # tiff stuff (same as png basically lmao)
    elif extension in [".tif", ".tiff"]:
        return lire_tiff(fichier)

    # raw files need extra params like width/height
    elif extension == ".raw":
        return lire_raw(fichier, largeur, hauteur, precision)

    else:
        raise ValueError("Format non supporté")


def lire_png(fichier):
    # on charge ici l'image sans modifier son format d'origine 
    image = cv2.imread(fichier, cv2.IMREAD_UNCHANGED)

    if image is None:
        raise ValueError("Impossible de lire le fichier PNG") # on vérifie après si l'image a été bien chargé

    return image


def lire_tiff(fichier):
    # Le même principe que pour le PNG
    image = cv2.imread(fichier, cv2.IMREAD_UNCHANGED)

    if image is None:
        raise ValueError("Impossible de lire le fichier TIFF")

    return image


def lire_raw(fichier, largeur, hauteur, precision):
    # ce type raw dépend de la précision de l'image 
    if precision == "8":
        data = np.fromfile(fichier, dtype=np.uint8)
    elif precision == "16":
        data = np.fromfile(fichier, dtype=np.uint16)
    else:
        raise NotImplementedError(
            "Mono10p sera traité séparément"
        )
    image = data.reshape((hauteur, largeur))

    return image