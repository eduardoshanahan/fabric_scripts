from fabric.api import sudo
from fabric.api import task


@task
def install():
    """
    Locust from pip package
    """
    sudo('pip install profilehooks')


@task
def full():
    """
    Full install with all the requirements
    """
    import pip
    pip.install()
    install()
