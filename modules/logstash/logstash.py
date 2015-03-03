from fabric.api import env
from fabric.api import put
from fabric.api import run
from fabric.api import sudo
from fabric.api import task


env.logstash_version_number = '1.4.2'
env.logstash_path = '/usr/lib/logstash'
env.logstash_config_path = '/etc/logstash'
env.logstash_local_configuration_directory = 'configuration/logstash'


@task
def install():
    """
    From binary
    """
    ensure_fresh_directory(env.logstash_path)
    sudo('chmod a+rw {0}'.format(env.logstash_path))
    run('curl -O https://download.elasticsearch.org/logstash/logstash/logstash-{0}.tar.gz'.format(env.logstash_version_number
    ))
    run('tar zxvf logstash-{0}.tar.gz -C {1}'.format(env.logstash_version_number, env.logstash_path))
    run('rm ./logstash-{0}.tar.gz'.format(env.logstash_version_number))
    sudo('mv {0}/logstash-{1}/* {0}'.format(env.logstash_path, env.logstash_version_number))
    sudo('rm -rf {0}/logstash-{1}'.format(env.logstash_path, env.logstash_version_number))



def ensure_fresh_directory(path):
    """
    Remove a directory and create it again
    """
    sudo('rm -rf {0}'.format(path))
    sudo('mkdir {0}'.format(path))


@task
def configure(configuration=env.logstash_local_configuration_directory):
    """
    Add upstart job (you can add :configuration='configuration files directory')
    """
    configure_properties(configuration, 'logstash')
    pass_configuration(configuration, 'logstash')


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
    local_path = '{0}{1}/{2}.properties'.format(configuration_path, logstash_config_path, application_name)
    remote_path = '{0}/{1}.properties'.format(logstash_config_path, application_name)
    put(local_path, remote_path, use_sudo=True)


@task
def full(configuration=env.logstash_local_configuration_directory):
    """
    Install with requirements and configure (you can add :configuration='configuration files directory')
    """
    from .. import java
    java.java.oracle.jdk.install()
    install()
    # configure(configuration)
