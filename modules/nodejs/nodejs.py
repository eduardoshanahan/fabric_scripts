from fabric.api import task
from fabric.api import run
from fabric.api import sudo
import bower
import bunyan
import grunt
import less
import nodemon
import tools
import yeoman


@task
def install():
    """
    NodeJS from external package
    """
    run('echo prefix = ~/.node >> ~/.npmrc')
    run('echo export PATH="$PATH:$HOME/.node/bin" >> ~/.bashrc')
    sudo('curl -sL https://deb.nodesource.com/setup_0.12 | bash -')
    sudo('apt-get update')
    sudo('apt-get install -y nodejs')
    run('mkdir -p .node')


@task
def prerequisites():
    """
    All the tools required to install and run
    """
    from .. import tools
    tools.build_essential.install()
    from .. import git
    git.git.install()

@task
def full():
    """
    Install NodeJS and tools
    """
    install()
    tools.full()
