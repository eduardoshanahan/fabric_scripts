from fabric.api import task
from fabric.api import sudo

@task
def install():
    """
    Get some tools
    """
    sudo('npm install -g bunyan')
    sudo('npm install -g nodemon')