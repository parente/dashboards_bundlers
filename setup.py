# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import os
from setuptools import setup


# Get location of this file at runtime
HERE = os.path.abspath(os.path.dirname(__file__))

# Eval the version tuple and string from the source
VERSION_NS = {}
with open(os.path.join(HERE, 'jupyter_dashboards_bundlers/_version.py')) as f:
    exec(f.read(), {}, VERSION_NS)

setup(
    name='jupyter_dashboards_bundlers',
    author='Jupyter Development Team',
    author_email='jupyter@googlegroups.com',
    description='Plugins for jupyter_cms to deploy and download notebooks as dashboard apps',
    long_description = '''
    This package adds a *Deploy as* and *Download as* menu items for bundling 
notebooks created using jupyter_dashboards as standalone web applications.

See `the project README <https://github.com/jupyter-incubator/dashboards_bundlers>`_
for more information. 
''',   
    url='https://github.com/jupyter-incubator/dashboards_bundlers',
    version=VERSION_NS['__version__'],
    license='BSD',
    platforms=['Jupyter Notebook 4.0.x'],
    packages=[
        'jupyter_dashboards_bundlers',
        'jupyter_dashboards_bundlers.local_deploy',
        'jupyter_dashboards_bundlers.php_download'
    ],
    include_package_data=True,
    scripts=[
        'scripts/jupyter-dashboards_bundlers'
    ],
    install_requires=['jupyter_cms>=0.3.0'],
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ]
)