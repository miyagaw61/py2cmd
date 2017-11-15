from enert import *
import better_exceptions
import os

def main():
    script_name = re.compile('(.*)\.py').findall(argv[1])[0]
    make_setup(script_name)
    install(script_name)

def make_setup(script_name):
    Shell(f'mkdir {script_name}').call()
    setup_text = f"""\
from setuptools import setup, find_packages

console_scripts = [
        '{script_name}={script_name}.{script_name}:main',
        ]

setup(
    name='{script_name}',
    version='0.0.1',
    packages=find_packages(),
    description='{script_name}',
    author='Taisei Miyagawa @miyagaw61',
    author_email='miyagaw61@gmail.com',
    entry_points = {{'console_scripts': console_scripts}},
    url='https://github.com/miyagaw61',
    license='MIT'
)\
"""
    init_text = f"""\
from .{script_name} import *
__version__ = '0.0.1'\
"""
    File(f'setup.py').write(setup_text)
    File(f'{script_name}/__init__.py').write(init_text)
    Shell(f'cp -a {script_name}.py {script_name}').call()

def install(script_name):
    Shell('python setup.py install > /dev/null 2>&1').call()
    File(f'{script_name}').rm()
    File('setup.py').rm()
    File('build').rm()
    File('dist').rm()
    File(f'{script_name}.egg-info').rm()
    HOME = os.environ['HOME']
    bashrc = File(f'{HOME}/.bashrc').read()
    Shell(bashrc).call()

if __name__ == '__main__':
    main()
