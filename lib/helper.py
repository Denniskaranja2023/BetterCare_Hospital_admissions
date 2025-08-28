import click
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
def add_doctor(session,first_name, last_name, speciality, user_name, password):
    """Add a new doctor"""
    new_doctor= Doctor(
             first_name=first_name,
             last_name= last_name,
             speciality=speciality,
             user_name=user_name,
             password=password
             )
    session.add(new_doctor)
    session.commit()

def add_prescription(session, patient, prescription):
    """Doctor makes a prescription on evaluating condition"""
    patient.doctor_prescription = prescription
    session.commit()

#Nurse helper functions  
def add_nurse(session,first_name, last_name, gender, user_name, password):
    """Add a new nurse"""
    new_nurse= Nurse(
             first_name= first_name,
             last_name= last_name,
             gender= gender,
             user_name=user_name,
             password=password
             )
    session.add(new_nurse)
    session.commit()

def add_condition(session, patient, condition):
    """Add a new condition to a patient"""
    patient.reported_condition = condition
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


def prompt_with_exit(message, **kwargs):
    """Wrapper around click.prompt that breaks if user types 'exit'."""
    value = click.prompt(message, **kwargs)
    if isinstance(value, str) and value.strip().lower() == "exit":
        raise KeyboardInterrupt
    return value

def prompt_with_exit_int(message, **kwargs):
    """Wrapper around click.prompt that breaks if user enters 0."""
    value = click.prompt(message, **kwargs)
    if isinstance(value, int) and value == 0:
        raise KeyboardInterrupt
    return value

