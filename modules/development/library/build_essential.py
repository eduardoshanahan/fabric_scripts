from fabric.api import sudo
from fabric.api import task

@task
def install():
    """
    Get some tools
    """
    sudo('apt-get install -y build-essential')