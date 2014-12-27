from fabric.api import task
from fabric.api import sudo


@task
def install():
    """
    Package from its own repository
    """
    sudo('wget -q -O - http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key | sudo apt-key add -')
    sudo("sh -c 'echo deb http://pkg.jenkins-ci.org/debian binary/ > /etc/apt/sources.list.d/jenkins.list'")
    sudo('apt-get update')
    sudo('apt-get install -y jenkins')
