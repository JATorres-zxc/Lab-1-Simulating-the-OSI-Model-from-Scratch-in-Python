class ApplicationLayer:
    def send(self, data):
        request = f"GET / HTTP/1.1\nHost: example.com\n\n{data}"
        print(f"[Application Layer] Sending Request:\n{request}")
        return request

    def receive(self, request):
        response = "HTTP/1.1 200 OK\nContent-Type: text/plain\n\nHello from Server"
        print(f"[Application Layer] Received Response:\n{response}")
        return response
