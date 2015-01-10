from fabric.api import run
from fabric.api import task
import bower
import bunyan
import grunt
import nodemon
import yeoman


@task
def install():
    """
    Install all the tools available
    """
    bower.install()
    bunyan.install()
    grunt.install()
    nodemon.install()
    yeoman.install()
