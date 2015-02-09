from fabric.api import run
from fabric.api import sudo
from fabric.api import task



@task
def install():
    """
    Leiningen install from package
    """
    sudo('sudo apt-get install -y leiningen')
    run('lein')
