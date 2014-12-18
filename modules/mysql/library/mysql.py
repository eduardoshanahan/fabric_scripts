from fabric.api import task
from fabric.api import sudo


@task
def install():
    """
    Install from package
    """
    sudo('apt-get install -y mysql-server')