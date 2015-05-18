from fabric.api import sudo
from fabric.api import task


@task
def install():
    """
    Dtrace provider
    """
    sudo('npm install -g dtrace-provider')
