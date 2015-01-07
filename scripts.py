from fabric.api import task
from modules.apache import apache
from modules.development import development
from modules.docker import docker
from modules.ec2 import ec2
from modules.git import git
from modules.java import java
from modules.jenkins import jenkins
from modules.kafka import kafka
from modules.mongo import mongo
from modules.mysql import mysql
from modules.nginx import nginx
from modules.nodejs import nodejs
from modules.php import php
from modules.python import python
from modules.redis import redis
from modules.ruby import ruby
from modules.scala import scala
from modules.ubuntu import ubuntu
from modules.vagrant import vagrant
from modules.zeromq import zeromq

@task
def call_vagrant():
    """
    Contact a Vagrant instance
    """
    env_details = vagrant.set_env()
    ubuntu.init(env_details)
