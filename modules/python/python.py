from fabric.api import task
from fabric.api import run
from library import docopt
from library import pip
from library import python_dev
from library import pyzmq
from library import redis
from library import tools
from library import watchdog


@task
def install():
    """
    Python 2.7.* from package
    """
    sudo('apt-get install python')
