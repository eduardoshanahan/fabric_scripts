from fabric.api import task
from fabric.api import sudo


@task
def install():
    """
    VirtualBox from repository
    """
    sudo('apt-get install virtualbox-dkms')
