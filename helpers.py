import json
import tkinter as tk
from tkinter import filedialog
import pygame

pygame.mixer.init()

def save_file(instrument_dictionary):
    file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    if file_path:
        with open(file_path, "w") as f:
            json.dump(instrument_dictionary, f)




def open_file(instrument_dictionary, instrument_visual_bool):
    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if file_path:
        with open(file_path, "r") as f:
            new_instrument_dictionary = json.load(f)
        instrument_dictionary.clear()
        instrument_dictionary.update(new_instrument_dictionary)

        for drum_type, beats in instrument_dictionary.items():
            for index, value in enumerate(beats):
                instrument_visual_bool[drum_type][index].set(value)


def clear_all(instrument_dictionary, instrument_visual_bool):
    for drum_type in instrument_dictionary:
        for i in range(len(instrument_dictionary[drum_type])):
            instrument_dictionary[drum_type][i] = False
            instrument_visual_bool[drum_type][i].set(False)


def start_playback(get_bpm, instrument_dictionary, sounds):
    bpm = get_bpm
    if bpm is not None:
        mpb = 60 / bpm

        for i in range(8):
            for drum_type, beats in instrument_dictionary.items():
                if beats[i]:
                    sounds[drum_type].play()
            pygame.time.wait(int(mpb * 1000))