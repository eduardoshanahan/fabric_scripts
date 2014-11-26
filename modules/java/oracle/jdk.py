from fabric.api import task
from fabric.api import sudo


@task
def install():
    """
    Oracle JDK from package
    """
    sudo('apt-get install -y python-software-properties')
    sudo('add-apt-repository -y ppa:webupd8team/java')
    sudo('apt-get update')
    sudo(('echo debconf shared/accepted-oracle-license-v1-1 '
          'select true | sudo debconf-set-selections'))
    sudo(('echo debconf shared/accepted-oracle-license-v1-1 '
          'seen true | sudo debconf-set-selections'))
    sudo('apt-get install -y oracle-java8-installer')