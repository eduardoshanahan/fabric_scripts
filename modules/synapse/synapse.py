from fabric.api import task
from fabric.api import sudo


@task
def install():
    """
    Synapse from ppa
    """
    sudo('apt-add-repository ppa:synapse-core/testing -y')
    sudo('apt-get update')
    sudo('apt-get install synapse')
