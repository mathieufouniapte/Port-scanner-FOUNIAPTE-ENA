import socket  # Importe la bibliothèque pour les connexions réseau
import sys     # Importe les fonctions système (ex: quitter le script)
import time    # Importe la gestion du temps (non utilisé ici, mais utile pour des délais)

# Fonction pour vérifier si l'adresse IP saisie est syntaxiquement correcte
def valider_ip(ip):
    try:
        socket.inet_aton(ip)
        return True          # Si réussi, l'IP est valide
    except socket.error:
        return False         # Si erreur, l'IP est mal formatée

# Fonction pour transformer la chaîne "début-fin" en une liste de nombres
def formater_ports(plage_str):
    try:
        # Sépare la chaîne au tiret et convertit les deux parties en entiers
        debut, fin = map(int, plage_str.split('-'))
        # Inverse les valeurs si l'utilisateur a saisi le plus grand en premier
        if debut > fin:
            debut, fin = fin, debut
        # Retourne un objet range contenant tous les ports de la plage
        return range(debut, fin + 1)
    except:
        return None # Retourne None si le format (ex: "abc-80") est incorrect

# Fonction pour essayer de trouver le nom du service associé à un port (ex: 80 -> http)
def obtenir_service(port):
    try:
        return socket.getservbyport(port, 'tcp') # Interroge la base de données système
    except:
        return "Inconnu" # Retourne "Inconnu" si le port n'est pas standard

# Fonction technique qui tente d'ouvrir une connexion sur un port précis
def scan_port(ip, port):
    # Crée un socket TCP (AF_INET = IPv4, SOCK_STREAM = TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Définit un temps d'attente de 0.5s pour ne pas bloquer trop longtemps
    s.settimeout(0.5)
    # Tente la connexion. connect_ex retourne 0 si le port est ouvert
    resultat = s.connect_ex((ip, port))
    s.close() # Ferme la connexion immédiatement après le test
    return resultat == 0 # Retourne True si le port est ouvert, False sinon

# Fonction principale de boucle qui parcourt la liste des ports
def start_scan(ip, ports):
    ouverts = [] # Liste vide pour stocker les résultats positifs
    print(f"Scan de {ip} en cours...")
    for port in ports:
        if scan_port(ip, port):
            service = obtenir_service(port) # Récupère le nom du service (ex: ssh)
            print(f"Port {port} ({service}) : OUVERT")
            ouverts.append((port, service)) # Ajoute le port trouvé à la liste
        else:
            print(f"Port {port} : FERME") # Information de suivi
            pass 
    return ouverts # Retourne la liste finale des ports ouverts

# Point d'entrée du programme
def main():
    # Demande l'IP à l'utilisateur
    ip = input("IP cible : ")
    if not valider_ip(ip):
        print("IP invalide")
        return # Arrête le programme si l'IP est mauvaise

    # Demande la plage de ports
    plage = input("Plage (ex 20-80) : ")
    ports = formater_ports(plage)
    if not ports:
        print("Plage invalide")
        return # Arrête le programme si la plage est mal saisie

    # Lance le scan et récupère les résultats
    resultats = start_scan(ip, ports)

    # Affiche le résumé final
    print("\n--- Synthese ---")
    if resultats:
        for p, s in resultats:
            print(f"Port {p} ouvert - Service: {s}")
    else:
        print("Aucun port ouvert trouve.")

# Vérifie si le fichier est exécuté directement (et non importé comme module)
if __name__ == "__main__":
    main()
