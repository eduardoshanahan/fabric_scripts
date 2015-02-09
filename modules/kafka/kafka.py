from fabric.api import cd
from fabric.api import env
from fabric.api import put
from fabric.api import run
from fabric.api import sudo
from fabric.api import task
from fabric.api import local


env.kafka_version = '0.8.2-beta'
env.kafka_path = '/usr/lib/kafka'
env.kafka_config_path = '/etc/kafka'
env.kafka_scala_version = '2.11'
env.kafka_local_configuration_directory = 'configuration/kafka'


@task
def install():
    """
    Kafka from binaries
    """
    ensure_fresh_directory(env.kafka_path)
    sudo('chmod a+rw {0}'.format(env.kafka_path))
    run('wget http://www.whoishostingthis.com/mirrors/apache/kafka/{0}/kafka_{1}-{0}.tgz'.format(env.kafka_version, env.kafka_scala_version))
    sudo('tar zxvf kafka_{0}-{1}.tgz -C {2}'.format(env.kafka_scala_version, env.kafka_version, env.kafka_path))
    run('rm ~/kafka_{0}-{1}.tgz'.format(env.kafka_scala_version,env.kafka_version))
    sudo('mv {0}/kafka_{1}-{2}/* {0}'.format(env.kafka_path, env.kafka_scala_version, env.kafka_version))
    sudo('rm -rf {0}/kafka_{1}-{2}'.format(env.kafka_path, env.kafka_scala_version, env.kafka_version))


def ensure_fresh_directory(path):
    """
    Remove a directory and create it again
    """
    sudo('rm -rf {0}'.format(path))
    sudo('mkdir {0}'.format(path))


@task
def configure(configuration=env.kafka_local_configuration_directory):
    """
    Add upstart jobs for zookeeper and kafka (you can add :configuration='configuration files directory')
    """
    configure_properties(configuration, 'zookeeper')
    pass_configuration(configuration, 'kafka_zookeeper')
    configure_properties(configuration, 'server')
    pass_configuration(configuration, 'kafka')


def pass_configuration(configuration_path, application_name):
    """
    Put the upstart file in place
    """
    sudo('initctl stop {0}'.format(application_name), warn_only=True)
    put('{0}/etc/init/{1}.conf'.format(configuration_path, application_name), '/etc/init/{0}.conf'.format(application_name), use_sudo=True)
    sudo('initctl start {0}'.format(application_name))


def configure_properties(configuration_path, application_name):
    """
    Put the Java properties file in place
    """
    sudo('mkdir -p {0}'.format(env.kafka_config_path))
    local_path = '{0}/etc/kafka/{1}.properties'.format(configuration_path, application_name)
    remote_path = '/etc/kafka/{0}.properties'.format(application_name)
    put(local_path, remote_path, use_sudo=True)


@task
def full(configuration=env.kafka_local_configuration_directory):
    """
    Install with requirements and configure (you can add :configuration='configuration files directory')
    """
    from .. import java
    java.java.oracle.jdk.install()
    install()
    configure(configuration)


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
