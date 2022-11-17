#Lucas Wenger
#Path Generator
#Created 18 Septenber 2020

import random

straightpath = "@|||||||||||||||@\n"
leftpath = "@///////////////@\n"
rightpath = "@\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\@\n"


def laytile(smoothness):
    global spacesfromstart
    global path
    smoothness = int(smoothness)
    pathtype = random.randint(1,3)
    if pathtype == 1:
        for j in range(smoothness):
            spacesfromstart -= 1
            path += " "*spacesfromstart + leftpath
    elif pathtype == 2:
        for j in range(smoothness):
            path += " "*spacesfromstart + straightpath
    elif pathtype == 3:
        for j in range(smoothness):
            spacesfromstart += 1
            path += " "*spacesfromstart + rightpath
        

def createpath(length, smoothness):
    global path
    for i in range(int(int(length)/int(smoothness))):
        laytile(smoothness)
    print(path)

while True:
    path = ''
    length = ''
    smoothness = ''
    spacesfromstart = 30
    while length.isdigit() == False or smoothness.isdigit() == False or smoothness == "0":
        length = input("How long would you like your path to be? Enter a positive integer.\n")
        smoothness = input("How smooth would you like your path to be? Enter a positive integer. \n")
    createpath(int(length),int(smoothness))
