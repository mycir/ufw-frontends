#!/usr/bin/env python

import os.path
from distutils.command.install import install
from distutils.core import setup

from gfw import __version__


class Install(install, object):

    def run(self):
        # Install scripts to prefix/sbin instead of prefix/bin
        self.install_scripts = os.path.join(self.install_data, 'sbin')
        super(Install, self).run()


setup(
    name='gfw',
    version=__version__,
    description='Graphical frontends for ufw',
    author='Darwin M. Bautista',
    author_email='djclue917@gmail.com',
    url='http://code.google.com/p/ufw-frontends/',
    cmdclass={'install': Install},
    scripts=['ufw-gtk', 'ufw-qt'],
    packages=['gfw'],
    data_files=[('share/ufw-frontends', ['ui/ufw-gtk.glade', 'ui/ufw-qt.ui'])],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: X11 Applications :: GTK',
        'Environment :: X11 Applications :: Qt',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.6'
    ]
)