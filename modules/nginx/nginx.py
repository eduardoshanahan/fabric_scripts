from fabric.api import cd
from fabric.api import env
from fabric.api import local
from fabric.api import put
from fabric.api import run
from fabric.api import sudo
from fabric.api import task


env.nginx_configuration_directory = 'configuration/nginx'


@task
def install(configuration=env.nginx_configuration_directory):
    """
    Nginx from source (you can add :configuration='configuration files directory')
    """
    version = '1.4.1'
    url = 'http://nginx.org/download/nginx-{0}.tar.gz'.format(version)
    sudo('apt-get install -y libpcre3')
    sudo('apt-get install -y libpcre3-dev')
    sudo('apt-get install -y libssl-dev')
    sudo('apt-get install -y zlib1g')
    sudo(('adduser '
          '--system '
          '--no-create-home '
          '--disabled-login '
          '--disabled-password '
          '--group nginx'))
    sudo('mkdir -p /var/www')
    run('mkdir -p ~/tmp')
    run('wget -P ~/tmp {0}'.format(url))
    with cd('~/tmp'):
        run('tar xvzf nginx-{0}.tar.gz'.format(version))
    with cd('~/tmp/nginx-{0}'.format(version)):
        run(('./configure '
             '--prefix=/opt/nginx '
             '--user=nginx '
             '--group=nginx '
             '--with-http_ssl_module '
             '--without-http_scgi_module '
             '--without-http_uwsgi_module '
             '--without-http_fastcgi_module'))
        run('make')
        sudo('make install')
    run('rm -rf ~/tmp')


@task
def configure(configuration=env.nginx_configuration_directory):
    """
    Create the config file to host the application (you can add :configuration='configuration files directory')
    """
    sudo('touch /opt/nginx/conf/nginx.conf')
    sudo('mkdir -p /opt/nginx/conf/backup')
    sudo('mv --backup=numbered /opt/nginx/conf/nginx.conf /opt/nginx/conf/backup')
    put('{0}/opt/nginx/conf/nginx.conf'.format(configuration), '/opt/nginx/conf/nginx.conf', use_sudo=True)
    sudo('initctl stop nginx', warn_only=True)
    put('{0}/etc/init/nginx.conf'.format(configuration), '/etc/init/nginx.conf', use_sudo=True)


@task
def start():
    """
    Fire off the service
    """
    sudo('initctl start nginx')

@task
def prerequisites():
    """
    Tools needed for Nginx to be installed and working
    """
    from .. import tools
    tools.make.install()


@task
def full(configuration=env.nginx_configuration_directory):
    """
    Install and configure
    """
    prerequisites()
    install(configuration)
    configure(configuration)
    start()
