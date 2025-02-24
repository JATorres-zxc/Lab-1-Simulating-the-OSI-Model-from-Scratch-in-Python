import base64

class PresentationLayer:
    def send(self, data):
        encoded_data = base64.b64encode(data.encode()).decode()
        print(f"[Presentation Layer] Encoded Data: {encoded_data}")
        return encoded_data

    def receive(self, encoded_data):
        data = base64.b64decode(encoded_data).decode()
        print(f"[Presentation Layer] Decoded Data: {data}")
        return data
