import click
from init import session
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
                click.secho("Choose an option: ", fg='yellow')
                click.secho("1.Admit a Patient", fg="cyan")
                click.secho("2.Remove a Patient", fg="cyan")
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
                        click.secho(f"<{ward.ward_name} ward: id: {ward.id} capacity: {ward.ward_capacity}, current_occupants: {ward.patient_count}\n", fg='green>')
                    ward_id=click.prompt("Select a ward id to admit patient ", type=int)
                    
        # full_name=full_name,
        # gender=gender,
        # age=age,
        # reported_condition=reported_condition,
        # doctor_prescription=doctor_prescription,
        # ward_id=ward_id,
        # bed_number=bed_number,
        # doctor_id=doctor_id,
        # nurse_id=nurse_id