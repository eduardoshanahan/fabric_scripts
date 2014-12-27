from fabric.api import task
from fabric.api import sudo


@task
def install_development_tools():
    """
    Compilers
    """
    sudo('apt-get install dtach')