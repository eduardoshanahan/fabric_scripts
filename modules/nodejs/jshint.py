from fabric.api import sudo
from fabric.api import task


@task
def install():
    """
    JSHint
    """
    sudo('npm install -g jshint')