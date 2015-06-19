from fabric.api import sudo
from fabric.api import task


@task
def install():
    """
    Process Manager 2
    """
    sudo('npm install -g pm2')