import click
from init import session
from models import Doctor, Patient, Nurse, Ward

if __name__=='__main__':
    
    click.echo(click.style('Better Care Admissions_System:', fg="blue", underline= True))
    click.secho("Choose a role: " , fg='yellow')
    click.secho("1.Admissions Officer")
    click.secho("2.Doctor")
    click.secho("3.Nurse")
    click.secho("4.To exit")
    user_option= click.prompt('Enter option ')
    click.secho(f'You have entered option {user_option}', fg="green")
    