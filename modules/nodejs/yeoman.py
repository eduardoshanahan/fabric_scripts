from fabric.api import sudo
from fabric.api import task


@task
def install():
    """
    Yeoman
    """
    sudo('npm install -g yo')


@task
def generators():
    """
    Generators for Yeoman
    """
    sudo('npm install -g generator-angular')
