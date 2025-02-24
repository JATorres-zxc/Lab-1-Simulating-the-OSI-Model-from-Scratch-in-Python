import hashlib
import random

class TransportLayer:
    def send(self, data):
        sequence_number = random.randint(1000, 9999)
        checksum = hashlib.md5(data.encode()).hexdigest()
        segment = f"{sequence_number}|{checksum}|{data}"
        print(f"[Transport Layer] Sending Segment: {segment}")
        return segment

    def receive(self, segment):
        seq_num, checksum, data = segment.split('|')
        if hashlib.md5(data.encode()).hexdigest() == checksum:
            print(f"[Transport Layer] Valid Segment: {seq_num}")
            return data
        else:
            print("[Transport Layer] Corrupt Segment!")
            return None
