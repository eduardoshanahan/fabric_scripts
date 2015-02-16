from fabric.api import run
from fabric.api import task
import bower
import bunyan
import grunt
import nodemon
import yeoman


@task
def full():
    """
    Install all the tools available
    """
    bower.install()
    bunyan.install()
    grunt.install()
    less.install()
    nodemon.install()
    yeoman.install()
