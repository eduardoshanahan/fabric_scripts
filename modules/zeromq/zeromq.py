from fabric.api import task
from fabric.api import sudo
from fabric.api import run
from fabric.api import cd
from library import jzmq


@task
def install():
    """
    ZeroMQ from source
    """
    version = '3.2.4'  # 4.0.4 is bombing at build on jzmq
    url = 'http://download.zeromq.org/zeromq-{0}.tar.gz' \
        .format(version)
    sudo('apt-get install -y libtool')
    sudo('apt-get install -y uuid-dev')
    run('mkdir -p ~/tmp')
    run('wget -P ~/tmp {0}'.format(url))
    with cd('~/tmp'):
        run('tar xvzf zeromq-{0}.tar.gz'.format(version))
    with cd('~/tmp/zeromq-{0}'.format(version)):
        run('./autogen.sh')
        run('./configure')
        run('make')
        sudo('make install')
        sudo('ldconfig')
    run('rm -rf ~/tmp')
