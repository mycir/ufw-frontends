#!/usr/bin/env python3

from distutils.command.install import install
from distutils.core import setup

from ufw_frontends import __version__


class Install(install, object):

    def run(self):
        self.install_scripts = '/usr/bin'
        super(Install, self).run()


setup(
    name='ufw_frontends',
    version=__version__,
    description='Graphical frontends for ufw',
    author='Darwin M. Bautista',
    author_email='djclue917@gmail.com',
    url='http://code.google.com/p/ufw-frontends/',
    cmdclass={'install': Install},
    scripts=['ufw-frontends', 'ufw-frontends-pkexec'],
    packages=['ufw_frontends'],
    package_data={'ufw_frontends': ['resources/*']},
    data_files=[
        ('/usr/share/icons/hicolor/48x48/apps', ['share/ufw-frontends.png']),
        ('/usr/share/applications', ['share/ufw-frontends-gtk.desktop']),
        ('/usr/share/polkit-1/actions', ['share/com.baudm.pkexec.ufw-frontends.policy'])
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
