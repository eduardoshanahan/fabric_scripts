from fabric.api import task
from fabric.api import run


@task
def install():
    """
    In memory data storage
    """
    sudo ('pip install redis')