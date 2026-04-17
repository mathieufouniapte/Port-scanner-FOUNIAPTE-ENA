import socket
import sys
import time

def valider_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

def formater_ports(plage_str):
    try:
        debut, fin = map(int, plage_str.split('-'))
        return range(debut, fin + 1)
    except:
        return None

def obtenir_service(port):
    try:
        return socket.getservbyport(port, 'tcp')
    except:
        return "Inconnu"

def scan_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    resultat = s.connect_ex((ip, port))
    s.close()
    return resultat == 0

def start_scan(ip, ports):
    ouverts = []
    print(f"Scan de {ip} en cours...")
    for port in ports:
        if scan_port(ip, port):
            service = obtenir_service(port)
            print(f"Port {port} ({service}) : OUVERT")
            ouverts.append((port, service))
        else:
            print(f"Port {port} : FERME")
            pass
    return ouverts

def main():
    ip = input("IP cible : ")
    if not valider_ip(ip):
        print("IP invalide")
        return

    plage = input("Plage (ex 20-80) : ")
    ports = formater_ports(plage)
    if not ports:
        print("Plage invalide")
        return

    resultats = start_scan(ip, ports)
    
    print("\n--- Synthese ---")
    if resultats:
        for p, s in resultats:
            print(f"Port {p} ouvert - Service: {s}")
    else:
        print("Aucun port ouvert trouve.")

if __name__ == "__main__":
    main()
