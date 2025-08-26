import click
from init import session
from models import Doctor, Patient, Nurse, Ward
from helper import admit_patient, discharge_patient
  
if __name__=='__main__':
    
    click.echo(click.style('Better Care Admissions_System:', fg="blue", bg='white', underline= True))
    click.secho("Choose a role: " , fg='yellow')
    click.secho("1.Admissions Officer", fg='cyan')
    click.secho("2.Doctor", fg='cyan')
    click.secho("3.Nurse",fg='cyan')
    click.secho("4.To exit")
    user_option= click.prompt('Enter option ')
    click.secho(f'You have entered option {user_option}', fg="green")
    if user_option== 1:
        click.secho("Hey, what would you like to do?", fg='yellow')
        while True:
            click.secho("1.Admit or remove a Patient", fg='cyan')
            click.secho("2.Add or remove a Doctor", fg="cyan")
            click.secho("3.Add or remove a Nurse", fg="cyan")
            click.secho("4.Add a new Ward", fg="cyan")
            