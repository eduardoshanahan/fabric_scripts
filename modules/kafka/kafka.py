from fabric.api import cd
from fabric.api import env
from fabric.api import run
from fabric.api import sudo
from fabric.api import task

env.kafka_version = '0.8.2-beta'
env.kafka_path = '/opt/kafka'
env.kafka_scala_version = '2.11'


@task
def install():
    """
    Kafka from binaries
    """
    sudo('rm -rf {0}'.format(env.kafka_path))
    sudo('mkdir -p {0}'.format(env.kafka_path))
    sudo('chmod a+rw {0}'.format(env.kafka_path))
    run('wget http://www.whoishostingthis.com/mirrors/apache/kafka/{0}/kafka_{1}-{0}.tgz'.format(env.kafka_version, env.kafka_scala_version))
    sudo('tar zxvf kafka_{0}-{1}.tgz -C {2}'.format(env.kafka_scala_version, env.kafka_version, env.kafka_path))
    run('rm ~/kafka_{0}-{1}.tgz'.format(env.kafka_scala_version,env.kafka_version))
    sudo('mv {0}/kafka_{1}-{2}/* {0}'.format(env.kafka_path, env.kafka_scala_version, env.kafka_version))
    sudo('rm -rf {0}/kafka_{1}_{2}'.format(env.kafka_path, env.kafka_scala_version, env.kafka_version))


@task
def full():
    """
    Get all the requirements first
    """
    from ..import development
    development.development.dtach.install()
    from .. import java
    java.java.oracle.jdk.install()
    install()


@task
def start():
    """
    Start zookeeper and kafka
    """
    from .. import development
    with cd(env.kafka_path):
        development.development.dtach.runbg('nohup bin/zookeeper-server-start.sh config/zookeeper.properties')
        development.development.dtach.runbg('nohup bin/kafka-server-start.sh config/server.properties')


@task
def test():
    """
    Test kafka
    """
    with cd(env.kafka_path):
        run('bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test')
        run('bin/kafka-topics.sh --list --zookeeper localhost:2181')
        # run('bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test < echo "this is a test message"')
        # run('bin/kafka-console-consumer.sh --zookeeper localhost:2181 --topic test --from-beginning')
