from lib.init import session
from models import Doctor, Patient, Nurse, Ward

def admit_patient(session, full_name,gender,age,reported_condition,doctor_prescription,ward_id,bed_number,doctor_id,nurse_id):
    """Create a patient record,assign them to a ward and update the count."""
    chosen_ward= session.query(Ward).filter_by(id=ward_id).first()
    if chosen_ward.patient_count>= chosen_ward.ward_capacity:
        raise ValueError(f"{chosen_ward.ward_name} ward is full")
    new_patient = Patient(
        full_name=full_name,
        gender=gender,
        age=age,
        reported_condition=reported_condition,
        doctor_prescription=doctor_prescription,
        ward_id=ward_id,
        bed_number=bed_number,
        doctor_id=doctor_id,
        nurse_id=nurse_id
    )
    chosen_ward.patient_count +=1
    session.add_all([new_patient, chosen_ward])
    session.commit()

def discharge_patient(session, patient):
    """Remove a patient and update the ward count."""
    ward= patient.ward
    ward.patient_count -=1
    session.delete(patient)
    session.commit()


