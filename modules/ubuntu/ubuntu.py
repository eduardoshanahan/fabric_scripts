from fabric.api import run
from fabric.api import sudo
from fabric.api import task
from fabric.api import env


def init(env_details):
    env = env_details


@task
def host_type():
    """
    Get the OS details
    """
    run('uname -a')


@task
def update():
    """
    Ubuntu full update
    """
    run('mkdir -p ~/tmp')
    sudo('apt-get clean')
    sudo('rm -rf /var/lib/apt/lists/*')
    sudo('apt-get clean')
    sudo('apt-get update')
    sudo('apt-get install python-software-properties -y ')
    sudo(('DEBIAN_FRONTEND=noninteractive apt-get -y '
          '-o Dpkg::Options::="--force-confdef" '
          '-o Dpkg::Options::="--force-confold" dist-upgrade'))
    run('rm -rf ~/tmp')


@task
def cleanup_packages():
    """
    Remove unused packages
    """
    sudo('apt-get autoclean -y')
    sudo('apt-get autoremove -y')