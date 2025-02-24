import socket

class PhysicalLayer:
    def __init__(self):
        self.buffer = []

    def send(self, data):
        """convert data to bits and simulate transmission"""
        bit_stream = ''.join(format(ord(char), '08b') for char in data)
        self.buffer.append(bit_stream)
        print(f"[Physical Layer] Sending Bits: {bit_stream}")
        return bit_stream

    def receive(self, bit_stream):
        """convert bits back to characters"""
        data = ''.join(chr(int(bit_stream[i:i+8], 2)) for i in range(0, len(bit_stream), 8))
        print(f"[Physical Layer] Received Data: {data}")
        return data
