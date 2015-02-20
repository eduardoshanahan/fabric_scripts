from fabric.api import run
from fabric.api import task


@task
def install():
    """
    Dtrace provider
    """
    run('npm install -g dtrace-provider')
