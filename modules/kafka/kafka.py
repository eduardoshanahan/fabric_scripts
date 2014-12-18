from fabric.api import task
from fabric.api import sudo
from fabric.api import run
from fabric.api import cd
from fabric.api import env


env.kafka_version = '0.8.0-beta1'

@task
def install():
    """
    Build from source
    """
    run('wget https://archive.apache.org/dist/kafka/kafka-{0}-src.tgz'.format(env.kafka_version))
    sudo('mkdir -p /usr/local/kafka')
    run('tar -zxvf kafka-{0}-src.tgz'.format(env.kafka_version))
    with cd('kafka-{0}-src'.format(env.kafka_version)):
        run('./sbt update')
        run('./sbt package')
        run('./sbt assembly-package-dependency')
    run('mv kafka-{0}-src /usr/local/kafka'.format(env.kafka_version))