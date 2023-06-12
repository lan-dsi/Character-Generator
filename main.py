import os
import random
import time
import colorama
from colorama import Fore

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

with open("Colors.txt", "r") as file:
    allText = file.read()
    Colors = list(map(str, allText.split()))
#gets list of colors from text file.
with open("Skin-color.txt", "r") as file:
    allText = file.read()
    Skin = list(map(str, allText.split()))
#gets list of skin colors
with open("Hair.txt", "r") as file:
    allText = file.read()
    Hair = list(map(str, allText.split()))
#gets list of hair styles
with open("Aesthetics.txt", "r") as file:
    allText = file.read()
    Aesthetics = list(map(str, allText.split()))
#gets list of aesthic types
with open("Themes.txt", "r") as file:
    allText = file.read()
    Themes = list(map(str, allText.split()))
#gets list of themes
gen = ["Female",]
attire = ["Casual","Formal"]
Height = ["Short", "Average", "Tall"]
Hheight = ["Short", "Average", "Long"]
#defines certain traits




def Generate():
  print("Character theme:", random.choice(Themes))
  print("Character Aesthetics:", random.choice(Aesthetics))
  print("Character Sex:", random.choice(gen))
  print("Character age:", random.randrange(15,35))
  print("Character skin color:", random.choice(Skin))
  print("Character hair color:", random.choice(Colors))
  print("Character hair style:", random.choice(Hair))
  print("Character Hair Length", random.choice(Hheight))
  print("Character eye color:", random.choice(Colors))
  print("Height:", random.choice(Height))
  print("Attire:", random.choice(attire))
  print(Fore.RED + "Note: Skin color uses the names of the colors relative to skin color. they may not be the same when context is changed.")
  print(Fore.WHITE + "Would you like to generate a new character? (type sure when your ready)")

Generate()
create = input()

#tells python what to refer to when create is mentioned



while create == "sure" or "Sure":
  print("Okay!")
  time.sleep(1)
  cls()
  time.sleep(1)
  Generate()
  input()

#checks for when create has a response and generates a response.

