import os
import sys
import subprocess
from Assets.Assets import compileAssets

def checkForRequirement(requirement):
    try:
        subprocess.call([requirement, '--version'], stdout=subprocess.DEVNULL)
        print('Requirement "' + requirement + '" found')
    except OSError as e:
        print('Error: Requirement "' + requirement + '" not found!')
        exit()

def build():
    # Requirements
    checkForRequirement('inkscape')
    checkForRequirement('oomox-cli')

    # Arguments
    hidpi = '--hidpi' in sys.argv

    # Compile the assets
    compileAssets(os.path.dirname(os.path.abspath(__file__)), hidpi=hidpi)

if __name__ == '__main__':
    build()
