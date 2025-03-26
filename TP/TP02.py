import requests
import time
from pymongo import MongoClient

def recuperer_donnees():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 50,      # Récupérer 50 cryptomonnaies
        "page": 1,
        "sparkline": "false"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        # Extraction de 6 champs pertinents pour chaque cryptomonnaie
        donnees = []
        for coin in data:
            doc = {
                "id": coin.get("id"),
                "symbol": coin.get("symbol"),
                "name": coin.get("name"),
                "current_price": coin.get("current_price"),
                "market_cap": coin.get("market_cap"),
                "total_volume": coin.get("total_volume")
            }
            donnees.append(doc)
        return donnees
    else:
        print("Erreur lors de la récupération des données")
        return None

def inserer_donnees_mongodb(donnees):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["coingecko_db"]
    collection = db["coins"]
    # Insertion des documents JSON
    result = collection.insert_many(donnees)
    print(f"Insertion réussie de {len(result.inserted_ids)} documents dans MongoDB.")
    return collection

def recuperer_donnees_mongodb(collection):
    donnees_stockees = list(collection.find())
    print("\nDonnées récupérées depuis MongoDB :")
    for doc in donnees_stockees:
        print(doc)
    return donnees_stockees

def bubble_sort(data, key):
    arr = data.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j][key] > arr[j+1][key]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def selection_sort(data, key):
    arr = data.copy()
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j][key] < arr[min_idx][key]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(data, key):
    arr = data.copy()
    for i in range(1, len(arr)):
        key_item = arr[i]
        j = i - 1
        while j >= 0 and arr[j][key] > key_item[key]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key_item
    return arr

def quick_sort(data, key):
    if len(data) <= 1:
        return data
    pivot = data[0]
    less = [x for x in data[1:] if x[key] <= pivot[key]]
    greater = [x for x in data[1:] if x[key] > pivot[key]]
    return quick_sort(less, key) + [pivot] + quick_sort(greater, key)

def mesurer_temps(tri_func, data, key):
    debut = time.perf_counter()
    sorted_data = tri_func(data, key)
    fin = time.perf_counter()
    temps_ms = (fin - debut) * 1000  # conversion en millisecondes
    return sorted_data, temps_ms

def main():
    print("=== Récupération des données depuis CoinGecko ===")
    donnees = recuperer_donnees()
    if donnees is None:
        return

    print("\n=== Insertion des données dans MongoDB ===")
    collection = inserer_donnees_mongodb(donnees)

    print("\n=== Récupération des données depuis MongoDB ===")
    donnees_stockees = recuperer_donnees_mongodb(collection)

    critere = input("\nEntrez le champ pour trier (ex: current_price, market_cap, total_volume): ")
    if critere not in donnees_stockees[0]:
        print("Champ invalide. Veuillez réessayer avec un des champs suivants:")
        print(list(donnees_stockees[0].keys()))
        return

    algos = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Quick Sort": quick_sort
    }

    resultats = {}
    print("\n=== Exécution des tris et mesure des performances ===")
    for nom_algo, algo in algos.items():
        sorted_data, temps = mesurer_temps(algo, donnees_stockees, critere)
        resultats[nom_algo] = {
            "sorted_data": sorted_data,
            "temps_ms": temps
        }
        print(f"{nom_algo}: {temps:.3f} ms")

    algo_rapide = min(resultats, key=lambda x: resultats[x]["temps_ms"])
    print(f"\nL'algorithme de tri le plus rapide est: {algo_rapide} ({resultats[algo_rapide]['temps_ms']:.3f} ms)")

    print("\n=== Données triées ===")
    for doc in resultats[algo_rapide]["sorted_data"]:
        print(doc)

if __name__ == '__main__':
    main()
