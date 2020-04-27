# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 16:59:13 2020

@author: User-PC
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 12:33:07 2020

@author: User-PC
"""

###CHECKBOX FORK BECAUSE UPDATE ISN'T WORKING WITH PYINSTALL

import PySimpleGUI as sg
import playsound as ps
import keyboard


##code for the airhorn
#ps.playsound(r"Data/mlg-airhorn.mp3")

#code for spoopy
#ps.playsound(r"Data/OtisSpoops.mp3")
#code for "pop Noice"
##ps.playsound(r"Data/OtisNoice.mp3")
#code for thanksforsubscribing
##ps.playsound(r"Data/OtisThanks.mp3")

sg.theme(new_theme="Topanga")

def makelayout():
    Layout=[[sg.Text("Zera's soundboard!")],
        [sg.Text("")],
        [sg.Checkbox("Sound board on?",key="checkbox")],
        [sg.Text("")],
        [sg.Text("Press j to play thanks")],
        [sg.Text("Press k to play airhorn")],
        [sg.Text("Press l to play spoops")],
        [sg.Text("Press ; to play noice")],
        [sg.Text("")],
        [sg.Quit()]]
    return Layout
    


win=sg.Window("Otis Productions",layout=makelayout())
#test=keyboard.on_press_key(key="spacebar",callback="test1")

soundboardon=False
while True:
    event,values=win.read(timeout=100)
    if event in ("Quit",None):
        break
    if keyboard.is_pressed("j") and values["checkbox"]:
        ps.playsound(r"Data/OtisThanks.mp3")
    if keyboard.is_pressed("k") and values["checkbox"]:
        ps.playsound(r"Data/mlg-airhorn.mp3")
    if keyboard.is_pressed("l") and values["checkbox"]:
        ps.playsound(r"Data/OtisSpoops.mp3")
    if keyboard.is_pressed("semicolon") and values["checkbox"]:
        ps.playsound(r"Data/OtisNoice.mp3")
        
win.close()