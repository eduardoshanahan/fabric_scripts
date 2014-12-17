from fabric.api import run
from fabric.api import task
import bunyan
import nodemon


@task
def install():
    """
    Install all the tools available
    """
    bunyan.install()
    nodemon.install()