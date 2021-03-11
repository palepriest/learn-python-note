# -*- coding:utf-8 -*-

# dict style
# mystuff = {'apple': "I AM APPLES!"}
# print mystuff['apple']

# module style
# import mystuff

# mystuff.apple()
# print mystuff.tangerine

# class style
# class MyStuff():

#     def __init__(self):
#         self.tangerine = "And now a thousand years between."

#     def apple():
#         print "I AM CLASSY APPLES!"

class Song(object):
    
    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't wan to get sued",
                   "So I'll stop right there"])
bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_a_song()
bulls_on_parade.sing_a_song()