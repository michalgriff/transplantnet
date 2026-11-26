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
        if not all(isinstance(value, str) for value in (
            organ_type, blood_type, donor_id, harvest_center
        )):
            return "Error: All registration fields must be text. "
        
        organ_type = organ_type.strip().lower()
        blood_type = blood_type.strip().upper()
        donor_id = donor_id.strip()
        harvest_center = harvest_center.strip()

        if not harvest_center: 
            return "Error: Enter harvest center name. "
        if not donor_id:
            return "Error: Enter a donor ID. "
        if organ_type not in {"kidney", "liver", "heart", "lung"}: 
            return "Error: Organ type not valid. "
        if blood_type not in {"O", "A", "B", "AB"}:
            return "Error: Blood type must be O, A, B, or AB. "

        with lock:

            for organ in organs:
                if (
                    organ["donor_id"] == donor_id
                    and organ["organ_type"] == organ_type
                ):
                    return "Error: Organ already registered."

            organ = {
                "organ_type": organ_type,
                "blood_type": blood_type,
                "donor_id": donor_id,
                "harvest_center": harvest_center,
                "status": "available"
            }

            organs.append(organ)

            available = sum(
                o["status"] == "available" for o in organs
            )


            return (
                f"Organ registered: {organ_type} ({blood_type}) "
                f"from Donor {donor_id} - {harvest_center}. "
                f"Total organs available: {available}"
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
            
            waiting = sum(
                p["status"] == "waiting" for p in patients
            )

            return (
                f"Patient registered: {patient_id} needs {organ_needed} "
                f"({blood_type}), urgency level {urgency}, "
                f"from {hospital_name}. "
                f"Total patients waiting: {waiting}"
            )


if __name__ == "__main__":
    server = ThreadedServer(
        TransplantService,
        port=8000
    )

    print("TransplantNet server running...")
    server.start()