from fabric.api import task
from fabric.api import sudo
from fabric.api import run
from fabric.api import env
from library import sbt


env.scala_version = '2.11.4'

@task
def install():
    """
    Install from binaries
    """
    sudo('apt-get remove -y scala-library scala')
    run('wget http://www.scala-lang.org/files/archive/scala-{0}.deb'.format(env.scala_version))
    sudo('dpkg -i scala-{0}.deb'.format(env.scala_version))
    sudo('apt-get update')
    sudo('apt-get install -y scala')
 

 # @task
 # def full_install():
 #    """
 #    Get the requirements and install
 #    """
    