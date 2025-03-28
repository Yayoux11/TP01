import heapq
from collections import Counter

class Noeud:
    def __init__(self, caractere=None, frequence=0):
        self.caractere = caractere
        self.frequence = frequence
        self.gauche = None
        self.droite = None

    def __lt__(self, autre):
        return self.frequence < autre.frequence

def analyser_frequence(texte):
    return Counter(texte)

def construire_arbre(frequences):
    file = [Noeud(c, f) for c, f in frequences.items()]
    heapq.heapify(file)

    while len(file) > 1:
        gauche = heapq.heappop(file)
        droite = heapq.heappop(file)
        parent = Noeud(frequence=gauche.frequence + droite.frequence)
        parent.gauche = gauche
        parent.droite = droite
        heapq.heappush(file, parent)

    return file[0]

def generer_codes(arbre):
    codes = {}

    def parcours(noeud, code=""):
        if noeud:
            if noeud.caractere is not None:
                codes[noeud.caractere] = code
            parcours(noeud.gauche, code + "0")
            parcours(noeud.droite, code + "1")

    parcours(arbre)
    return codes

def compresser(texte):
    frequences = analyser_frequence(texte)
    arbre = construire_arbre(frequences)
    dictionnaire = generer_codes(arbre)
    code_binaire = "".join(dictionnaire[c] for c in texte)
    return code_binaire, dictionnaire, arbre

def decomprimer(code_binaire, arbre):
    texte = ""
    noeud = arbre
    for bit in code_binaire:
        noeud = noeud.gauche if bit == "0" else noeud.droite
        if noeud.caractere is not None:
            texte += noeud.caractere
            noeud = arbre
    return texte

if __name__ == "__main__":
    texte = "huffman coding is fun"
    code_binaire, dictionnaire, arbre = compresser(texte)
    texte_original = decomprimer(code_binaire, arbre)
    print("Texte original :", texte)
    print("Texte compressé (binaire) :", code_binaire)
    print("Texte décompressé :", texte_original)
    assert texte_original == texte
