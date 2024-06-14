''' pg_midi_sound101.py
play midi music files (also mp3 files) using pygame
tested with Python273/331 and pygame192 by vegaseat
'''
import board
import sys
import pygame as pg
import os
import time
from pathlib import Path
import digitalio
from led_ring import rainbow, blink, parts_true, full_circle, start_light
freq = 44100    # audio CD quality
bitsize = -16   # unsigned 16 bit
channels = 2    # 1 is mono, 2 is stereo
buffer = 2048   # number of samples (experiment to get right sound)
volume = 0.2

button_0 = digitalio.DigitalInOut(board.D4)
button_1 = digitalio.DigitalInOut(board.D17)
button_2 = digitalio.DigitalInOut(board.D27)
button_3 = digitalio.DigitalInOut(board.D22)
button_4 = digitalio.DigitalInOut(board.D5)
button_5 = digitalio.DigitalInOut(board.D6)

button_0.direction = digitalio.Direction.INPUT
button_0.pull = digitalio.Pull.UP
button_1.direction = digitalio.Direction.INPUT
button_1.pull = digitalio.Pull.UP
button_2.direction = digitalio.Direction.INPUT
button_2.pull = digitalio.Pull.UP
button_3.direction = digitalio.Direction.INPUT
button_3.pull = digitalio.Pull.UP
button_4.direction = digitalio.Direction.INPUT
button_4.pull = digitalio.Pull.UP
button_5.direction = digitalio.Direction.INPUT
button_5.pull = digitalio.Pull.UP


def play_music(button, song):
    '''
    stream music with mixer.music module
    '''
    print(song)
    if pg.mixer.music.get_busy():
        
        pg.mixer.music.fadeout(1000)
        pg.mixer.music.stop()
        pg.mixer.music.load(song)
        pg.mixer.music.set_volume(volume)
        pg.mixer.music.play()
    else:
        pg.mixer.music.load(song)
        pg.mixer.music.set_volume(volume)
        pg.mixer.music.play()


def stop_music():
    '''
    Stop music
    '''
    if pg.mixer.music.get_busy():
        pg.mixer.music.stop()


def get_folders():

    root = Path('.')
    sound_dir = root / 'sounds'
    music = sound_dir.glob('*')
    return [i for i in music]

def main():
    
    start_light()
    pg.mixer.init(freq, bitsize, channels, buffer)
    folders = get_folders()
    folder_number = 0
    print(len(folders))
    button_states = {0:False, 1:False, 2:False, 3:False, 4:False, 5:False}
    active_folder = folders[folder_number]
    sounds = [i for i in active_folder.glob('*')]

    while True:
        


        if not button_0.value:
            button_states[0] = True
            parts_true(button_states)
            print(sounds[0])
            play_music(0, sounds[0])
            time.sleep(1)

        if not button_1.value:
            button_states[1] = True
            parts_true(button_states)
            print(sounds[1])
            play_music(1, sounds[1])
            time.sleep(1)

        if not button_2.value:
            button_states[2] = True
            parts_true(button_states)
            print(sounds[2])
            play_music(2, sounds[2])
            time.sleep(1)

        if not button_3.value:
            button_states[3] = True
            parts_true(button_states)
            print(sounds[3])
            play_music(3, sounds[3])
            time.sleep(1)

        if not button_4.value:
            button_states[4] = True
            parts_true(button_states)
            print(sounds[4])
            play_music(4, sounds[4])
            time.sleep(1)

        if not button_5.value:
            button_states[5] = True
            parts_true(button_states)
            print(sounds[5])
            play_music(5, sounds[5])
            time.sleep(1)


        if all(button_states.values()) == True:
            full_circle()
            if folder_number == len(folders)-1:
                folder_number = 0
                print(folder_number)
            else:
                folder_number += 1
                print(folder_number)
            sounds = [i for i in active_folder.glob('*')]
            active_folder = folders[folder_number]
            for key in button_states:
                button_states[key] = False
            print(button_states)


if __name__ == "__main__":
    main()
