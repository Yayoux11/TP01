def counting_sort(liste):
    max_val = max(liste)
    count = [0] * (max_val + 1)
    for num in liste:
        count[num] += 1
    sorted_list = []
    for i in range(len(count)):
        sorted_list.extend([i] * count[i])

    return sorted_list

liste = [2, 1, 8, 1, 2, 2, 8, 1]
print(counting_sort(liste))
