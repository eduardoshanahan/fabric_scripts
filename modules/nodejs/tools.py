from fabric.api import task
from fabric.api import sudo
from fabric.api import run

@task
def install():
    """
    Get some tools
    """
    run('npm install -g bunyan')
    run('npm install -g nodemon')