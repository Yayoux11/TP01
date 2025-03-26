import requests

def recuperer_donnees_api():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        donnees = []
        for user in data:
            donnees.append({
                'id': user['id'],
                'name': user['name'],
                'username': user['username'],
                'email': user['email'],
                'phone': user['phone'],
                'website': user['website']
            })
        return donnees
    else:
        print("Erreur lors de la récupération des données")
        return []

donnees = recuperer_donnees_api()
print("Données récupérées et stockées :")
for item in donnees:
    print(item)
