import tkinter as tk
from tkinter import ttk, Menu
from ctypes import windll
import pygame 
import threading

import numpy as np

from helpers import save_file, open_file, clear_all, start_playback

pygame.mixer.init()

sounds = {
    "bass": pygame.mixer.Sound("assets/audio/samples/bass.ogg"),
    "hihat": pygame.mixer.Sound("assets/audio/samples/hihat.ogg"),
    "snare": pygame.mixer.Sound("assets/audio/samples/snare.ogg")
}


def command():
    x = 1

def toggle_drum_beat(drum_type, location, current_dictionary):
    if current_dictionary[drum_type][location] == False:
        current_dictionary[drum_type][location] = True
    elif current_dictionary[drum_type][location] == True:
        current_dictionary[drum_type][location] = False

root = tk.Tk()
root.title("Drum thingmabob")
windll.shcore.SetProcessDpiAwareness(1)

frm_instruments = ttk.Frame(root, padding=10)
frm_instruments.grid(column=0, row=1)







menubar = Menu(root)
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="New", command=command)
file_menu.add_command(label="Open", command=lambda: open_file(current_instrument_dictionary, tk_variable_list_to_stop_bad_behaviour))
file_menu.add_command(label="Save as", command=lambda: save_file(current_instrument_dictionary))
file_menu.add_command(label="Quit", command=root.destroy)

menubar.add_cascade(label="File", menu=file_menu)

new_list = [False] * 8
tk_variable_list_to_stop_bad_behaviour = {
    "hihat": [],
    "snare": [],
    "bass": []
}

for i in range(8):
    tk_variable_list_to_stop_bad_behaviour["hihat"].append(tk.BooleanVar())
    tk_variable_list_to_stop_bad_behaviour["snare"].append(tk.BooleanVar())
    tk_variable_list_to_stop_bad_behaviour["bass"].append(tk.BooleanVar())
    

current_instrument_dictionary = {
    "hihat": new_list.copy(),
    "snare": new_list.copy(),
    "bass": new_list.copy()
}
print(tk_variable_list_to_stop_bad_behaviour)
print(current_instrument_dictionary)

frm_setting1 = ttk.Frame(root, padding=10)
frm_setting1.grid(column=0, row=0)

bpmLabel = ttk.Label(frm_setting1, text="BPM:")
bpmLabel.grid(column=0, row=0)
bpmEntry = ttk.Entry(frm_setting1)
bpmEntry.grid(column=1, row=0)

#hihat area
hihatLabel = ttk.Label(frm_instruments, text="hi-hat:")
hihatLabel.grid(column=0, row=1)
for i in range(8):

    ttk.Checkbutton(frm_instruments, variable=tk_variable_list_to_stop_bad_behaviour["hihat"][i], command= lambda current_i_value=i: [toggle_drum_beat("hihat", current_i_value, current_instrument_dictionary), sounds["hihat"].play()]).grid(column=i + 3, row=1)


#snare area
snareLabel = ttk.Label(frm_instruments, text="snare:")
snareLabel.grid(column=0, row=2)

for i in range(8):
    ttk.Checkbutton(frm_instruments, variable=tk_variable_list_to_stop_bad_behaviour["snare"][i], command= lambda current_i_value=i: [toggle_drum_beat("snare", current_i_value, current_instrument_dictionary), sounds["snare"].play()]).grid(column=i + 3, row=2)

#bass area
bassLabel = ttk.Label(frm_instruments, text="base:")
bassLabel.grid(column=0, row=3)
for i in range(8):
    ttk.Checkbutton(frm_instruments, variable=tk_variable_list_to_stop_bad_behaviour["bass"][i], command= lambda current_i_value=i: [toggle_drum_beat("bass", current_i_value, current_instrument_dictionary), sounds["bass"].play()]).grid(column=i + 3, row=3)


def get_bpm():
    bpm = bpmEntry.get()
    try:
        bpm = int(bpm)
        if bpm < 20 or bpm > 300:
            raise ValueError
        return bpm
    except:
        tk.messagebox.showerror("Invalid BPM", "Please enter a valid BPM between 20 and 300.")
        return None


playback = False
def set_playback_false():
    playback = False

frm_buttons = ttk.Frame(root, padding=10)
frm_buttons.grid(column=1, row=1)
play_button = tk.Button(frm_buttons, text="play", command= lambda: [start_playback(get_bpm(), current_instrument_dictionary, sounds)]).grid(column=0, row=0)
stop_button = tk.Button(frm_buttons, text="stop", command= lambda: set_playback_false(playback)).grid(column=0, row=1)
clear_button = tk.Button(frm_buttons, text="clear", command= lambda: clear_all(current_instrument_dictionary, tk_variable_list_to_stop_bad_behaviour)).grid(column=0, row=3)





root.config(menu=menubar)
root.mainloop()