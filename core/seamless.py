import os
import tarfile

import click
import requests

from core.constants import ARCHIVE_FOR_SENDING_NAME, SEAMLESS_SERVICE_URL, ARCHIVE_SIZE_LIMIT, EXCLUDE_FOLDERS_AND_FILES


@click.group()
# This is just an entry point for the CLI, all other commands are registered in this group
def cli():
    pass


@cli.command()
def run():
    try:
        def filtr(file):
            for name in EXCLUDE_FOLDERS_AND_FILES:
                if file.name.startswith(f"./{name}"):
                    return None
            return file

        folder_to_archive = '.'
        tar = tarfile.open(ARCHIVE_FOR_SENDING_NAME, "w:gz")
        tar.add(folder_to_archive, filter=filtr)
        tar.close()
        # TODO we should have this limit only on server side and return meaningful error
        # TODO it should be doable with the production WSGI server and catching 413 error
        if os.stat(ARCHIVE_FOR_SENDING_NAME).st_size > ARCHIVE_SIZE_LIMIT:
            print(f"Your project is too big."
                  f" After we compressed the folder {folder_to_archive} the resulting file is more than 10 MB."
                  f"In order to have a really seamless experience we recommend to remove non-essential files."
                  f"If you need to increase the limit - please shoot us an email at hello@seamlesscloud.io")
            exit(1)

        resp = requests.post(SEAMLESS_SERVICE_URL,
                             headers={'Authorization': '12345678'},
                             files={'seamless_project': open(ARCHIVE_FOR_SENDING_NAME, 'rb')},
                             stream=True)
        resp.raise_for_status()
        for line in resp.iter_lines(decode_unicode=True, chunk_size=1):
            print(line)
    finally:
        try:
            os.remove(ARCHIVE_FOR_SENDING_NAME)
        except OSError:
            pass


@cli.command()
@click.option(
    "--schedule",
    help="cron expression that identifies the schedule your code runs on",
)
def publish(schedule):
    if not schedule:
        click.echo("Publishing your code...")
    else:
        click.echo(
            "Publishing your code to run on schedule {schedule}...".format(
                schedule=schedule
            )
        )
    click.echo("Success!")


@cli.command()
def init():
    click.echo("Initializing an example seamless project")
