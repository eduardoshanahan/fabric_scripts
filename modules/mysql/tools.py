from fabric.api import task
from fabric.api import sudo

@task
def install():
    """
    Get some tools
    """
    sudo('apt-get install -y mysql-client-core-5.6')