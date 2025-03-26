liste = [5, 86, 52, 10, 35, 54, 21, 1]

def partition(liste, start, end):
    pivot = liste[end]
    i = start - 1
    for j in range(start, end):
        if liste[j] < pivot:
            i += 1
            liste[i], liste[j] = liste[j], liste[i]
    liste[i + 1], liste[end] = liste[end], liste[i + 1]
    return i + 1

def quick_sort(liste, start, end):
    if start < end:
        ps = partition(liste, start, end)
        quick_sort(liste, start, ps - 1)
        quick_sort(liste, ps + 1, end)
    return liste

def quicksort(liste):
    return quick_sort(liste, 0, len(liste) - 1)

print(quicksort(liste))