import subprocess
import os
import shutil
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

def setPlankPreferences():
    command = ['dconf', 'write', '/net/launchpad/plank/docks/dock1/dock-items', PLANK_LAYOUT]
    print('Applying plank preferences...')
    subprocess.call(command)
    subprocess.call(['dconf', 'write', '/net/launchpad/plank/docks/dock1/icon-size', '40'])
    subprocess.call(['dconf', 'write', '/net/launchpad/plank/docks/dock1/theme', '"Transparent"'])

# Install dotfiles
installFolder('themes/oomox-GtkTheme', '.themes')
installFolder('themes/WindowTheme', '.themes')
installFolder('icons/Zafiro-icons', '.icons')
installFolder('config/alacritty', '.config')
installFolder('config/nvim', '.config')
installFolder('config/plank', '.config')
installFolder('config/ulauncher', '.config')
installFolder('config/xfce4', '.config')
installFolder('config/zsh', '.config')
installFolder('fonts/JetBrainsMono/ttf', '.fonts')
installFolder('fonts/inter/Inter Desktop', '.fonts')
copyfile('config/.zshrc', '.config/.zshrc')

# Apply settings
setPlankPreferences()
