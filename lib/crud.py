from faker import Faker
import random
from init import session

from models import Ward
from models import Doctor
from models import Patient
from models import Nurse

fake= Faker()

if __name__ == '__main__':
    
    session.query(Doctor).delete()
    session.query(Patient).delete()
    session.query(Ward).delete()
    session.query(Nurse).delete()
    session.commit()
    
    
    specialities=["Pediatrician","Oncologist","Dermatologist","Gynecologist", "General surgeon"]
    doctors=[]
    genders=["Male", "Female"]

    for i in range(10):
        gender = random.choice(genders)
        if gender == "Male":
            first_name = fake.first_name_male()
        else:
            first_name = fake.first_name_female()

        doctor= Doctor(
            first_name= first_name,
            last_name= fake.last_name(),
            speciality= random.choice(specialities)   
        )
        doctors.append(doctor)   
    session.add_all(doctors)
    session.commit()
    
    
    ward_names = ["Pediatrics_1", "Pediatrics_2", "Oncology_1", "Oncology_2","General", "ICU", "HDU_1", "HDU_2", "Renal Unit"]
    ward_locations = ["Health Complex,3rd Floor", "Mandela Complex,2nd Floor","Centum-Core,ground floor","Mwai Kibaki Wing, 1st Floor"]
    chosen_names = random.sample(ward_names, len(ward_names))

    wards = []
    for name in chosen_names:
        ward = Ward(
           ward_name=name,
           ward_capacity=random.randint(5, 10),
           ward_location=random.choice(ward_locations)
        )
        wards.append(ward)
    session.add_all(wards)
    session.commit()

    
    
    nurses=[]
    for i in range(15):
        gender = random.choice(genders)
        if gender == "Male":
            first_name = fake.first_name_male()
        else:
            first_name = fake.first_name_female()

        nurse= Nurse(
            first_name= first_name,
            last_name= fake.last_name(),
            gender= gender       
        )
        nurses.append(nurse)
    session.add_all(nurses)
    session.commit()
    
    
    patients=[]
    for i in range(30):
        random_ward=random.choice(wards)
        random_doctor= random.choice(doctors)
        random_nurse= random.choice(nurses)

        gender = random.choice(genders)
        if gender == "Male":
            full_name = f"{fake.first_name_male()} {fake.last_name()}"
        else:
            full_name = f"{fake.first_name_female()} {fake.last_name()}"

        patient= Patient(
            full_name= full_name,
            gender= gender,
            age= random.randint(13, 70),
            reported_condition= fake.sentence(),
            doctor_prescription= fake.sentence(),
            ward_id= random_ward.id,
            bed_number= random.randint(1, random_ward.ward_capacity),
            doctor_id= random_doctor.id,
            nurse_id= random_nurse.id,
            admission_date = fake.date_between(start_date="-1y", end_date="today")
        )
        patients.append(patient)
        
    session.add_all(patients)
    session.commit()
    session.close()
