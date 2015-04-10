from fabric.api import sudo
from fabric.api import task


@task
def install():
    """
    Bunyan logging
    """
    sudo('npm install -g bunyan')