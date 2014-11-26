from fabric.api import task
from fabric.api import sudo


@task
def install():
    """
    Mongo from package
    """
    sudo('apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10')
    sudo("echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | tee /etc/apt/sources.list.d/mongodb.list")
    sudo('apt-get update')
    sudo('apt-get install -y mongodb-10gen')