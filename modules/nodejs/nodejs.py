from fabric.api import task
from fabric.api import run
from fabric.api import sudo
from fabric.api import env
from library import bunyan
from library import nodemon
from library import tools


@task
def install():
    """
    NodeJS from external package
    """
    sudo('apt-get install -y python-software-properties')
    sudo('apt-get install -y software-properties-common')
    sudo('add-apt-repository -y ppa:chris-lea/node.js')
    sudo('apt-get update')
    sudo('apt-get install -y nodejs')
