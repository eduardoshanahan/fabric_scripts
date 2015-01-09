from fabric.api import env
from fabric.api import local
from fabric.api import task



def set_env():
    """
    Connect to Vagrant from the host machine
    """
    env.user = 'vagrant'
    result = dict(line.split() for line in local(
        'vagrant ssh-config', capture=True).splitlines())
    env.hosts = ['{0}:{1}'.format(result['HostName'], result['Port'])]
    env.key_filename = result['IdentityFile'].replace('"', '')
    return env


@task
def connect():
    from .. import ubuntu
    env_details = set_env()
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


@task
def destroy(id):
    """
    Remove a machine -> :a3d345f or :id=a3d345f
    """
    local('vagrant destroy {0}'.format(id))
