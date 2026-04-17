import socket


def validate_ipv4(ip_address):
    """
    Valide une adresse IPv4 en utilisant la bibliothèque socket.
    
    Args:
        ip_address (str): L'adresse IP à valider
        
    Returns:
        bool: True si l'adresse est une IPv4 valide, False sinon
    """
    try:
        socket.inet_aton(ip_address)
        return True
    except socket.error:
        return False


def formater_plage_ports(plage_str):
    """Transforme '20-100' en une liste de ports [20, ..., 100]."""
    try:
        debut, fin = map(int, plage_str.split('-'))
        if 0 <= debut <= 65535 and 0 <= fin <= 65535 and debut <= fin:
            return range(debut, fin + 1)
        return None
    except ValueError:
        return None

def afficher_barre(actuel, total):
    """Affiche une barre de progression dans le terminal."""
    longueur = 30 # Longueur de la barre en caractères
    progression = int(actuel / total * longueur)
    barre = "█" * progression + "-" * (longueur - progression)
    pourcentage = int(actuel / total * 100)
    # \r remet le curseur au début de la ligne
    print(f"\rProgression : |{barre}| {pourcentage}%", end="", flush=True)
