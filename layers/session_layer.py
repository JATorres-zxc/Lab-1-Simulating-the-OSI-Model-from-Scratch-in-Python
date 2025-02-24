class SessionLayer:
    def __init__(self):
        self.session_active = False

    def send(self, data):
        self.session_active = True
        print("[Session Layer] Session Started")
        return data

    def receive(self, data):
        print("[Session Layer] Session Ended")
        self.session_active = False
        return data
