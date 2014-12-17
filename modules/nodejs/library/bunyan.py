from fabric.api import task
from fabric.api import sudo

@task
def install():
    """
    Bunyan logging
    """
    sudo('npm install -g bunyan')