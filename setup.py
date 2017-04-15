from distutils.core import setup
import glob
import os

if os.name == 'nt':
    import py2exe

setup(name="invasores",
      description="Very simple game written in Python.",
      version="0.9.9",
      author='Nilo Menezes',
      author_email="nilo@nilo.pro.br",
      url="https://github.com/lskbr/invasores",
      requires=["pygame(>=1.9)"],
      windows=[
          {
              "script": "invasores.py",
              "icon_resources": [(1, "pygame.ico")]
          }
      ],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: MacOS X',
          'Environment :: X11 Applications',
          'Environment :: Win32 (MS Windows)          ',
          'Intended Audience :: Education',
          'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
          'Natural Language :: English',
          'Natural Language :: French',
          'Natural Language :: Spanish',
          'Natural Language :: Portuguese (Brazilian)',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows :: Windows 7',
          'Operating System :: Microsoft :: Windows :: Windows 8',
          'Operating System :: Microsoft :: Windows :: Windows 8.1',
          'Operating System :: Microsoft :: Windows :: Windows 10',
          'Operating System :: POSIX :: BSD :: FreeBSD',
          'Operating System :: POSIX :: BSD :: OpenBSD',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python :: 3.6',
          'Topic :: Games/Entertainment :: Arcade',
          ],
      data_files=[("", glob.glob("*.png")),
                  ("", glob.glob("*.bmp")),
                  ("fonts", glob.glob("*.ttf")),
                  ("sons", glob.glob("sons/*.wav")),
                  ("lang", glob.glob("lang/*.lang")),
                  ("licenca", glob.glob("licenca/*.txt"))])
