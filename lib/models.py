from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey, create_engine, CheckConstraint,func
from sqlalchemy.orm import relationship, validates
from init import engine , session, Base



#schema for patients table
class Patient(Base):
    __tablename__ = "patients"
    
    id= Column(Integer(), primary_key=True)
    full_name= Column(String())
    gender= Column(String())
    age=Column(Integer())
    reported_condition= Column(Text())
    doctor_prescription= Column(Text())
    ward_id=Column(Integer(), ForeignKey('wards.id'))
    bed_number= Column(Integer())
    doctor_id= Column(Integer(), ForeignKey('doctors.id'))
    nurse_id= Column(Integer(), ForeignKey('nurses.id'))
    admission_date = Column(Date(), server_default=func.current_date())
    
    @validates("ward_id")
    def validate_ward_capacity(self,key, ward_id):
        ward = session.query(Ward).get(ward_id)
        if ward and len(ward.patients) >= ward.ward_capacity:
            raise ValueError("Ward capacity exceeded")
        return ward_id
    
    def __repr__ (self):
        ward_name = self.ward.ward_name if hasattr(self, "ward") and self.ward else None
        return f"<Patient_name:{self.full_name}, ward_name:{ward_name}, bed_number:{self.bed_number}>"


#schema for the doctors table
class Doctor(Base):
    __tablename__ = 'doctors'
    
    id= Column(Integer(), primary_key=True)
    first_name= Column(String())
    last_name= Column(String())
    speciality= Column(String())
    patients= relationship('Patient', backref='doctor')
    
    def __repr__ (self):
        return f"<Doctor {self.id}: Name:{self.first_name} {self.last_name}, speciality:{self.speciality}>"


#schema for the wards table
class Ward(Base):
    __tablename__= 'wards'
    
    id= Column(Integer(), primary_key=True)
    ward_name= Column(String())
    ward_capacity= Column(Integer())
    ward_location= Column(String())
    patients= relationship('Patient', backref='ward')
    
    def __repr__(self):
        return f"<Ward {self.id}: name:{self.ward_name}, location:{self.ward_location}>"
    
    
#schema for the nurses table
class Nurse(Base):
    __tablename__ ='nurses'
    
    id= Column(Integer(), primary_key=True)
    first_name= Column(String())
    last_name=Column(String())
    gender=Column(String())
    patients=relationship('Patient', backref='nurse')
    
    def __repr__(self):
        return f"<Nurse {self.id}: name: {self.first_name} {self.last_name},gender: {self.gender}>"

Base.metadata.create_all(engine)