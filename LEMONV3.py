# MIT License
# 
# Copyright (c) 2025 zuparb
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

unusual = {"axes": "axe",
           "children": "child",
           "people": "person",
           "mice": "mouse",
           "lice": "louse",
           "fish": "fish",
           "shrimp": "shrimp",
           "oxen": "ox",
           "rice": "a grain of rice",
           "men": "man",
           "women": "woman",
           "geese": "goose",
           "teeth": "tooth",
           "deer": "deer",
           "sheep": "sheep",
           "tuna": "tuna",
           "feet": "foot",
           "dice": "die",
           "enterprises": "enterprise",
           "devices": "device",
           "practices": "practice",
           "vices": "vice",
           "databases": "database",
           "showcases": "showcase",
           "offices": "office",
           "releases": "release",
           "notices": "notice",
           "staircases": "staircase",
           "synopses": "synopsis",
           "buses": "bus",
           "atlases": "atlas"}

# Currently, the algorithm is finely tuned to handle the underlying logic behind greek and latin to english lemmatization.
# However, some words are niche/unpredictable so they have to get placed inside here.
# Unfortunately, there are no simple algorithm to determine wether or not a word should stay put or get an obscure suffix.
# Ex. If i put the rule word.endswith("ia") to detect Latin words greek words will get 'incorrectly' flagged
# Remember, on a philosphical standpoint this engine is never wrong, grammaticaly it can be though
# If you don't like a lazy/inefficient solution of mine, fix it! :)

Latin = {"bacteria": "bacterium",
         "opus": "opera",
         "corpus": "corpora"}
def lemo(word):
    word = word.lower()
    single = word[:-1]
    
    if word == "axes":
        print("Axes is the plural for both axis and axe")
    elif word in unusual:
        single = unusual[word]
    elif word in Latin:
        single = Latin[word]
    elif word.endswith(("ies")) and word[:-3].endswith(("t", "b", "r", "n", "l", "d", "c", "s", "g", "h", "x")):
        single = word[:-3] + "y"
    elif word.endswith(("mata", "uses")):
        single = word[:-2]
    elif word.endswith(("ons", "ops", "ents", "ols", "ors", "oms", "ows", "ots", "oks", "ods", "ads", "uses", "urses")):
        single = word[:-1] #Sorry for the inelegant solution, but it has to work with another rule. It ain't pretty but it works.
    elif word.endswith("a") and word[:-1].endswith(("di","ci", "t", "l", "d", "v")):
        single = word[:-1] + "um"
    elif word.endswith("a") and word[:-1].endswith(("ri", "li", "ti", "r", "ri", "m", "mi", "n")):
        single = word[:-1] + "on"
    elif word.endswith("i"):
        single = word[:-1] + "us"
    elif word.endswith("ices"):
        single = word[:-4] + "ix"
    elif word[:-2].endswith(("ss", "ps")):
        single = word[:-2]
    elif word[:-2].endswith(("ch", "x", "z", "sh", "o")) and len(word[:-2]) >= 3:
        single = word[:-2]
    elif word.endswith("eces"):
        single = word[:-4] + "ex"
    elif word.endswith(("tives", "hives", "rives")):
        single = word[:-1]
    elif len(word[:-3]) > 2 and word.endswith("ves"):
        single = word[:-3] + "f"
    elif len(word[:-3]) >= 2 and word.endswith("ves"):
        single = word[:-3] + "fe"
    elif word.endswith(("ases", "eses", "oses", "yses", "ises", "pses")):
        single = word[:-2] + "is"
    elif word[-3:] == "men":
        single = word.replace("men", "man")
    return single
    
while True:
    print("Use a plural! LEMONV3")
    wish = input("Please enter the word(s) you wish to lemonize: ").split()

    if wish and wish[0].lower() == "quit":
        break
    
    lemon_form = [lemo(word) for word in wish]
    print("Lemonized word: ", " ".join(lemon_form))
    print(" ")
    
#THIS IS LEMONV3.
#CLOSE TO PERFECT.