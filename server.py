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

            return (
                f"Organ registered: {organ_type} ({blood_type}) "
                f"from Donor {donor_id} - {harvest_center}. "
                f"Total organs available: {len(organs)}"
            )

    def exposed_register_patient(
        self,
        patient_id,
        organ_needed,
        blood_type,
        urgency,
        hospital_name
    ):
        with lock:
            patient = {
                "patient_id": patient_id,
                "organ_needed": organ_needed,
                "blood_type": blood_type,
                "urgency": urgency,
                "hospital_name": hospital_name,
                "status": "waiting"
            }

            patients.append(patient)

            return (
                f"Patient registered: {patient_id} needs {organ_needed} "
                f"({blood_type}), urgency level {urgency}, "
                f"from {hospital_name}. "
                f"Total patients waiting: {len(patients)}"
            )


if __name__ == "__main__":
    server = ThreadedServer(
        TransplantService,
        port=8000
    )

    print("TransplantNet server running...")
    server.start()