from fabric.api import task
from fabric.api import sudo


@task
def install():
    """
    Yeoman 
    """
    sudo('npm install -g yo')


@task
def generator_yeoman():
    """
    Generators for Yeoman
    """
    sudo('npm install -g generator-angular')