from fabric.api import task
from fabric.api import sudo


@task
def install():
    """
    Apache bindings
    """
    sudo('apt-get install -y libapache2-mod-auth-mysql')
    sudo('apt-get install -y php5-mysql')