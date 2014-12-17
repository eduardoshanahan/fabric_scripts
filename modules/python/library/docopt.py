from fabric.api import task
from fabric.api import sudo


@task
def install():
    """
    Document the command line
    """
    sudo('pip install docopt')