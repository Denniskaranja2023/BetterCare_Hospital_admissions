from init import session
from models import Doctor, Patient, Nurse, Ward

#Patient helper functions
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

#Doctor helper functions  
def add_doctor(session,first_name, last_name, speciality):
    """Add a new doctor"""
    new_doctor= Doctor(
             first_name=first_name,
             last_name= last_name,
             speciality=speciality       
             )
    session.add(new_doctor)
    session.commit()


#Nurse helper functions  
def add_nurse(session,first_name, last_name, gender):
    """Add a new nurse"""
    new_nurse= Nurse(
             first_name= first_name,
             last_name= last_name,
             gender= gender      
             )
    session.add(new_nurse)
    session.commit()


#Ward helper function 
def add_ward(session,ward_name, ward_capacity, ward_location, patient_count):
    """Add a new ward"""
    new_ward= Ward(
             ward_name= ward_name,
             ward_capacity= ward_capacity,
             ward_location= ward_location,
             patient_count= patient_count     
             )
    session.add(new_ward)
    session.commit()


#delete function
def delete_record(session, ward):
    """Remove a record"""
    session.delete(ward)
    session.commit()
    

