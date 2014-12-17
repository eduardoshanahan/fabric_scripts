from fabric.api import task
from fabric.api import sudo


@task
def install():
    """
    Python binding for ZeroMQ
    """
    sudo('pip install pyzmq')