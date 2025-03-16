import random
import uuid

class DataLinkLayer:
    def __init__(self):
        self.src_mac = self.get_mac_address()
        self.dest_mac = None

    def get_mac_address(self):
        """Get the actual MAC address of the machine."""
        mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
        return ":".join(mac[i : i + 2] for i in range(0, 12, 2))

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

