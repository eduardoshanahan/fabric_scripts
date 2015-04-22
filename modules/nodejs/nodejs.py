from fabric.api import task
from fabric.api import run
from fabric.api import sudo
import bower
import bunyan
import forever
import grunt
import less
import nodemon
import yeoman


@task
def install():
    """
    NodeJS from external package
    """
    # run('echo prefix = ~/.node >> ~/.npmrc')
    # run('echo export PATH="$PATH:$HOME/.node/bin" >> ~/.bashrc')
    sudo('curl -sL https://deb.nodesource.com/setup_0.12 | bash -')
    sudo('apt-get update')
    sudo('apt-get install -y nodejs')
    run('mkdir -p .node')
    run('mkdir -p .npm')
    run('mkdir -p .config')


@task
def prerequisites():
    """
    Get what you need to install and run
    """
    from .. import tools
    tools.build_essential.install()


@task
def full():
    """
    Install NodeJS and tools
    """
    prerequisites()
    install()
    tools.full()
