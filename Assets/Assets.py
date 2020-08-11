import os
import subprocess
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

def compileAssets(root, hidpi=False):
    compileWindowTheme(os.path.join(root, 'themes/WindowTheme'), hidpi)
