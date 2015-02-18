from fabric.api import sudo
from fabric.api import task
from fabric.api import env
import host
import hosts
import packages


def init(env_details):
    env = env_details

@task
def reboot():
    """
    Reboot Ubuntu
    """
    sudo('reboot')
