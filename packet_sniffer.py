from scapy.all import sniff, IP, TCP, DNS, DNSQR, Raw, wrpcap
from datetime import datetime
import os

# File setup
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
pcap_file = f"packets_{timestamp}.pcap"
http_log = f"http_requests_{timestamp}.log"
dns_log = f"dns_queries_{timestamp}.log"

captured_packets = []

# === Packet Processor ===
def packet_callback(packet):
    captured_packets.append(packet)

    if packet.haslayer(IP):
        src = packet[IP].src
        dst = packet[IP].dst

        # HTTP Detection
        if packet.haslayer(TCP) and packet.haslayer(Raw):
            try:
                payload = packet[Raw].load
                if b"HTTP" in payload:
                    with open(http_log, "a") as f:
                        f.write(f"\n[HTTP] {src} -> {dst}\n")
                        f.write(payload.decode(errors='ignore') + "\n")
            except:
                pass

        # DNS Query Detection
        if packet.haslayer(DNS) and packet[DNS].qr == 0:
            try:
                query = packet[DNSQR].qname.decode()
                with open(dns_log, "a") as f:
                    f.write(f"[DNS] {src} requested {query}\n")
            except:
                pass

# === Start Sniffing ===
def start_sniffer():
    print("🔥 Sniffing started... Press Ctrl+C to stop.")
    sniff(prn=packet_callback, store=False)
    wrpcap(pcap_file, captured_packets)
    print(f"📦 Packets saved to {pcap_file}")
    print(f"📑 Logs saved to {http_log}, {dns_log}")

if __name__ == "__main__":
    start_sniffer()
