from fabric.api import task
from fabric.api import run


@task
def install():
    """
    Install from npm
    """
    run('npm install -g mkdirp')
