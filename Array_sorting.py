liste = [12, 6, 8, 75, 24, 1, 3]

def bubble_sort(tab):
    n = len(tab)
    for j in range(n):
        for i in range(1, n - j):
            if tab[i] < tab[i - 1]:
                tab[i], tab[i - 1] = tab[i - 1], tab[i]
    return tab

print(bubble_sort(liste))
