from fabric.api import task
from fabric.api import sudo


@task
def install():
    """
    Apache from package
    """
    sudo ('apt-get install -y apache2')