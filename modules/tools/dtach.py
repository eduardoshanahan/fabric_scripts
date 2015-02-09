from fabric.api import run
from fabric.api import sudo
from fabric.api import task


@task
def install():
    """
    Compilers
    """
    sudo('apt-get install dtach')


def runbg(cmd, socket_name="dtach"):
    return run(
        'dtach -n `mktemp -u /tmp/{0}.XXXX` {1}'.format(socket_name, cmd))