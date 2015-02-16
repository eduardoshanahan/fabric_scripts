from fabric.api import run
from fabric.api import task


@task
def install():
    """
    Yeoman
    """
    run('npm install -g yo')


@task
def generators():
    """
    Generators for Yeoman
    """
    run('npm install -g generator-angular')
