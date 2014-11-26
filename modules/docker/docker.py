from fabric.api import task
from fabric.api import sudo



@task
def install():
    """
    Install Docker.io
    """
    sudo('apt-get install docker.io -y')
    sudo('ln -sf /usr/bin/docker.io /usr/local/bin/docker')
    sudo("sed -i '$acomplete -F _docker docker' /etc/bash_completion.d/docker.io")