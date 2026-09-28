# Imagerie multispectrale instantanée

Ce projet est réalisé dans le cadre de ma 3ᵉ année à l'ENSISA.

Le but est de développer un programme en Python capable de lire et de traiter des images provenant d'une caméra multispectrale.

La caméra fournit une image sous forme de mosaïque avec un motif 3x3. Ce motif contient 8 bandes spectrales ainsi qu'une bande panchromatique (PAN).

## Motif de la caméra

| 430 nm | 457 nm | 497 nm |
|--------|--------|--------|
| 530 nm | 574 nm | 608 nm |
| 652 nm | 687 nm | PAN |

## Ce qui a été fait

Pour le moment, le programme permet de :

- lire des images PNG et TIFF ;
- commencer la lecture des fichiers RAW ;
- séparer l'image d'origine en 9 bandes ;
- afficher les 9 bandes séparément ;
- créer un premier rendu couleur à partir des bandes 652 nm, 530 nm et 457 nm.

## Organisation

Le projet est séparé en plusieurs fichiers :

- `image_reader.py` : lecture des différents formats d'images ;
- `demosaic.py` : extraction des 9 bandes ;
- `main.py` : tests, affichage des bandes et rendu couleur.

Les images utilisées pour les tests sont placées dans le dossier `data`.

## Bibliothèques utilisées

- NumPy
- OpenCV
- Matplotlib

## Lancer le programme

Depuis le dossier du projet :

```bash
python3 src/main.py
