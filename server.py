import rpyc
import threading
from rpyc.utils.server import ThreadedServer

organs = []
patients = []
matches = []
subscriptions = {}

lock = threading.Lock()

class TransplantService(rpyc.Service):

    def exposed_ping(self):
        return "Connected to TransplantNet"


if __name__ == "__main__":
    server = ThreadedServer(
        TransplantService,
        port=8000
    )

    print("TransplantNet server running...")
    server.start()