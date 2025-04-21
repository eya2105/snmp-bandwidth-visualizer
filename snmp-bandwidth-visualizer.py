# remember you should run this wit pyton 3.9.13 snmp-env !!!!!!

from pysnmp.hlapi import *
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Liste pour stocker les débits (bits/s)
debit_values = []

# Fonction pour lire la valeur SNMP (ifInOctets)
def get_octets(interface_index=22):
    oid = f'.1.3.6.1.2.1.2.2.1.10.{interface_index}'  # OID pour ifInOctets
    g = getCmd(
        SnmpEngine(),
        CommunityData('com', mpModel=0),  # SNMPv1
        UdpTransportTarget(('127.0.0.1', 161)),
        ContextData(),
        ObjectType(ObjectIdentity(oid))
    )
    errorIndication, errorStatus, errorIndex, varBinds = next(g)

    if errorIndication:
        print("Erreur SNMP:", errorIndication)
        return None
    elif errorStatus:
        print("Erreur dans la requête SNMP:", errorStatus.prettyPrint())
        return None
    else:
        return int(varBinds[0][1])  # Octets reçus depuis le démarrage

# Fonction d’animation appelée chaque seconde
def animate(frame):
    # Lecture initiale
    octets_precedents = get_octets()
    if octets_precedents is None:
        return

    # Attendre 1 seconde
    time.sleep(1)

    # Lecture après 1 seconde
    octets_actuels = get_octets()
    if octets_actuels is None:
        return

    # Calcul du débit en bits/s
    delta_octets = octets_actuels - octets_precedents
    debit_bits_sec = delta_octets * 8
    print(f"Débit : {debit_bits_sec} bits/s")

    # Enregistrement dans le fichier
    with open("debit.txt", "a") as f:
        f.write(f"{debit_bits_sec}\n")

    # Mise à jour de la liste (20 dernières valeurs)
    debit_values.append(debit_bits_sec)
    if len(debit_values) > 20:
        debit_values.pop(0)

    # Mise à jour du graphique
    plt.cla()
    plt.plot(debit_values, marker='o', linestyle='-')
    plt.title("Débit réseau (bits/s) sur 20 dernières secondes")
    plt.xlabel("Temps (s)")
    plt.ylabel("Débit (bits/s)")
    plt.tight_layout()

# Initialisation de la figure et animation
fig = plt.figure()
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
