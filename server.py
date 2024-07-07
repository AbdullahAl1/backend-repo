import yaml
import os

class Server:
    def __init__(self):
        config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'config.yaml')
        with open(config_path, 'r') as file:
            self.config = yaml.safe_load(file)

    def run(self):
        if self.config.get('run_localhost'):
            print("Server running on localhost")
        else:
            print("Server running remotely")

if __name__ == "__main__":
    server = Server()
    server.run()
