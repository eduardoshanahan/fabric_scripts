from fabric.api import task
from fabric.api import sudo


@task
def install():
    """
    Fabric from pip
    """
    sudo('pip install fabric')


@task
def prerequisites():
    """
    Pip
    """
    import pip
    pip.install()

@task
def full_install():
    """
    Prerequisites and functionality
    """
    prerequisites()
    install()
