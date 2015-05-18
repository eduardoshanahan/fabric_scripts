from fabric.api import run
from fabric.api import task
import os


@task
def root_path():
  """
  Get the root path for a given operating system
  """
  result = os.path.abspath(os.sep)
  print('root path is {0}'.format(result))
  return result