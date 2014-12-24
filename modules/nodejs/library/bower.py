from fabric.api import task
from fabric.api import sudo


@task
def install():
    """
    Bower from npm
    """
    sudo('npm install -g bower')
