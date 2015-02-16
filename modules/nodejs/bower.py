from fabric.api import run
from fabric.api import task


@task
def install():
    """
    Bower from npm
    """
    run('npm install -g bower')
