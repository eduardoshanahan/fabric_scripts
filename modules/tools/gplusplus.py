from fabric.api import task
from fabric.api import sudo


@task
def install():
    """
    From package
    """
    sudo('apt-get install -y g++')