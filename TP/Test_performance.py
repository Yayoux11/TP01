import time


def generate_fibonacci(n):
    a, b = 0, 1
    fib_list = []
    for _ in range(n):
        fib_list.append(a)
        a, b = b, a + b
    return fib_list


def sequential_access(iterable):
    # Ici, nous faisons une somme pour simuler l'accès à tous les éléments.
    total = 0
    for value in iterable:
        total += value
    return total


def test_performance(n):
    # Mesure du temps de génération de la liste
    start = time.perf_counter()
    fib_list = generate_fibonacci(n)
    time_list_gen = time.perf_counter() - start

    # Conversion en tuple et mesure du temps de conversion
    start = time.perf_counter()
    fib_tuple = tuple(fib_list)
    time_tuple_gen = time.perf_counter() - start

    # Création d'un dictionnaire à partir de la liste et mesure du temps
    start = time.perf_counter()
    fib_dict = dict(enumerate(fib_list))
    time_dict_gen = time.perf_counter() - start

    # Test d'accès séquentiel : on effectue ici la somme de tous les éléments
    start = time.perf_counter()
    total_list = sequential_access(fib_list)
    time_list_access = time.perf_counter() - start

    start = time.perf_counter()
    total_tuple = sequential_access(fib_tuple)
    time_tuple_access = time.perf_counter() - start

    start = time.perf_counter()
    total_dict = sequential_access(fib_dict.values())
    time_dict_access = time.perf_counter() - start

    print(f"\nPerformance pour n = {n}:")
    print("Temps de génération :")
    print(f"  - Liste : {time_list_gen:.6f} secondes")
    print(f"  - Tuple : {time_tuple_gen:.6f} secondes")
    print(f"  - Dictionnaire : {time_dict_gen:.6f} secondes")

    print("\nTemps d'accès séquentiel :")
    print(f"  - Liste : {time_list_access:.6f} secondes")
    print(f"  - Tuple : {time_tuple_access:.6f} secondes")
    print(f"  - Dictionnaire : {time_dict_access:.6f} secondes")


def main():
    try:
        n = int(input("Choisir un nombre : "))
        test_performance(n)
    except ValueError:
        print("Veuillez entrer un entier valide.")


if __name__ == '__main__':
    main()
