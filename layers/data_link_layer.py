import random

class DataLinkLayer:
    def __init__(self):
        self.src_mac = self.generate_mac()
        self.dest_mac = None

    def generate_mac(self):
        return ':'.join(f"{random.randint(0x00, 0xFF):02x}" for _ in range(6))

    def send(self, data, dest_mac):
        self.dest_mac = dest_mac
        frame = f"{self.src_mac}->{self.dest_mac}|{data}"
        print(f"[Data Link Layer] Sending Frame: {frame}")
        return frame

    def receive(self, frame):
        """extract data from the frame"""
        try:
            parts = frame.split('|', 1)
            if len(parts) < 2:
                print("[Data Link Layer] ERROR: Malformed frame received")
                return None

            mac_header, packet = parts
            src_mac, dest_mac = mac_header.split('->')

            print(f"[Data Link Layer] Received Frame from {src_mac} to {dest_mac}")
            return packet

        except Exception as e:
            print(f"[Data Link Layer] ERROR: {e}")
            return None

