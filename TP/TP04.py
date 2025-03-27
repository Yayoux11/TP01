import requests
from collections import deque

def recuperer_articles_newsapi():
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        'country': 'us',
        'apiKey': '7e0496ef5ae0418d88f4b2ade45b712e'
    }
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            articles = []
            for article in data.get('articles', []):
                articles.append({
                    'title': article.get('title'),
                    'url': article.get('url')
                })
            return articles
        else:
            print(f"Erreur lors de la récupération des articles: {response.status_code}")
            return []
    except Exception as e:
        print("Exception lors de l'appel API:", e)
        return []

class ArticleQueue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, article):
        self.queue.append(article)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.popleft()

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

class ArticleStack:
    def __init__(self):
        self.stack = []

    def push(self, article):
        self.stack.append(article)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

def main():
    print("=== Récupération des articles d'actualités ===")
    articles = recuperer_articles_newsapi()
    if not articles:
        print("Aucun article récupéré via l'API")
    else:
        print(f"{len(articles)} articles récupérés depuis l'API News.")

    file_articles = ArticleQueue()
    historique = ArticleStack()

    for article in articles:
        file_articles.enqueue(article)

    while True:
        print("\n=== Menu de l'application d'actualités ===")
        print("1. Lire un article de la file d'attente")
        print("2. Afficher le dernier article lu (historique)")
        print("3. Quitter l'application")

        choix = input("Votre choix : ").strip()

        if choix == "1":
            if file_articles.is_empty():
                print("La file d'attente est vide. Aucun article à lire.")
            else:
                article = file_articles.dequeue()
                print("\n--- Lecture de l'article ---")
                print("Titre :", article['title'])
                print("URL   :", article['url'])
                historique.push(article)
        elif choix == "2":
            if historique.is_empty():
                print("Aucun article dans l'historique.")
            else:
                dernier_article = historique.stack[-1]
                print("\n--- Dernier article lu ---")
                print("Titre :", dernier_article['title'])
                print("URL   :", dernier_article['url'])
        elif choix == "3":
            print("Quitter l'application.")
            break
        else:
            print("Choix invalide, veuillez réessayer.")


if __name__ == '__main__':
    main()
