### Importations

import json
import os
from time import sleep
from colorama import Fore, Back, Style

version = 'v0.1.1'

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

#Disgusting thing
def convYesNoToBool(input):
    if input == 'yes':
        return True
    elif input == 'no':
        return False
    else:
        return 'input not valid'

### Main Program starts here


try:
    # setup stuff
    clearScreen()
    dir = input(f'{Fore.BLUE}Drag the unzipped Beat Saber Map into this terminal window then press enter: \n \n{Style.RESET_ALL}')
    dir.replace("'","")
    os.chdir(dir.replace('"',''))

    # Load info.dat
    infoDatRaw = open('Info.dat', 'r')
    inDat = json.loads(infoDatRaw.read())
    print('Loaded Info.dat')
    sleep(0.1)
    infoDatRaw.close() #Closes raw info.dat file

    # Clears screen and prints title
    clearScreen()
    print(f'{Fore.BLUE}Scuffed {Fore.RED}Beat {Fore.BLUE}Saber Characteristic Editor ' + version + f'\n {Style.RESET_ALL}')

    # selection while loop
    selc = ''
    while not(selc.isnumeric() and (int(selc) >= 1) and (int(selc) <= len(inDat['_difficultyBeatmapSets']))):  
        printCharacteristics()
        selc = input('Select Characteristic: ')

        if not(selc.isnumeric()):
            print(f'{Fore.RED}\nYou must type a number{Style.RESET_ALL}')
        elif not((int(selc) >= 1) and (int(selc) <= len(inDat['_difficultyBeatmapSets']))):
            print(f'{Fore.RED}\nSelection not valid{Style.RESET_ALL}')
    selc = int(selc) - 1

    # custom name
    clearScreen()
    ti = input('Please type out a characteristic title:\n')
    if_else = 0

    # custom image
    # What the fuck is with my coding kills
    while not(type(if_else)==bool):
        if_else = convYesNoToBool(input('Do you want to add an image? '))
        if not(type(if_else)==bool):
            print(f'{Fore.RED}Enter yes or no{Style.RESET_ALL}')
    if if_else:
        im = input('Type out the image filename:\n')
    else:
        im = 'None'

    # Inject customData into characteristic
    injectCustomData(selc,ti,im)
    infoDatRaw = open('Info.dat', 'w')
    infoDatRaw.write(json.dumps(inDat, indent=2))
    infoDatRaw.close()

    # Print out injection status
    print(f'{Fore.GREEN}\nCustomData injected into characteristic{Style.RESET_ALL}')
    input('Press Enter to continue')
except:
    print(f'{Fore.RED}Oops you broke it.\nPlease submit an issue to GitHub or contact me on Discord [dwmdotexe].\n{Style.RESET_ALL}')
    input('Press Enter to continue')
