from fabric.api import sudo
from fabric.api import task


@task
def install():
    """
    ZMQ 
    """
    # sudo('add-apt-repository ppa:chris-lea/zeromq -y')
    # sudo('add-apt-repository ppa:chris-lea/libpgm -y')
    # sudo('apt-get update')
    sudo('apt-get install libzmq3-dev -y') 
    sudo('npm install -g zmq')



