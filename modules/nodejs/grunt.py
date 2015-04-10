from fabric.api import sudo
from fabric.api import task


@task
def install():
    """
    Grunt client form npm
    """
    sudo('npm install -g grunt-cli')