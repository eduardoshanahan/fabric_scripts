from fabric.api import task
from fabric.api import sudo


@task
def install():
    """
    Pip from package
    """
    sudo('apt-get install -y python-pip')
    sudo('apt-get install -y python-dev')
    sudo('apt-get install -y build-essential')
    sudo('pip install --upgrade pip')