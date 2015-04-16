from fabric.api import task
from fabric.api import sudo


@task
def install():
    """
    Install from npm
    """
    sudo('npm install -g less')