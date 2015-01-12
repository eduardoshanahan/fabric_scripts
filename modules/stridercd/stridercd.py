from fabric.api import run
from fabric.api import task
from fabric.api import sudo


@task
def install():
    """
    StriderCD stable from npm
    """
    # sudo('useradd -s /bin/bash -m -d /home/strider -c "strider" strider')
    # sudo('usermod -aG sudo strider')
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
    nodejs.nodejs.bower.install()
    mongo.mongo.install()
    install()