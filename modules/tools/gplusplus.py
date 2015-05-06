from fabric.api import task
from fabric.api import sudo


@task
def install():
    """
    From package
    """
    sudo('apt-get install -y g++')


@task
def prerequisites():
    """
    Tools required
    """
    pass
    

@task
def full():
    """
    Everything required
    """
    install()