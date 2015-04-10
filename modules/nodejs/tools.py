from fabric.api import task
import bower
import bunyan
import dtrace
import forever
import grunt
import less
import nodemon
import yeoman


@task
def full():
    """
    Install all the tools available
    """
    from .. import git
    git.git.install()
    bower.install()
    bunyan.install()
    dtrace.install()
    forever.install()
    grunt.install()
    less.install()
    nodemon.install()
    yeoman.install()
