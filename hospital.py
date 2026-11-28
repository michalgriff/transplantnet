import rpyc

conn = rpyc.connect("localhost", 8000)

try:
    print(conn.root.ping())

    print("\n--- Patient Registration ---")

    patient_id = input("Enter patient ID: ")
    organ_needed = input("Enter organ needed: ")
    blood_type = input("Enter blood type: ")
    urgency = int(input("Enter urgency level (1-6): "))
    hospital_name = input("Enter hospital name: ")

    result = conn.root.register_patient(
        patient_id,
        organ_needed,
        blood_type,
        urgency,
        hospital_name
    )

    print("\n" + result)

finally:
    conn.close()