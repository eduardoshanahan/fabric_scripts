from fabric.api import task
from fabric.api import sudo
from .. import mongo
from .. import nodejs


@task
def install():
    """
    StriderCD stable from npm
    """
    sudo('npm install -g strider')


@task
def full():
    """
    StriderCD with all required dependencies
    """
    nodejs.nodejs.install()
    mongo.install()
    install()