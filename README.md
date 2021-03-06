# Dotfiles

![Screenshot](Screenshot.png)

## Dependencies

- `xfce4`
- `ulauncher`
- `xfce4-appmenu-plugin`
- `alacritty`
- `neovim`
- `plank`
- `inkscape`
- `dconf-cli`
- `gtk2-engines`
- `git`
- `ytop`
- `exa`
- `bat`

## Installation

```sh
python3 Install.py [--hidpi]
```

### Completing the installation

Set the desktop background color to **#333**

Set up autostart for the following applications:

- `plank`
- `ulauncher` (can be set up from the application itself)

### Fixing the GTK theme

Generating the GTK theme using `oomox-cli` does not seem to work properly. If that is the case, import the color scheme (`Assets/GtkTheme/GtkTheme`) into `oomox-gui` and generate the theme.

## Usage

Use <kbd>Alt</kbd> <kbd>Space</kbd> to access Ulauncher.
