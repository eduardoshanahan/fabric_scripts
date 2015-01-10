from fabric.api import run
from fabric.api import task


@task
def install():
    """
    StriderCD stable from npm
    """
    run('npm install -g strider')
    run('strider addUser -l contact@eduardoshanahan.com -p supersecret -a')


@task
def full():
    """
    StriderCD with all required dependencies
    """
    from .. import development
    from .. import git
    from .. import mongo
    from .. import nodejs
    development.development.gplusplus.install()
    git.git.install()
    nodejs.nodejs.install()
    mongo.mongo.install()
    install()