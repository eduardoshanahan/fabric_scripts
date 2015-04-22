from fabric.api import sudo
from fabric.api import task


@task
def install():
    """
    Install from npm
    """
    sudo('npm install -g less')