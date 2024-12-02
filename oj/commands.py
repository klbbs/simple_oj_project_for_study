import click

from oj import oj, db
from oj.models import Problem

@oj.cli.command()
@click.option('--drop',is_flag=True,help='Create after drop')
def initdb(drop):
    """initialize the database"""
    if drop:
        click.confirm('delete the database, continue?', abort=true)
        db.drop_all()
        click.echo('drop done')
    db.create_all()
    click.echo('initialize done')

@oj.cli.command()
@click.option('--count',default=20,help='generate fake problems, default 20 conut')
def forge(count):
    """generate fake problems"""
    from faker import Faker
    db.drop_all()
    db.create_all()
    fake = Faker()
    for i in range(count):
        problem = Problem(
            title = fake.sentence(nb_words=20),
            description = fake.text(max_nb_chars=100),
            difficulty = fake.random_digit_not_null(),
            category = fake.sentence(nb_words=10),
            input_sample = fake.text(max_nb_chars=30),
            output_sample = fake.text(max_nb_chars=30),
        )
        db.session.add(problem)
    db.session.commit()
    click.echo('random done')