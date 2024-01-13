import os
import glob
from distutils.core import setup

if os.name == "nt":
    pass

setup(
    name="invasores",
    description="Very simple game written in Python.",
    version="0.9.10b",
    author="Nilo Menezes",
    author_email="nilo@nilo.pro.br",
    url="https://github.com/lskbr/invasores",
    requires=["pygame(>=1.9)"],
    windows=[{"script": "invasores.py", "icon_resources": [(1, "pygame.ico")]}],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: MacOS X",
        "Environment :: X11 Applications",
        "Environment :: Win32 (MS Windows)          ",
        "Intended Audience :: Education",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Natural Language :: French",
        "Natural Language :: Spanish",
        "Natural Language :: Portuguese (Brazilian)",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: Microsoft :: Windows :: Windows 11",
        "Operating System :: POSIX :: BSD :: FreeBSD",
        "Operating System :: POSIX :: BSD :: OpenBSD",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.12",
        "Topic :: Games/Entertainment :: Arcade",
    ],
    data_files=[
        ("", glob.glob("*.png")),
        ("", glob.glob("*.bmp")),
        ("fonts", glob.glob("*.ttf")),
        ("sons", glob.glob("sons/*.wav")),
        ("lang", glob.glob("lang/*.lang")),
        ("licenca", glob.glob("licenca/*.txt")),
    ],
)
