import shutil
import os
from Build import build

# Build
build()

def installFolder(source, dest):
    homedir = os.getenv('HOME')
    destdir = os.path.join(homedir, dest)
    print('Installing ' + source + ' -> ' + destdir)
    shutil.copytree(source, destdir, dirs_exist_ok=True)

# Install dotfiles
installFolder('themes', '.themes')
