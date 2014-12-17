from fabric.api import task
from fabric.api import run


@task
def install():
    """
    Get Redis source and build
    """
    sudo('mkdir -p /etc/redis')
    sudo('mkdir -p /var/redis')
    sudo('mkdir -p /var/redis/6379')
    run('mkdir -p ~/tmp')
    run('wget -P ~/tmp http://download.redis.io/redis-stable.tar.gz')
    with cd('~/tmp'):
        run('tar xvzf redis-stable.tar.gz')
    #sudo('rm redis-stable.tar.gz')
    with cd('~/tmp/redis-stable'):
        run('make distclean')
        run('make')
        sudo('make install')
        sudo('cp ./utils/redis_init_script /etc/init.d/redis_6379')
        sudo('cp ./redis.conf /etc/redis/6379.conf')
    rm('rm -rf ~/tmp')
    sed('/etc/redis/6379.conf', 'daemonize no', 'daemonize yes',
        use_sudo=True)
    sed('/etc/redis/6379.conf', 'pidfile /var/run/redis.pid',
        'pidfile /var/run/redis_6379.pid', use_sudo=True)
    sed('/etc/redis/6379.conf', 'logfile stdout',
        'logfile /var/log/redis_6379.log', use_sudo=True)
    sed('/etc/redis/6379.conf', 'dir ./', 'dir /var/redis/6379',
        use_sudo=True)
    sudo('/etc/init.d/redis_6379 start')
    sudo('update-rc.d redis_6379 defaults')