from fabric.api import env
from fabric.api import local
from fabric.api import task


def set_env(hosted):
    """
    Connect to Vagrant from the host machine
    """
    env.user = 'vagrant'
    config_details = local('vagrant ssh-config', capture=True).splitlines()
    hosting = [line for line in config_details if 'Host ' in line or 'Port' in line]
    print('Hosts available are',hosting)
    result = dict((line.split() for line in config_details if line != ''))
    env.hosts = ['{0}:{1}'.format(result['HostName'], result['Port'])]
    env.key_filename = result['IdentityFile'].replace('"', '')
    if hosted != '':
        env.hosts = hosted
    print('Going to connect to host \n{0}\n'.format(env.hosts))
    return env


@task
def connect(hosted=''):
    """
    Apply Vagrant credentials to the SSH session (you can put :hosted=127.0.0.1:port_number)
    """
    from .. import ubuntu
    env_details = set_env(hosted)
    ubuntu.ubuntu.init(env_details)


@task
def list():
    """
    List existing machines
    """
    local('vagrant global-status')


@task
def cleanup():
    """
    Remove invalid machines
    """
    local('vagrant global-status --prune')
