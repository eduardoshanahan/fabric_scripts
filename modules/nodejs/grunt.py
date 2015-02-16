from fabric.api import run
from fabric.api import task


@task
def install():
    """
    Grunt client form npm
    """
    run('npm install -g grunt-cli')