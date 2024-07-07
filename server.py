class Server:
    def __init__(self, config):
        self.config = config

    def run(self):
        if self.config.get('run_localhost'):
            print("Server running on localhost")
        else:
            print("Server running remotely")