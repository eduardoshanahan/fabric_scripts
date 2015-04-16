from fabric.api import sudo
from fabric.api import task


@task
def install():
    """
    Bower from npm
    """
    sudo('npm install -g bower')
