from fabric.api import task
from fabric.api import sudo

@task
def install():
    """
     Install Kafka protocol support in Python
     https://github.com/mumrah/kafka-python
    """
    # sudo('apt-get install -y python-pip') #First I need install pip
    sudo('pip install kafka-python' )
