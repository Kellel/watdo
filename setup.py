from distutils.core import setup
from getpass import getuser

setup(name='watdo',
      version='0.1',
      description='A stupid simple todo list',
      author='Kellen Fox',
      url='https://github.com/Kellel/watdo',
      packages=['watdo'],
      scripts=['scripts/wat',],
      data_files=[('/home/{}/.wat'.format(getuser()), ['data/wat.dat'])],)
