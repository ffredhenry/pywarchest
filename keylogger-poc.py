#!/usr/bin/python3

import keyboard
keys = keyboard.record(until = 'ENTER')
keyboard.play(keys)
