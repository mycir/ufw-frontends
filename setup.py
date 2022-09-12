#!/usr/bin/env python

from distutils.core import setup

from ufw_frontends import __version__

setup(
    name='ufw-frontends',
    version=__version__,
    description='Graphical frontends for ufw',
    author='Darwin M. Bautista',
    author_email='djclue917@gmail.com',
    url='http://code.google.com/p/ufw-frontends/',
    packages=['ufw_frontends'],
    package_data={ 
        'ufw_frontends': ['resources/*'],
    },
    data_files=[
        ('share/icons/hicolor/128x128/apps', ['share/ufw-frontends.png']),
        ('sbin', ['sbin/ufw-frontends', 'sbin/ufw-frontends-pkexec']),
        ('share/applications', ['share/ufw-frontends-gtk.desktop']),
        ('../share/polkit-1/actions', ['share/com.baudm.pkexec.ufw-frontends.policy'])
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: X11 Applications :: GTK',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.8'
    ]
)
