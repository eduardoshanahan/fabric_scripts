from fabric.api import env
from fabric.api import task
from fabric.api import sudo


# I should move this to the configuration
env.default_password = "FabricScriptsDefaultPassword"

@task
def default(received_password=''):
    """
    Let the installer work without asking for root details
    """
    if received_password=='':
        received_password = env.default_password
    print('password used at mysql.password is {0}'.format(received_password))
    sudo('apt-get install debconf-utils')
    password = 'mysql-server mysql-server/root_password password {0}'.format(received_password)
    sudo("debconf-set-selections <<< '{0}'".format(password))
    password_again = 'mysql-server mysql-server/root_password_again password {0}'.format(received_password)
    sudo("debconf-set-selections <<< '{0}'".format(password_again))
