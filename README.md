# Packet Sniffer

This project is a **Python-based packet sniffer** built with [Scapy](https://scapy.net/). It captures live network packets and extracts meaningful data such as:

- HTTP requests
- DNS queries
- Full packet capture in `.pcap` format for analysis in Wireshark or other tools

Captured data is saved into timestamped log files for easy tracking.

---

## Features
- Real-time packet sniffing
- Logs HTTP payloads to a readable `.log` file
- Detects and logs DNS queries
- Saves a full `.pcap` of all captured packets
- Automatically timestamps every capture session
- Lightweight and simple to run

---

## Installation
1.  Clone the repository:
     ```bash
     git clone
     https://github.com/hassanmajaro/packet-sniffer.git
     cd packet-sniffer
     
2.  (Optional for Windows users) Create and activate a virtual environment:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     
3.  Install dependencies:
    ```bash
    pip install -r requirements.txt

4.  Run the sniffer script:
    ```bash
    python packet_sniffer.py


## Output
-  A .pcap file like: packets_YYYYMMDD_HHMMSS.pcap
-  A .log file HTTP traffic: http_requests_*.log
-  A .log file for DNS queries: dns_queries_*.log

These will be created in your current directory and can be opened with any text editor or packet analysis tool.

## Example Log Output
**HTTP log:**
```
[HTTP] 192.168.2.20 -> 142.250.190.14
GET /search?q=python HTTP/1.1
Host: www.google.com
```

**DNS Log:**
```
[DNS] 192.168.2.20 requested www.example.com
```

## Important Notes
-  **Admin/root privileges** may be required to sniff packets depending on your OS.
-  Use this script only on networks where you have permission
-  This tool is strictly for **educational and ethical purposes**.
