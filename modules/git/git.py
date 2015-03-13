from fabric.api import task
from fabric.api import sudo


@task
def install():
    """
    Git from the ppa
    """
    sudo('add-apt-repository -y ppa:git-core/ppa')
    sudo('apt-get update')
    sudo('apt-get install -y git')
    sudo('git config --global url."https://".insteadOf git://')
