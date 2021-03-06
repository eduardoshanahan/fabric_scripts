from fabric.contrib.files import append
from fabric.api import run
from fabric.api import sudo
from fabric.api import task


@task
def install():
    """
    Install Tomcat 7
    """
    # append('/etc/environment', 'JAVA_HOME="/usr/bin/java"', use_sudo=True)
    sudo('apt-get install -y tomcat7')

#
# @task
# def tools():
#     """
#     Tools
#     """
#     # sudo('apt-get install -y tomcat7-admin-webapps')
#     from .. import tools
#     tools.gcc.install()


@task
def full_install():
    """
    Server and tools
    """
    install()
    # tools()
