from fabric.api import task
from fabric.api import sudo
from fabric.api import run
from fabric.api import cd


@task
def install():
    """
    Java bindings for ZeroMQ
    """
    url = 'https://github.com/zeromq/jzmq/archive/master.zip'
    sudo('apt-get install -y unzip')
    sudo('apt-get install -y pkg-config')
    run('mkdir -p ~/tmp')
    run('wget -P ~/tmp {0}'.format(url))
    with cd('~/tmp'):
        run('unzip master.zip')
    with cd('~/tmp/jzmq-master'):
        run('./autogen.sh')
        run('./configure')
        run('make')
        sudo('make install')
        sudo('ldconfig')
    run('rm -rf ~/tmp')
    sudo(('echo export LD_LIBRARY_PATH=/usr/local/lib'
          ' > /etc/profile.d/ldlibrarypath.sh'))


@task
def prerequisites():
    """
    Tools required
    """
    from . import zeromq
    zeromq.install()


@task
def full():
    """
    Everything installed
    """
    prerequisites()
    install()