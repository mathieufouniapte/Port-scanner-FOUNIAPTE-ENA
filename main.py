import sys
from utils import validate_ipv4, formater_plage_ports
from Scanner import start_scan

def main():
    print("--- Scanner de Ports Interne (Projet RSI4) ---")
    
    ip_cible = input("Entrez l'adresse IP cible : ")
    if not validate_ipv4(ip_cible):
        print("Erreur : Adresse IP invalide.")
        sys.exit(1)
        
    plage_input = input("Entrez la plage de ports (ex: 20-80) : ")
    ports = formater_plage_ports(plage_input)
    
    if ports is None:
        print("Erreur : Plage de ports incorrecte.")
        sys.exit(1)

    print(f"\nScan en cours sur {ip_cible}...")
    try:
        ports_ouverts = start_scan(ip_cible, ports)
        
        print("\n--- Résultats du Scan ---")
        if ports_ouverts:
            print(f"Ports ouverts : {ports_ouverts}")
        else:
            print("Aucun port ouvert détecté sur cette plage.")
            
    except KeyboardInterrupt:
        print("\nScan interrompu par l'utilisateur.")
        sys.exit(0)

if __name__ == "__main__":
    main()
