from fabric.api import task
import bower
import bunyan
import dtrace
import forever
import grunt
import less
import nodemon
import yeoman
import zmq


@task
def prerequisites():
    """
    Get the tools needed to install and run
    """
    from .. import git
    git.git.install()
    from .. import tools
    tools.build_essential.install()


@task
def full():
    """
    Install all the tools available
    """
    prerequisites()
    bower.install()
    bunyan.install()
    dtrace.install()
    forever.install()
    grunt.install()
    less.install()
    nodemon.install()
    yeoman.install()
