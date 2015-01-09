from fabric.api import task
from fabric.api import run


@task
def type():
    """
    Get details about the operating system
    """
    run('uname -a')
