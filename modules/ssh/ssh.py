from fabric.api import task
from fabric.api import sudo


@task
def install():
    """
    OpenSSH server from repository
    """
    sudo('apt-get install openssh-server')


@task
def enable():
    """
    Enable ssh access
    """