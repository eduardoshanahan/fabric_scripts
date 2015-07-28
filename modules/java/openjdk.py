from fabric.api import task
from fabric.api import sudo


@task
def install():
    """
    Oracle JDK from package
    """
    # sudo('apt-get install -y python-software-properties')
    sudo('apt-get install -y openjdk-7-jre')
    sudo('apt-get install -y openjdk-7-jdk')
