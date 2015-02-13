from fabric.api import env
from fabric.api import local
from fabric.api import task


def get_pairs(line):
    result = line.split('\"')
    if len(result) == 1:
        result = line.split()
    result = [item.lstrip().rstrip() for item in result if item != '']
    print('the result is', result)
    return result


def set_env(hosted):
    """
    Connect to Vagrant from the host machine
    """
    env.user = 'vagrant'
    config_details = local('vagrant ssh-config', capture=True).splitlines()
    hosting = [line for line in config_details if 'Host ' in line or 'Port']
    print('Hosts available are',hosting)
    result = dict((get_pairs(line) for line in config_details if line != ''))
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
