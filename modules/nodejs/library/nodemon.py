from fabric.api import task
from fabric.api import sudo

@task
def install():
    """
    Run node apps permanently
    """
    sudo('npm install -g nodemon')