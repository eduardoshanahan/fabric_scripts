from fabric.api import task


@task
def install(received_password=""):
    """
    Install using the default credentials
    """
    print('password used at mysql.default is {0}'.format(received_password))
    import password
    import mysql
    password.default(received_password)
    mysql.install()
