from fabric.api import task
from fabric.api import run
from fabric.api import sudo
import bower
import bunyan
import forever
import grunt
import less
import nodemon
import pm2
import tools
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
    ensure_directory_access()
    # run('mkdir -p .node')
    # run('mkdir -p .npm')
    # run('mkdir -p .config')


@task
def ensure_directory_access():
    """
    Make sure that all directories needed are accessible
    """
    sudo('mkdir -p ~/.npm')
    sudo('chmod -R a+rw ~/.npm')

@task
def prerequisites():
    """
    Get what you need to install and run
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
    prerequisites()
    install()


@task
def full_and_tools():
    """
    Node and the usual tools
    """
    full()
    tools.full()
