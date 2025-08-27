import click
from lib.init import session
from models import Doctor, Patient, Nurse, Ward
from helper import admit_patient, discharge_patient
  
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
            click.secho("Hey, what would you like to do?", fg='yellow')
            click.secho("1.Admit or remove a Patient", fg='cyan')
            click.secho("2.Add or remove a Doctor", fg="cyan")
            click.secho("3.Add or remove a Nurse", fg="cyan")
            click.secho("4.Add a new Ward", fg="cyan")
            click.secho("5.return", fg="red")
            user_entry=click.prompt('Enter option ', type=int)
            if user_entry ==1:
                while True:
                    click.secho("Choose an option: ", fg='yellow')
                    click.secho("1.Admit a Patient", fg="cyan")
                    click.secho("2.Remove a Patient", fg="cyan")
                    click.secho("3 to return" , fg='red')
                    user_choice= click.prompt('Enter option ', type=int)
                    if user_choice== 1:
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
                        admit_patient(session, full_name,gender,age,reported_condition,doctor_prescription,ward_id,bed_number,doctor_id,nurse_id)
                        click.secho(f"{full_name} successfuly admitted!", fg="green")
                    if user_choice==2:
                        patient_fullname= click.prompt("Enter Full name of Patient you want to remove ")
                        selected_patient= session.query(Patient).filter_by(full_name= patient_fullname).first()
                        if selected_patient is None:
                            click.secho(f"Error: Patient with name '{patient_fullname}' not found.", fg='red')
                        else:
                            confirmation= click.confirm('Are you sure you want to remove this patient?')
                            if confirmation:
                                discharge_patient(session, selected_patient)   
                                click.secho(f"{selected_patient.full_name} successfuly removed!", fg="green") 
                            else:
                                break
                    if user_choice == 3:
                        break
                        
                    
        # full_name=full_name,
        # gender=gender,
        # age=age,
        # reported_condition=reported_condition,
        # doctor_prescription=doctor_prescription,
        # ward_id=ward_id,
        # bed_number=bed_number,
        # doctor_id=doctor_id,
        # nurse_id=nurse_id