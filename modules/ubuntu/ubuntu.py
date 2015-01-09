from fabric.api import run
from fabric.api import sudo
from fabric.api import task
from fabric.api import env
from library.host import type
from library.packages import cleanup
from library.packages import update


def init(env_details):
    env = env_details
