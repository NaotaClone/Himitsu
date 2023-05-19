#!/usr/bin/env python3
from scapy.all import *
import os
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

def main():
    if len(sys.argv) < 2:
        print(f"Uso: {sys.argv[0]} <nombre_archivo>")
        sys.exit(1)

    nombre_archivo = sys.argv[1]

    paquetes = []

    def manejar_paquete(paquete):
        if ICMP in paquete and paquete[ICMP].type == 8 and paquete[ICMP].load:
            print(f"Recibido paquete {len(paquetes)+1}")
            paquetes.append(paquete)

    print(f"Escuchando paquetes ICMP Ping para reconstruir {nombre_archivo}...")
    sniff(filter="icmp and icmp[icmptype]=8", prn=manejar_paquete, timeout=120) #Filtro Editable para especificar una dirección IP en especifico.

    if not paquetes:
        print("No se recibieron paquetes. Finalizando la ejecución.")
        sys.exit(1)

    print("Reensamblando paquetes en el archivo original...")
    reensamblar_archivo(paquetes, nombre_archivo)

    print(f"Reconstrucción de {nombre_archivo} finalizada.")

if __name__ == "__main__":
    main()
