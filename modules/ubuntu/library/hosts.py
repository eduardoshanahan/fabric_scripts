from fabric.contrib.files import sed
from fabric.api import task


@task
def add(ip, name):
    """
    Add a new name at the end of the /etc/hosts file (you have to add :ip=10.0.0.1,name=server_name)
    """
    sed('/etc/hosts', '127.0.0.1 localhost', '127.0.0.1 localhost\n{0} {1}'.encode('string_escape').format(ip, name), use_sudo=True)
