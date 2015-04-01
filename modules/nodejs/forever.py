from fabric.api import run
from fabric.api import task


@task
def install():
    """
    Bunyan logging
    """
    run('npm install -g forever')