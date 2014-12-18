from fabric.api import task


@task
def install():
    """
    Install using the default credentials
    """
    import password
    import mysql
    password.default()
    mysql.install()