# easy-click
Easy-Click is a simple event listener that allows you to perform mouse clicks using your hardware keyboard.

## Why?
Touchpads are usually small and hard to use for anything else other than just navigation. Imagine you're trying to draw something with your favourite open-source vector software and you have to press down on your touchpad to actually keep drawing. Now, this creates a problem because whenever you're pressing really hard it's much harder to move your finger because of the friction.

Here are two results I've got:

|                                                    Without Easy-Click                                                     |                                                   With Easy-Click                                                   |
| :-----------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------: |
| <img alt="Without Easy-Click" src="https://raw.githubusercontent.com/f34rl00/easy-click/master/images/no-easy-click.png"> | <img alt="With Easy-Click" src="https://raw.githubusercontent.com/f34rl00/easy-click/master/images/easy-click.png"> |

> Notice how it looks more curly and natural with Easy-Click. And no, I didn't make the first one bad intentionally.

## Installation
> This script is created and tested on a linux system and isn't intented for other operating systems. But this doesn't mean that it won't work with other systems.
1. Clone the repository and install the python module **pynput**:
```
git clone https://github.com/f34rl00/easy-click.git
cd easy-click
python -m pip install -r requirements.txt
```

2. Install **xdotool**:
> If you're unsure, check out its [own repo](https://github.com/jordansissel/xdotool)
- Arch Linux: pacman -S xdotool
- Debian and Ubuntu: apt-get install xdotool
- Fedora: dnf install xdotool
- FreeBSD: pkg install xdotool
- macOS: brew install xdotool or sudo port install xdotool
- OpenSUSE: zypper install xdotool

3. Move the script to **.local/bin** for direct usage (optional):
```
cp easy-click ~/.local/bin/
```

## Usage
Start Easy-Click by running the command `easy-click`. This will shrink the terminal window and put it in the bottom right corner of your screen. If it says `Mode:On`, then the event listener should be running. The window will move itself out of the way if you need to click something underneath the terminal window.

Here are the default keys:
- Back quote key: Hold down left click
- 1 from number keys: Left click
- 2 from number keys: Right click
- F1: Switch mode on/off
- Esc: Exit

And here's the default layout:
<img src="https://raw.githubusercontent.com/f34rl00/easy-click/master/images/layout.png">
