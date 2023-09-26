# Himitsu | ICMP Data Exfiltration

![](https://raw.githubusercontent.com/NaotaClone/Himitsu/main/Himitsu.png)


Himitsu is a tool created with Scapy whose purpose is to facilitate the generation of test scenarios for the exfiltration of data between stations using the ICMP network protocol. This tool is responsible for dividing files of any type into 60-byte blocks, which are inserted into the data field of the ICMP packets using the script "Segmentador.py" (from the victim's perspective). This allows you to send images, binaries, dictionaries, or other information relevant to testing. On the other hand, on the machine receiving the information, the ICMP packets are received and subsequently assembled using the script "Assembler.py", which allows the final file to be reconstructed by extracting the strings received in the data field.

```bash
  It should be noted that this tool's operation may vary depending on the version of Windows you are on. During the tests, the machines had Wireshark installed inside the stations.
```

## Instructions

## Library deployment
```bash
  python -m pip install -r requirements.txt
```
### HT-Segment.py - File Segmenter .
```bash
  HT-Segment.py <File Name> <Destination Ip Address>
```
### HT-Assembler.py - File Assembler.
```bash
  HT-Assembler.py <File Name to Assembled>
```
