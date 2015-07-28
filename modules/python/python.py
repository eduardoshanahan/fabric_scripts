from fabric.api import task
from fabric.api import run
from library import docopt
from library import locust
from library import pip
from library import python_dev
from library import python_fabric
from library import pyzmq
from library import redis
from library import tools
from library import watchdog
from library.root_path import root_path


@task
def install():
    """
    Python 2.7.* from package
    """
    sudo('apt-get install python')
