from fabric.api import task
from fabric.api import sudo


@task
def install():
    """
    Compilers
    """
    sudo('apt-get install dtach')