#!/usr/bin/python
# -*- encoding:utf-8 -*-

import shlex
from subprocess import PIPE, Popen

from pynput import keyboard, mouse
from pynput.mouse import Button, Controller


class Watcher:
    def __init__(self):
        self.mode            = True
        self.window_id       = None
        self.window_position = True

        self.mouse    = Controller()
        self.keyboard = Controller()

        self.mouse_listener = mouse.Listener(
            on_move=self.on_move,
        )

        self.keyboard_listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release
        )

        self.window_setup()

    def window_setup(self):
        proc = Popen(shlex.split('xdotool getactivewindow'),stdout=PIPE)
        self.windowid = int(proc.communicate()[0])

        Popen(shlex.split(f'xdotool windowsize {self.windowid} 40 3'),stdout=PIPE)
        Popen(shlex.split(f'xdotool windowmove {self.windowid} 1880 1077'),stdout=PIPE)
        Popen(shlex.split(f'xdotool windowstate --add STICKY {self.windowid}'),stdout=PIPE)
        Popen(shlex.split(f'xdotool windowstate --add ABOVE {self.windowid}'),stdout=PIPE)

    def on_move(self, x, y):
        # Mouse at bottom right
        if self.window_position and x in range(1558, 1946) and y in range(936, 1109):
            Popen(shlex.split(f'xdotool windowmove {self.windowid} -26 9'),stdout=PIPE)
            self.window_position = False

        # Mouse at top left
        if not self.window_position and x in range(-26, 362) and y in range(9, 182):
            Popen(shlex.split(f'xdotool windowmove {self.windowid} 1880 1075'),stdout=PIPE)
            self.window_position = True

    def on_press(self, key):
        if key == keyboard.Key.f1:
            self.mode = not self.mode
            print(f"Mode:{'On ' if self.mode else 'Off'}", end='\r')

        elif self.mode and hasattr(key, 'vk') and key.vk == 34:
            self.mouse.press(Button.left)

        elif self.mode and hasattr(key, 'vk') and key.vk == 49:
            self.mouse.press(Button.left)
            self.mouse.release(Button.left)

        elif self.mode and hasattr(key, 'vk') and key.vk == 50:
            self.mouse.press(Button.right)
            self.mouse.release(Button.right)

        # Exit Program
        elif self.mode and key == keyboard.Key.esc:
            Popen(shlex.split(f'xdotool windowstate --remove STICKY {self.windowid}'),stdout=PIPE)
            Popen(shlex.split(f'xdotool windowstate --remove ABOVE {self.windowid}'),stdout=PIPE)
            exit()

        elif hasattr(key, 'vk'):
            self.keyboard.press(key.vk)

    def on_release(self, key):
        if self.mode and hasattr(key, 'vk') and key.vk == 34:
            self.mouse.release(Button.left)

    def start(self):
        self.mouse_listener.start()
        self.keyboard_listener.start()
        self.keyboard_listener.join()


if __name__ == "__main__":
    watcher = Watcher()
    watcher.start()
