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

PLANK_LAYOUT = "['thunar.dockitem', 'org.gnome.Epiphany.dockitem', 'firefox.dockitem', 'org.gnome.Geary.dockitem', " + \
               "'org.gnome.Calendar.dockitem', 'texstudio.dockitem', 'org.gnome.Builder.dockitem', " + \
               "'jetbrains-studio.dockitem', 'com.alacritty.Alacritty.dockitem', 'gitkraken.dockitem', " + \
               "'discord.dockitem', 'telegramdesktop.dockitem', 'signal-desktop.dockitem', 'spotify.dockitem', " + \
               "'com.github.hannesschulze.conecto.dockitem', 'trash.dockitem']"

def setPlankLayout():
    command = ['dconf', 'write', '/net/launchpad/plank/docks/dock1/dock-items', PLANK_LAYOUT]
    print('Applying plank layout...')
    subprocess.call(command)

# Install dotfiles
installFolder('themes/oomox-GtkTheme', '.themes')
installFolder('themes/WindowTheme', '.themes')
installFolder('icons/Zafiro-icons', '.icons')

# Apply settings
setPlankLayout()
