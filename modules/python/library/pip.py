from fabric.api import task
from fabric.api import sudo


@task
def install():
    """
    Pip from package
    """
    sudo('apt-get install -y python-pip')
    sudo('apt-get install -y python-dev')
    sudo('apt-get install -y build-essential')
    sudo('pip install --upgrade pip')


@task
def upgrade():
    """
    Upgrade all packages installed with pip
    """
    import pip

    installed = run('pip.get_installed_distributions()')
    for dist in installed:
        sudo("pip install --upgrade {0}".format(dist.project_name))