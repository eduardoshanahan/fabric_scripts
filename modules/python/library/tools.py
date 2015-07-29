from fabric.api import run
from fabric.api import task


@task
def install():
    """
    Install all the tools available
    """
    pip.install()
    docopt.install()
    pyzmq.install()
    python_dev.install()
    redis.install()
    watchdog.install()
    profilehooks.install()
