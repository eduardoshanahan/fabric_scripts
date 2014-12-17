from fabric.api import run
from fabric.api import task


@task
def install():
    """
    Install all the tools available
    """
    bunyan.install()
    nodemon.install()