from fabric.api import task
from fabric.api import sudo
from fabric.api import env
import tools


env.default_password = "MySuperPassword"

@task
def install():
    """
    mySQL from package
    """
    sudo('apt-get install -y mysql-server')


@task
def default_password():
    """
    Let the installer work without asking for root details
    """
    sudo('apt-get install debconf-utils')
    password = 'mysql-server mysql-server/root_password password {0}'.format(env.default_password)
    sudo("debconf-set-selections <<< '{0}'".format(password))
    password_again = 'mysql-server mysql-server/root_password_again password {0}'.format(env.default_password)
    sudo("debconf-set-selections <<< '{0}'".format(password_again))


@task
def install_default():
    """
    Install using the default credentials
    """
    default_password()
    install()