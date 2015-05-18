from fabric.api import cd
from fabric.api import env
from fabric.api import put
from fabric.api import run
from fabric.api import sudo
from fabric.api import task


env.elasticsearch_version_number = '1.4.4'
env.elasticsearch_path = '/usr/lib/elasticsearch'
env.elasticsearch_config_path = '/etc/elasticsearch'
env.elasticsearch_local_configuration_directory = 'configuration/elasticsearch'


@task
def install():
    """
    From binary
    curl -X GET http://localhost:9200/
    """
    ensure_fresh_directory(env.elasticsearch_path)
    sudo('chmod a+rw {0}'.format(env.elasticsearch_path))
    run('curl -O https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-{0}.tar.gz'.format(env.elasticsearch_version_number
    ))
    run('tar zxvf elasticsearch-{0}.tar.gz -C {1}'.format(env.elasticsearch_version_number, env.elasticsearch_path))
    run('rm ./elasticsearch-{0}.tar.gz'.format(env.elasticsearch_version_number))
    sudo('mv {0}/elasticsearch-{1}/* {0}'.format(env.elasticsearch_path, env.elasticsearch_version_number))
    sudo('rm -rf {0}/elasticsearch-{1}'.format(env.elasticsearch_path, env.elasticsearch_version_number))



def ensure_fresh_directory(path):
    """
    Remove a directory and create it again
    """
    sudo('rm -rf {0}'.format(path))
    sudo('mkdir {0}'.format(path))


@task
def configure(configuration=env.elasticsearch_local_configuration_directory):
    """
    Add upstart job (you can add :configuration='configuration files directory')
    """
    pass_configuration(configuration, 'elasticsearch')


def pass_configuration(configuration_path, application_name):
    """
    Put the upstart file in place
    """
    sudo('initctl stop {0}'.format(application_name), warn_only=True)
    put('{0}/etc/init/{1}.conf'.format(configuration_path, application_name), '/etc/init/{0}.conf'.format(application_name), use_sudo=True)
    sudo('initctl start {0}'.format(application_name))


@task
def plugins():
    """
    Usual plugins
    """
    with cd('{0}'.format(env.elasticsearch_path)):
        run('bin/plugin --install mobz/elasticsearch-head')
        run('bin/plugin -install lmenezes/elasticsearch-kopf')
        run('bin/plugin --install elasticsearch/marvel/latest')


@task
def full(configuration=env.elasticsearch_local_configuration_directory):
    """
    Install with requirements and configure (you can add :configuration='configuration files directory')
    """
    from .. import java
    java.java.oracle.jdk.install()
    install()
    configure(configuration)
    plugins()
    sudo('initctl start elasticsearch', warn_only=True)
