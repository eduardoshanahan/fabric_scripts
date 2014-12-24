from fabric.api import task
from fabric.api import sudo


@task
def install():
    """
    Grunt client form npm
    """
    sudo('npm install -g grunt-cli')