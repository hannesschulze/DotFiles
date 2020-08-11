import subprocess
import os
from Build import build

# Build
build()

def installFolder(source, dest):
    homedir = os.getenv('HOME')
    destdir = os.path.join(homedir, dest)
    print('Installing ' + source + ' -> ' + destdir)
    subprocess.call(['mkdir', '-p', destdir])
    subprocess.call(['cp', '-r', source, destdir])

# Install dotfiles
installFolder('themes/oomox-GtkTheme', '.themes')
installFolder('themes/WindowTheme', '.themes')
installFolder('icons/Zafiro-icons', '.icons')
