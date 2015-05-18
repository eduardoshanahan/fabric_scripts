from fabric.api import cd
from fabric.api import task
from fabric.api import run
from fabric.api import sudo
from fabric.contrib.files import sed


@task
def install():
    """
    Get Redis source and build
    """
    sudo('apt-add-repository ppa:synapse-core/testing')
    sudo('apt-get update')
    sudo('apt-get install synapse')
