import os
import subprocess
import shutil
from string import Template
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

def formatXfceHiDPI(outputPath, hidpi):
    sourcePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ConfigHiDPI')
    print('Configuring xfwm4')
    with open(os.path.join(sourcePath, 'xfwm4.xml.in'), 'r') as xfwmFile:
        xfwmTemplate = Template(xfwmFile.read())
    titleFontSize = '16' if hidpi else '9'
    xfwmData = xfwmTemplate.substitute(titlefontsize=titleFontSize)
    with open(os.path.join(outputPath, 'xfwm4.xml'), 'w+') as xfwmFile:
        xfwmFile.write(xfwmData)

    print('Configuring xsettings')
    with open(os.path.join(sourcePath, 'xsettings.xml.in'), 'r') as xsettingsFile:
        xsettingsTemplate = Template(xsettingsFile.read())
    cursorSize = '48' if hidpi else '24'
    scaleFactor = '2' if hidpi else '1'
    xsettingsData = xsettingsTemplate.substitute(cursorsize=cursorSize, scalefactor=scaleFactor)
    with open(os.path.join(outputPath, 'xsettings.xml'), 'w+') as xsettingsFile:
        xsettingsFile.write(xsettingsData)

def formatAlacrittyHiDPI(outputPath, hidpi):
    if not os.path.exists(outputPath):
        os.mkdir(outputPath)
    sourcePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ConfigHiDPI')
    print('Configuring alacritty')
    with open(os.path.join(sourcePath, 'alacritty.yml.in'), 'r') as configFile:
        configTemplate = Template(configFile.read())
    fontSize = '19' if hidpi else '9'
    configData = configTemplate.substitute(fontsize=fontSize)
    with open(os.path.join(outputPath, 'alacritty.yml'), 'w+') as configFile:
        configFile.write(configData)

def compileAssets(root, hidpi=False):
    compileWindowTheme(os.path.join(root, 'themes/WindowTheme'), hidpi)
    compileGtkTheme(os.path.join(root, 'themes'), hidpi)
    formatXfceHiDPI(os.path.join(root, 'config/xfce4/xfconf/xfce-perchannel-xml'), hidpi)
    formatAlacrittyHiDPI(os.path.join(root, 'config/alacritty'), hidpi)
