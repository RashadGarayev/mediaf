from setuptools import setup
import os
os.system("sudo apt-get install libmp3lame-dev")
os.system("sudo apt-get install ffmpeg")
setup(
name='mediaf',
py_modules=['mediaf'],
version='1',
description='pip install mediaf',
url='https://github.com/RashadGarayev/mediaf',
author='Rashad Garayev',
author_email='pythonaz@yahoo.com',
license='MIT'
)
