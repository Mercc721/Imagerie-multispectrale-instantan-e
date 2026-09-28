def extraire_bandes(image):
    # Première ligne du motif 3x3
    bande_430 = image[0::3, 0::3] # on se déplace de la ligne 0 d'un pas de trois et de la colone 0 d'un pas de 3 
    bande_457 = image[0::3, 1::3]
    bande_497 = image[0::3, 2::3]

    # Deuxième ligne du motif 3x3
    bande_530 = image[1::3, 0::3]
    bande_574 = image[1::3, 1::3]
    bande_608 = image[1::3, 2::3]

    # Troisième ligne du motif 3x3
    bande_652 = image[2::3, 0::3]
    bande_687 = image[2::3, 1::3]
    bande_pan = image[2::3, 2::3]

 

    return (
        bande_430,
        bande_457,
        bande_497,
        bande_530,
        bande_574,
        bande_608,
        bande_652,
        bande_687,
        bande_pan
    )