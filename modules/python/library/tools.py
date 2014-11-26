from fabric.api import task
from fabric.api import sudo


@task
def install():
    """
    Python 2.7 from package
    """
    sudo('pip install docopt')
    sudo('pip install pyzmq')
    sudo('pip install watchdog')