### Importations

import json
import os
from time import sleep
from colorama import Fore, Back, Style

version = 'v0.1.0'

### functions

def clearScreen():
    #Taken from geeks for geeks cause im gay
    if (os.name == 'nt'):
        os.system('cls')
    else:
        os.system('clear')

# Display available characteristics
def printCharacteristics():
    print('Available Characteristics: \n')
    for index in range(len(inDat['_difficultyBeatmapSets'])):
        print(str(index + 1) + '. ' + inDat['_difficultyBeatmapSets'][index]['_beatmapCharacteristicName'])

def injectCustomData(listIndex, Title, Image):
    inDat['_difficultyBeatmapSets'][listIndex]['_customData'] = {}
    inDat['_difficultyBeatmapSets'][listIndex]['_customData']['_characteristicLabel'] = Title
    if not(Image == 'None'):
        inDat['_difficultyBeatmapSets'][listIndex]['_customData']['_characteristicIconImageFilename'] = Image


### Main Program starts here

# Load info.dat
try:
    infoDatRaw = open('Info.dat', 'r')
    inDat = json.loads(infoDatRaw.read())
    print('Loaded Info.dat')
    infoDatRaw.close()

    # Clears screen and prints title
    clearScreen()
    print(f'{Fore.BLUE}Scuffed {Fore.RED}B{Fore.BLUE}S Characteristic Editor ' + version + f'\n {Style.RESET_ALL}')

    selc = ''
    # selection while loop
    while not(selc.isnumeric() and (int(selc) >= 1) and (int(selc) <= len(inDat['_difficultyBeatmapSets']))):  
        printCharacteristics()
        selc = input('Select Characteristic: ')

        if not(selc.isnumeric()):
            print(f'{Fore.RED}\nYou must type a number{Style.RESET_ALL}')
        elif not((int(selc) >= 1) and (int(selc) <= len(inDat['_difficultyBeatmapSets']))):
            print(f'{Fore.RED}\nInput out of range{Style.RESET_ALL}')
    selc = int(selc) - 1

    # custom name
    clearScreen()
    ti = input('Please type out a characteristic title:\n')
    if_else = ''

    # custom image
    while not((if_else == 'yes') or (if_else == 'no')):
        if_else = input('Do you want to add an image? ')
        if not((if_else == 'yes') or (if_else == 'no')):
            print(f'{Fore.RED}Enter yes or no{Style.RESET_ALL}')
    if (if_else == 'yes'):
        im = input('Type out image name:\n')
    else:
        im = 'None'

    # Inject customData into characteristic
    injectCustomData(selc,ti,im)
    infoDatRaw = open('Info.dat', 'w')
    infoDatRaw.write(json.dumps(inDat, indent=2))
    infoDatRaw.close()
    print(f'{Fore.GREEN}\nCustomData injected into characteristic{Style.RESET_ALL}')
    input('Press Enter to continue')
except:
    print(f'{Fore.RED}Oops you broke it. You probably forgot to run this in a folder with info.dat\nIf not, then make a GitHub issue or contact me on Discord [dwmdotexe].\n{Style.RESET_ALL}')
    input('Press Enter to continue')
