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
    run('npm install -g strider@1.5.0')
    # run('node strider addUser -l contact@eduardoshanahan.com -p supersecret -a')


@task
def full():
    """
    StriderCD with all required dependencies
    """
    from .. import development
    from .. import git
    from .. import mongo
    from .. import nodejs
    development.development.build_essential.install()
    development.development.make.install()
    development.development.gplusplus.install()
    mongo.mongo.install()
    git.git.install()
    nodejs.nodejs.install()
    # nodejs.nodejs.bower.install()
    # nodejs.nodejs.mkdirp.install()
    # nodejs.nodejs.less.install()
    install()