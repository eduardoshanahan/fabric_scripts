from fabric.api import task
from fabric.api import sudo


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
    from .. import git
    from .. import mongo
    from .. import nodejs
    git.git.install()
    nodejs.nodejs.install()
    mongo.mongo.install()
    install()