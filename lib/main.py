import click
from init import session
from models import Doctor, Patient, Nurse, Ward
from helper import admit_patient, discharge_patient, add_doctor, add_nurse, add_ward, delete_record
  
while True:
    click.echo(click.style('Better Care Admissions_System:', fg="blue", bg='white', underline= True))
    click.secho("Choose a role: " , fg='yellow')
    click.secho("1.Admissions Officer", fg='cyan')
    click.secho("2.Doctor", fg='cyan')
    click.secho("3.Nurse",fg='cyan')
    click.secho("4.To exit", fg="red")
    user_option= click.prompt('Enter option ', type=int)
    click.secho(f'You have entered option {user_option}', fg="green")
    if user_option== 1:
        while True:
            click.secho("Hi! Choose an action below", fg='yellow')
            click.secho("1.Admit or remove a Patient", fg='cyan')
            click.secho("2.Add or remove a Doctor", fg="cyan")
            click.secho("3.Add or remove a Nurse", fg="cyan")
            click.secho("4.Add or remove a Ward", fg="cyan")
            click.secho("5.return", fg="red")
            user_entry=click.prompt('Enter option ', type=int)
            if user_entry ==1:
                while True:
                    click.secho("Choose an option: ", fg='yellow')
                    click.secho("1.Admit a Patient", fg="cyan")
                    click.secho("2.Remove a Patient", fg="cyan")
                    click.secho("3 To return" , fg='red')
                    user_choice_1= click.prompt('Enter option ', type=int)
                    if user_choice_1== 1:
                        click.secho("Enter patient details: ", fg='yellow')
                        full_name=click.prompt("Enter patient's full_name e.g John Doe ")
                        gender=click.prompt("Male or Female ")
                        age=click.prompt("Enter patient's age ", type=int)
                        reported_condition=click.prompt("Enter patient's condition at admission: ")
                        doctor_prescription= click.prompt("Enter doctor's prescription at admission: ")
                        click.secho("Consider the following wards: ", fg="yellow")
                        wards=session.query(Ward).all()
                        for ward in wards:
                            click.secho(f"|{ward.ward_name} ward| id: {ward.id}| capacity: {ward.ward_capacity}| current_occupants: {ward.patient_count}|\n", fg='magenta')
                        ward_id=click.prompt("Select a ward id to admit patient ", type=int)
                        ward_selected=session.query(Ward).filter_by(id=ward_id).first()
                        click.secho("The following patients are in the ward: ", fg="yellow")
                        for patient in ward_selected.patients:
                            click.secho(patient, fg="magenta")
                        bed_number=click.prompt("Select a bed_number for patient ", type=int)
                        click.secho("Assign patient to one of the doctors below: ", fg="yellow")
                        doctors=session.query(Doctor).all()
                        for doctor in doctors:
                            click.secho(doctor, fg="magenta")
                        doctor_id =click.prompt("Assign doctor by selecting doctor_id ", type=int)
                        click.secho("Assign patient to one of the nurses below: ", fg="yellow")
                        nurses=session.query(Nurse).all()
                        for nurse in nurses:
                            click.secho(nurse, fg="magenta")
                        nurse_id =click.prompt("Assign nurse by selecting nurse_id ", type=int)
                        admit_patient(session, full_name.strip(),gender,age,reported_condition,doctor_prescription,ward_id,bed_number,doctor_id,nurse_id)
                        click.secho(f"{full_name} successfuly admitted!", fg="green")
                    if user_choice_1==2:
                        patient_fullname= click.prompt("Enter Full name of Patient you want to remove ")
                        selected_patient= session.query(Patient).filter_by(full_name= patient_fullname.strip()).first()
                        if selected_patient is None:
                            click.secho(f"Error: Patient with name '{patient_fullname}' not found.", fg='red')
                        else:
                            confirmation= click.confirm('Are you sure you want to remove this patient?')
                            if confirmation:
                                discharge_patient(session, selected_patient)   
                                click.secho(f"{selected_patient.full_name} successfuly removed!", fg="green") 
                            else:
                                break
                    if user_choice_1 == 3:
                        break
            if user_entry ==2:
                while True:
                    click.secho("Choose an option: ", fg='yellow')
                    click.secho("1.Add a Doctor", fg="cyan")
                    click.secho("2.Remove a Doctor", fg="cyan")
                    click.secho("3 To return" , fg='red')
                    user_choice_2= click.prompt('Enter option ', type=int)
                    if user_choice_2 == 1:
                        click.secho("Enter doctor's details: ", fg='yellow')
                        first_name=click.prompt('Enter first name ')
                        last_name= click.prompt("Enter last name" )
                        speciality= click.prompt("Enter doctor's speciality ")
                        add_doctor(session, first_name.strip(), last_name.strip(), speciality)
                        click.secho(f"{first_name}{last_name} successfully added as doctor", fg="green")
                    if user_choice_2 == 2:
                        doctor_firstName=click.prompt('Enter first name of doctor to be removed ' )
                        doctor_lastName=click.prompt('Enter last name of doctor ')
                        selected_doctor= session.query(Doctor).filter(Doctor.first_name==doctor_firstName.strip(), Doctor.last_name==doctor_lastName.strip()).first()
                        if selected_doctor is None:
                            click.secho(f"{doctor_firstName} {doctor_lastName} not found")
                        else:
                            confirmation= click.confirm('Are you sure you want to remove this doctor?')
                            if confirmation:
                                delete_record(session, selected_doctor)
                                click.secho(f"{selected_doctor.first_name} {selected_doctor.last_name} successfuly removed!", fg="green")
                            else:
                                break
                    if user_choice_2 == 3:
                        break
            if user_entry==3:
                while True:
                    click.secho("Choose an option: ", fg='yellow')
                    click.secho("1.Add a Nurse", fg="cyan")
                    click.secho("2.Remove a Nurse", fg="cyan")
                    click.secho("3 To return" , fg='red')
                    user_choice_3= click.prompt('Enter option ', type=int)
                    if user_choice_3 == 1:
                        click.secho("Enter nurse's details: ", fg='yellow')
                        first_name=click.prompt('Enter first name ')
                        last_name= click.prompt("Enter last name" )
                        gender= click.prompt("Enter nurse's gender ")
                        add_nurse(session, first_name.strip(), last_name.strip(), gender)
                        click.secho(f"{first_name} {last_name} successfully added as nurse", fg="green")
                    if user_choice_3 == 2:
                        nurse_firstName=click.prompt('Enter first name of nurse to be removed ' )
                        nurse_lastName=click.prompt('Enter last name of nurse ')
                        selected_nurse= session.query(Nurse).filter(Nurse.first_name==nurse_firstName.strip(), Nurse.last_name == nurse_lastName.strip()).first()
                        if selected_nurse is None:
                            click.secho(f"{nurse_firstName} {nurse_lastName} not found")
                        else:
                            confirmation= click.confirm('Are you sure you want to remove this nurse?')
                            if confirmation:
                                delete_record(session, selected_nurse)
                                click.secho(f"{selected_nurse.first_name} {selected_nurse.last_name} successfuly removed!", fg="green")
                            else:
                                break
                    if user_choice_3 == 3:
                        break       
            if user_entry==4:
                while True:
                    click.secho("Choose an option: ", fg='yellow')
                    click.secho("1.Add a Ward", fg="cyan")
                    click.secho("2.Remove a Ward", fg="cyan")
                    click.secho("3 To return" , fg='red')
                    user_choice_4= click.prompt('Enter option ', type=int)
                    if user_choice_4 == 1:
                        click.secho("Enter Ward details: ", fg='yellow')
                        ward_name=click.prompt('Enter ward name ')
                        ward_capacity= click.prompt("Enter ward full-capacity ", type=int )
                        ward_location= click.prompt("Enter ward location (Building,floor) ")
                        patient_count=0
                        add_ward(session, ward_name.strip(), ward_capacity, ward_location, patient_count)
                        click.secho(f"{ward_name} ward successfully added", fg="green")
                    if user_choice_4 == 2:
                        name_of_ward =click.prompt('Enter name of ward to be removed ' )
                        capacity_of_ward= click.prompt("Enter capacity of ward(5-10)", type=int)
                        selected_ward= session.query(Ward).filter(Ward.ward_name == name_of_ward.strip(), Ward.ward_capacity == capacity_of_ward).first()
                        if selected_ward is None:
                            click.secho(f"{name_of_ward} ward not found")
                        else:
                            confirmation= click.confirm('Are you sure you want to remove this ward?')
                            if confirmation:
                                delete_record(session, selected_ward)
                                click.secho(f"{selected_ward.ward_name} ward successfuly removed!", fg="green")
                    if user_choice_4 == 3:
                        break
            if user_entry ==5:
                break
            
                    
                         