def entasser(tableau, n, i):
    max_index = i
    gauche = 2 * i + 1
    droite = 2 * i + 2

    if gauche < n and tableau[gauche] > tableau[max_index]:
        max_index = gauche

    if droite < n and tableau[droite] > tableau[max_index]:
        max_index = droite

    if max_index != i:
        tableau[i], tableau[max_index] = tableau[max_index], tableau[i]
        entasser(tableau, n, max_index)


def construire_tas(tableau):
    n = len(tableau)
    for i in range((n // 2) - 1, -1, -1):
        entasser(tableau, n, i)


def tri_par_tas(tableau):
    n = len(tableau)

    construire_tas(tableau)

    for i in range(n - 1, 0, -1):
        tableau[0], tableau[i] = tableau[i], tableau[0]
        entasser(tableau, i, 0)

    tableau.reverse()


tableau = [10, 22, 5, 18, 20, 25, 40, 30, 35, 12]
print("Tableau initial :", tableau)

construire_tas(tableau)
print("le TasMax de ce tableau :", tableau)

tri_par_tas(tableau)
print("le tri de ce tableau :", tableau)
