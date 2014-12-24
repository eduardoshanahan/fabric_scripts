from fabric.api import task
from fabric.api import sudo


@task
def install():
    """
    Pep from pip
    """
    sudo('pip install pep8')
