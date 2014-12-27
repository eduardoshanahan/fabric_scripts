from fabric.api import task
from fabric.api import sudo
from fabric.api import run


@task
def install():
    """
    From RVM manager
    """
    sudo('gpg --keyserver hkp://keys.gnupg.net --recv-keys D39DC0E3')
    sudo('\curl -sSL https://get.rvm.io | bash -s stable --ruby')
