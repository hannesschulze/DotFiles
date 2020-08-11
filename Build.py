import os
import sys
import subprocess
from Assets.Assets import compileAssets

def checkForRequirement(requirement):
    try:
        subprocess.call([requirement, '--version'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print('Requirement "' + requirement + '" found')
    except OSError as e:
        print('Error: Requirement "' + requirement + '" not found!')
        exit()

def build():
    # Requirements
    checkForRequirement('inkscape')
    checkForRequirement('oomox-cli')
    checkForRequirement('git')
    checkForRequirement('dconf')
    checkForRequirement('plank')
    checkForRequirement('wget')
    checkForRequirement('unzip')

    # Arguments
    hidpi = '--hidpi' in sys.argv

    # Compile the assets
    rootPath = os.path.dirname(os.path.abspath(__file__))
    compileAssets(rootPath, hidpi=hidpi)

    # Download submodules
    print('Downloading additional git submodules...')
    subprocess.call(['git', 'submodule', 'init'])
    subprocess.call(['git', 'submodule', 'update'])

    # Download Inter
    print('Downloading Inter...')
    interPath = os.path.join(rootPath, 'Assets/Inter.zip')
    extractedPath = os.path.join(rootPath, 'fonts/inter')
    if not os.path.exists(interPath):
        subprocess.call(['wget', 'https://github.com/rsms/inter/releases/download/v3.13/Inter-3.13.zip', '-O', interPath], stdout=subprocess.DEVNULL)
    assert(os.path.exists(interPath))
    if not os.path.exists(extractedPath):
        subprocess.call(['unzip', interPath, '-d', extractedPath], stdout=subprocess.DEVNULL)


if __name__ == '__main__':
    build()
