# setup.py
from distutils.core import setup
import glob
import py2exe

setup(name="invasores",
      description="Very simple game written in Python.",
      version="0.9_beta3",
      windows=[
    {
      "script": "invasores.py",
      "icon_resources": [(1,"pygame.ico")]
    }
             ],
      data_files=[("", glob.glob("*.png")),
                  ("", glob.glob("*.bmp")),
                  ("fonts",  glob.glob("*.ttf")),
                  ("sons",    glob.glob("sons/*.wav")),
                  ("lang",    glob.glob("lang/*.lang")),
                  ("licenca",    glob.glob("licenca/*.txt"))])
