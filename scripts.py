from fabric.api import task
from modules.ubuntu import ubuntu
from modules.vagrant import vagrant
from modules.development import development
from modules.nginx import nginx
from modules.python import python
from modules.docker import docker
from modules.nodejs import nodejs
from modules.mongo import mongo
from modules.zeromq import zeromq
from modules.java import java
from modules.ec2 import ec2
from modules.mysql import mysql


@task
def call_vagrant():
    """
    Contact a Vagrant instance
    """
    env_details = vagrant.set_env()
    ubuntu.init(env_details)


