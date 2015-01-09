from fabric.api import sudo
from fabric.api import task
from fabric.contrib.files import sed
from php import install as php_install


@task
def install():
    """
    Requirements for PHP in Apache
    """
    sudo('apt-get install -y libapache2-mod-php5')
    sudo('apt-get install -y php5-mcrypt')


@task
def configure():
    """
    Put php as the first option
    """
    sed('/etc/apache2/mods-enabled/dir.conf', 
        'DirectoryIndex index.html',
        'DirectoryIndex index.php index.html', 
        use_sudo=True)
    sudo('service apache2 restart')


@task
def full():
    """
    Get PHP configured in Apache
    """
    php_install()
    install()
    configure()