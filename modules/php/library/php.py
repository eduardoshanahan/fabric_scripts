from fabric.api import sudo
from fabric.api import task


@task
def install():
    """
    PHP 5 from package
    """
    sudo ('apt-get install -y php5')