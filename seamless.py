import click


@click.group()
def cli():
    pass


@cli.command()
def run():
    click.echo('Running your code seamlessly')


@cli.command()
@click.option('--schedule', default=1, help='cron expression that identifies the schedule your code runs on')
def publish(schedule):
    if schedule:
        click.echo('Publishing your code...')
    else:
        click.echo('Publishing your code to run on schedule {schedule}...'.format(schedule=schedule))
    click.echo("Success!")


@cli.command()
def init():
    click.echo('Initializing an example seamless project')
