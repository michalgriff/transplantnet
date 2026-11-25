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

    def exposed_register_organ(self, organ_type, blood_type, donor_id, harvest_center):
        with lock:
            organ = {
                "organ_type": organ_type,
                "blood_type": blood_type,
                "donor_id": donor_id,
                "harvest_center": harvest_center,
                "status": "available"
            }
            organs.append(organ)
            return f"Organ registered: {organ_type} ({blood_type}) from Donor {donor_id} - {harvest_center}. Total organs available: {len(organs)}"
if __name__ == "__main__":
    server = ThreadedServer(
        TransplantService,
        port=8000
    )

    print("TransplantNet server running...")
    server.start()
