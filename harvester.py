import rpyc

# Harvest Center Client 
# Registers an available organ with the central server

conn = rpyc.connect("localhost", 8000)

try:
    print(conn.root.ping())

    print("\n--- TransplantNet: Harvest Center ---")
    harvest_center = input("Harvest Center name: ")
    donor_id = input("Donor ID: ")
    organ_type = input("Organ type (kidney/liver/heart/lung): ").lower()
    blood_type = input("Donor blood type (O/A/B/AB): ").upper()

    result = conn.root.register_organ(organ_type, blood_type, donor_id, harvest_center)
    print(result)

finally:
    conn.close()
