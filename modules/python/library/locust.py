from fabric.api import sudo
from fabric.api import task


@task
def install():
    """
    Locust from pip package
    """
    sudo('pip install locustio')


@task
def full():
    """
    Full install with all the requirements
    """
    import pip
    pip.install()
    import pyzmq
    pyzmq.install()
    install()

