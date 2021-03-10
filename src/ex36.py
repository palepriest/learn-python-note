# Description: write a interesting game with 
# lists, functions and modules you have learned.

# Design: draw a map first for figuring out
# the rooms, monsters and traps, which players encounter.

# Coding according to the splited tasks.

# -*- coding:utf-8 -*-
from sys import exit

# common events
def battle():

def dead(why):
    print why, "Game Over!"
    exit(0)

# game goal: collect sky-pearls with 5 kinds of element.
def game_goal():

# step: water sky-pearl
def water_pearl():

# step: fire sky-pearl
def fire_pearl():

# step: thunder sky-pearl
def thunder_pearl():

# step: wind sky-pearl
def wind_pearl():

# step: terra sky-pearl
def terra_pearl():

# preface: sky-pearls falling out through the world.
def start():
    elements = ['水', '火', '风', '雷', '土']
    print "很久很久以前，天地初生，因能量消耗殆尽，神树进入了休眠，"
    print "做为天地灵气孕育出的精灵，你需要收集 5 种元素的灵珠唤醒神树，"
    print "水、火、风、雷、土灵珠散落各自的灵域，你想先去寻找哪一个？"

    choice = raw_input("> ")

    if choice == elements[0]:
        water_pearl()
    elif choice == elements[1]:
        fire_pearl()
    elif choice == elements[2]:
        wind_pearl()
    elif choice == elements[3]:
        thunder_pearl()
    elif choice == elements[4]:
        terra_pearl()
    else：
        dead("You stumble around the room until you starve.")

# start your game.
start()