from fabric.api import env
from fabric.api import run
from fabric.api import sudo
from fabric.api import task


env.sbt_version = '0.13.6'

@task
def install():
    """
    Install from binaries
    """
    sudo('apt-get purge sbt.')
    run('wget http://dl.bintray.com/sbt/debian/sbt-{0}.deb'.format(env.sbt_version))
    sudo('dpkg -i sbt-{0}.deb'.format(env.sbt_version))
    sudo('apt-get update')
    sudo('apt-get install -y sbt')