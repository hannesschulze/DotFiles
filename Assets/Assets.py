import os
import subprocess
import shutil
from Assets.WindowTheme.Map import WINDOW_THEME_FILES

def svgToPng(source, output, hidpi):
    command = ['inkscape', source, '--export-png=' + output]
    if hidpi:
        command.append('--export-dpi=192')
    subprocess.run(command, stdout=subprocess.DEVNULL)

def compileWindowTheme(outputPath, hidpi):
    sourceDir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'WindowTheme')
    for output in WINDOW_THEME_FILES:
        outFile = os.path.join(outputPath, 'xfwm4', output + '.png')
        sourceFile = os.path.join(sourceDir, WINDOW_THEME_FILES[output] + '.svg')
        print('Exporting asset: ' + sourceFile + ' -> ' + outFile)
        svgToPng(sourceFile, outFile, hidpi)

def compileGtkTheme(outputPath, hidpi):
    sourceFile = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'GtkTheme', 'GtkTheme')
    print('Building theme: ' + sourceFile)
    shutil.rmtree(os.path.join(outputPath, 'oomox-GtkTheme'), ignore_errors=True)
    command = ['oomox-cli', '-t', outputPath]
    if hidpi:
        command.append('--hidpi')
        command.append('True')
    command.append(sourceFile)
    subprocess.run(command, stdout=subprocess.DEVNULL)

def compileAssets(root, hidpi=False):
    compileWindowTheme(os.path.join(root, 'themes/WindowTheme'), hidpi)
    compileGtkTheme(os.path.join(root, 'themes'), hidpi)
