from fabric.api import task
from fabric.api import sudo
from fabric.api import run


@task
def install():
    """
    Install from package
    """
    sudo ('apt-get install python-dev')
