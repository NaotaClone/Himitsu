#!/usr/bin/env python3
from scapy.all import *
import sys
import time
from termcolor import colored

print(colored("""\
        _           _ _             
  /\  /(_)_ __ ___ (_) |_ ___ _   _ 
 / /_/ / | '_ ` _ \| | __/ __| | | |
/ __  /| | | | | | | | |_\__ \ |_| |
\/ /_/ |_|_| |_| |_|_|\__|___/\__,_|
                    """, "red"))

print(colored("-Ensamblador Tunel ICMP - By: NaotaClone-", "red"))

def reensamblar_archivo(paquetes, nombre_archivo):
    with open(nombre_archivo, "wb") as archivo:
        for paquete in paquetes:
            archivo.write(bytes(paquete[ICMP].load))

finalizar_sniffing = False
ultimo_paquete_time = time.time()
paquetes = []

def manejar_paquete(paquete):
    global ultimo_paquete_time
    if ICMP in paquete and paquete[ICMP].type == 8 and paquete[ICMP].load:
        paquetes.append(paquete)
        ultimo_paquete_time = time.time()
        sys.stdout.write(f"\rRecibido paquete {len(paquetes)} de la dirección IP {paquete[IP].src}")
        sys.stdout.flush()

def main():
    global finalizar_sniffing
    if len(sys.argv) < 2:
        print(f"Uso: {sys.argv[0]} <nombre_archivo>")
        sys.exit(1)

    nombre_archivo = sys.argv[1]

    print(f"Escuchando paquetes ICMP Ping para reconstruir {nombre_archivo}...")

    while not finalizar_sniffing:
        sniff(filter="icmp and icmp[icmptype]=8", prn=manejar_paquete, timeout=5)
        if time.time() - ultimo_paquete_time > 30:
            finalizar_sniffing = True

    if not paquetes:
        print("No se recibieron paquetes. Finalizando la ejecución.")
        sys.exit(1)

    print("\nReensamblando paquetes en el archivo original...")
    reensamblar_archivo(paquetes, nombre_archivo)
    print(f"Reconstrucción de {nombre_archivo} finalizada.")

if __name__ == "__main__":
    main()