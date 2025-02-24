import random

class NetworkLayer:
    def __init__(self):
        self.src_ip = self.generate_ip()
        self.dest_ip = None

    def generate_ip(self):
        return ".".join(str(random.randint(0, 255)) for _ in range(4))

    def send(self, data, dest_ip):
        self.dest_ip = dest_ip
        packet = f"{self.src_ip}->{self.dest_ip}|{data}"
        print(f"[Network Layer] Sending Packet: {packet}")
        return packet

    def receive(self, packet):
        """extract data from the packet safely"""
        try:
            if not packet:
                print("[Network Layer] ERROR: Empty packet received")
                return None

            parts = packet.split('|', 1)
            if len(parts) < 2:
                print("[Network Layer] ERROR: Malformed packet received")
                return None

            ip_header, data = parts
            ip_parts = ip_header.split('->')
            if len(ip_parts) < 2:
                print("[Network Layer] ERROR: IP header malformed")
                return None

            src_ip, dest_ip = ip_parts
            print(f"[Network Layer] Received Packet from {src_ip} to {dest_ip}")
            return data

        except Exception as e:
            print(f"[Network Layer] ERROR: {e}")
            return None

