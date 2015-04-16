from fabric.api import run
from fabric.api import task


@task
def install():
    """
    Run node apps permanently
    """
    sudo('npm install -g nodemon')