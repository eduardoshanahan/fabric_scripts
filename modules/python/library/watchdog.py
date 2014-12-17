from fabric.api import task
from fabric.api import sudo


@task
def install():
    """
    Keep track of changes
    """
    sudo('pip install watchdog')