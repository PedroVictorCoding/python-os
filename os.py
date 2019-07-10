import speech_recognition as sr
from PIL import Image, ImageEnhance
import socket
import os
import sys
import time
from datetime import datetime, timezone
import pytz
import pafy
import vlc

# import tkinter as tk


# Window Start
'''
window = tk.Tk()
window.title('Volto')
window.configure()
'''
version = "1.0"


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


image1 = Image.open('picture.jpeg')

width, height = image1.size

# Window size

error_word = " Couldn't find any edit"

r = sr.Recognizer()
audio = sr.AudioFile('bw.flac')

with audio as source:
    audioData = r.record(source)
type(audioData)
# text = r.recognize_google(audioData)
text = input(" What do you want to do: ")
print(" You said: " + text)
if len(text) < 1:
    print("   ")
    print(bcolors.OKBLUE + " These are not the droids you are looking for" + bcolors.ENDC)
    print(bcolors.WARNING + " Try typing a little more" + bcolors.ENDC)
    print("   ")


def black_and_white_convert():
    print("   ")
    print(bcolors.OKGREEN + " Action: Turn Image Into Black and White" + bcolors.ENDC)
    print("   ")
    image_from_user = input(
        bcolors.OKBLUE + " What is the file name of the picture? (make sure to add extension like '.jpeg'): " + bcolors.ENDC)
    print("   ")
    new_image = Image.open(image_from_user)
    image_convert = new_image.convert('L')
    file_naming = input(
        bcolors.OKBLUE + " Set the name of the file (make sure to add extension like '.jpeg'): " + bcolors.ENDC)
    image_convert.save(file_naming)
    print("   ")
    print(bcolors.HEADER + " Image Saved Successfully As " + file_naming + bcolors.ENDC)
    print(bcolors.HEADER + " Loading " + file_naming + bcolors.ENDC)
    print("   ")
    print(bcolors.OKGREEN + " Action Completed" + bcolors.ENDC)
    print("   ")
    image_convert.show()


def increase_contrast_1():
    print("   ")
    print(bcolors.OKGREEN + " Action: Increase Contrast by 1" + bcolors.ENDC)
    print("   ")
    image_from_user = input(
        bcolors.OKBLUE + " What is the file name of this picture? (make sure to add extension like '.jpeg'): " + bcolors.ENDC)
    print("   ")
    new_image = Image.open(image_from_user)
    image_convert = ImageEnhance.Contrast(new_image).enhance(1)
    file_naming = input(
        bcolors.OKBLUE + " Set the name of the file (make sure to add extension like '.jpeg'): " + bcolors.ENDC)
    image_convert.save(file_naming),
    print("   ")
    print(bcolors.HEADER + " Image Saved Successfully As " + file_naming + bcolors.ENDC)
    print(bcolors.HEADER + " Loading " + file_naming + bcolors.ENDC)
    print("   ")
    image_convert.show()


def increase_contrast_2():
    print("   ")
    print(bcolors.OKGREEN + " Action: Increase Contrast by 2" + bcolors.ENDC)
    print("   ")
    image_from_user = input(
        bcolors.OKBLUE + " What is the file name of this picture? (make sure to add extension like '.jpeg'): " + bcolors.ENDC)
    print("   ")
    new_image = Image.open(image_from_user)
    image_convert = ImageEnhance.Contrast(new_image).enhance(2)
    file_naming = input(
        bcolors.OKBLUE + " Set the name of the file (make sure to add extension like '.jpeg'): " + bcolors.ENDC)
    image_convert.save(file_naming),
    print("   ")
    print(bcolors.HEADER + " Image Saved Successfully As " + file_naming + bcolors.ENDC)
    print(bcolors.HEADER + " Loading " + file_naming + bcolors.ENDC)
    print("   ")
    image_convert.show()


def increase_contrast_3():
    print("   ")
    print(bcolors.OKGREEN + " Action: Increase Contrast by 3" + bcolors.ENDC)
    print("   ")
    image_from_user = input(
        bcolors.OKBLUE + " What is the file name of this picture? (make sure to add extension like '.jpeg'): " + bcolors.ENDC)
    print("   ")
    new_image = Image.open(image_from_user)
    image_convert = ImageEnhance.Contrast(new_image).enhance(3)
    file_naming = input(
        bcolors.OKBLUE + " Set the name of the file (make sure to add extension like '.jpeg'): " + bcolors.ENDC)
    image_convert.save(file_naming),
    print("   ")
    print(bcolors.HEADER + " Image Saved Successfully As " + file_naming + bcolors.ENDC)
    print(bcolors.HEADER + " Loading " + file_naming + bcolors.ENDC)
    print("   ")
    image_convert.show()


def increase_contrast_4():
    print("   ")
    print(bcolors.OKGREEN + " Action: Increase Contrast by 4" + bcolors.ENDC)
    print("   ")
    image_from_user = input(
        bcolors.OKBLUE + " What is the file name of this picture? (make sure to add extension like '.jpeg'): " + bcolors.ENDC)
    print("   ")
    new_image = Image.open(image_from_user)
    image_convert = ImageEnhance.Contrast(new_image).enhance(4)
    file_naming = input(
        bcolors.OKBLUE + " Set the name of the file (make sure to add extension like '.jpeg'): " + bcolors.ENDC)
    image_convert.save(file_naming),
    print("   ")
    print(bcolors.HEADER + " Image Saved Successfully As " + file_naming + bcolors.ENDC)
    print(bcolors.HEADER + " Loading " + file_naming + bcolors.ENDC)
    print("   ")
    image_convert.show()


def increase_contrast_5():
    print("   ")
    print(bcolors.OKGREEN + " Action: Increase Contrast by 5" + bcolors.ENDC)
    print("   ")
    image_from_user = input(
        bcolors.OKBLUE + " What is the file name of this picture? (make sure to add extension like '.jpeg'): " + bcolors.ENDC)
    print("   ")
    new_image = Image.open(image_from_user)
    image_convert = ImageEnhance.Contrast(new_image).enhance(5)
    file_naming = input(
        bcolors.OKBLUE + " Set the name of the new file (make sure to add extension like '.jpeg'): " + bcolors.ENDC)
    image_convert.save(file_naming),
    print("   ")
    print(bcolors.HEADER + " Image Saved Successfully As " + file_naming + bcolors.ENDC)
    print(bcolors.HEADER + " Loading " + file_naming + bcolors.ENDC)
    print("   ")
    image_convert.show()


def timezones():
    utc_dt = datetime.now(timezone.utc)

    pst = pytz.timezone('US/Pacific')
    ist = pytz.timezone('Asia/Jerusalem')
    pt = pytz.timezone('Europe/Lisbon')
    fr = pytz.timezone('Europe/Paris')
    ny = pytz.timezone('America/New_York')

    print(bcolors.OKGREEN + "   ")
    print(" UTC time     {}".format(utc_dt.isoformat()))
    print(" Local time   {}".format(utc_dt.astimezone().isoformat()))
    print(" Pacific time {}".format(utc_dt.astimezone(pst).isoformat()))
    print(" Israeli time {}".format(utc_dt.astimezone(ist).isoformat()))
    print(" Lisbon time {}".format(utc_dt.astimezone(pt).isoformat()))
    print(" Paris time {}".format(utc_dt.astimezone(fr).isoformat()))
    print(" New York time {}".format(utc_dt.astimezone(ny).isoformat()))
    print("   " + bcolors.ENDC)


if any(i in text for i in ["delete", "file"]):
    print("   ")
    file_delete_removal = input(
        bcolors.OKGREEN + " Name the file that you want to remove (add file extension like .jpeg): " + bcolors.ENDC)
    if len(file_delete_removal) > 2:
        os.remove(file_delete_removal)
    else:
        print(bcolors.WARNING + " Nothing to be deleted: " + bcolors.ENDC)

if "time" in text or "timezones" in text:
    timezones()

if "IP" in text or "ip" in text:
    print(bcolors.OKBLUE + "\n Your IP Address is: ", end="" + bcolors.ENDC)
    print(bcolors.OKGREEN + socket.gethostbyname(socket.gethostname()) + bcolors.ENDC)
    print("   ")

if any(i in text for i in ["remove", "data"]):
    start_time_remove_data = time.time()
    print("   ")
    print(" Info: Whenever you edit an image it automatically removes any data (exif)")
    print("   ")
    image_from_user_remove = input(
        bcolors.OKBLUE + " What is the file name of this picture? (make sure to add extension like '.jpeg'): " + bcolors.ENDC)
    print("   ")
    if len(image_from_user_remove) < 1:
        print(bcolors.OKBLUE + " These are not the droids you are looking for" + bcolors.ENDC)
        print(bcolors.WARNING + " Try typing more" + bcolors.ENDC)
    else:
        file_naming_remove = input(
            bcolors.OKBLUE + " Set the name of the new file (make sure to add extension like '.jpeg'): " + bcolors.ENDC)
        if len(file_naming_remove) < 1:
            print(bcolors.OKBLUE + " These are not the droids you are looking for" + bcolors.ENDC)
        else:
            image_remove_data = Image.open(image_from_user_remove).save(file_naming_remove)
            print(" Data was remove from you image")
            print("   ")
            print("---It took you %s seconds to remove the data from this Image---" % (
                    time.time() - start_time_remove_data))
            print("   ")


def add_xy():
    x = int(input(bcolors.OKBLUE + " Enter first number: " + bcolors.ENDC))
    print("   ")
    y = int(input(bcolors.OKBLUE + " Enter second number: " + bcolors.ENDC))
    z = x + y
    print("   ")
    print(" Ans: " + str(z))
    print("   ")


def subtract_xy():
    x = int(input(bcolors.OKBLUE + " Enter first number: " + bcolors.ENDC))
    print("   ")
    y = int(input(bcolors.OKBLUE + " Enter second number: " + bcolors.ENDC))
    z = x - y
    print("   ")
    print(" Ans: " + str(z))
    print("   ")


def multiply_xy():
    x = int(input(bcolors.OKBLUE + " Enter first number: " + bcolors.ENDC))
    print("   ")
    y = int(input(bcolors.OKBLUE + " Enter second number: " + bcolors.ENDC))
    z = x * y
    print("   ")
    print(" Ans: " + str(z))
    print("   ")


def division_xy():
    x = int(input(bcolors.OKBLUE + " Enter first number: " + bcolors.ENDC))
    print("   ")
    y = int(input(bcolors.OKBLUE + " Enter second number: " + bcolors.ENDC))
    z = x / y
    print("   ")
    print(" Ans: " + str(float(z)))
    print("   ")


def multiples_xy():
    pass


if 'calculator' in text or 'calc' in text:
    print(bcolors.OKGREEN + " Mathematical operations available: ")
    print(" 1- Add; ")
    print(" 2- Subtract;")
    print(" 3- Multiply;")
    print(" 4- Divide;")
    print(" 5- Multiples;")
    print(" 6- More coming" + bcolors.ENDC)
    operation = input(" Choose an operation (pick a number): ")
    if "1" in operation:
        add_xy()
    elif "2" in operation:
        subtract_xy()
    elif "3" in operation:
        multiply_xy()
    elif "4" in operation:
        division_xy()
    elif "5" in operation:
        multiples_xy()

if '-v' in text or 'version' in text:
    print(" You are in the version: " + version)
    print(" UPDATE: Check the Github repository to see if you are in the current version")
    print("   ")

if '-h' in text or 'help' in text:
    print("   ")
    print(bcolors.OKGREEN + " Action: Show Help")
    print("   ")
    print(" Program made by Pedro Victor, using many Awesome Python Libraries")
    print("                 _                _      _             ")
    print("                | |              (_)    | |            ")
    print("  _ __   ___  __| |_ __ _____   ___  ___| |_ ___  _ __ ")
    print(" | '_ \ / _ \/ _` | '__/ _ \ \ / / |/ __| __/ _ \| '__|")
    print(" | |_) |  __/ (_| | | | (_) \ V /| | (__| || (_) | |   ")
    print(" | .__/ \___|\__,_|_|  \___/ \_/ |_|\___|\__\___/|_|   ")
    print(" | | ")
    print(" |_| ")
    print("   ")
    print(" -h || help - Shows all the available commands")
    print("   ")
    print(" -q || quit - Closes the program")
    print("   ")
    print(" -r || restart - Restarts the program")
    print("   ")
    print(" -v || version - Shows the current software version")
    print("   ")
    print(" -c || clear - Cleans the page")
    print("   ")
    print(" -env || environment - Enters clean environment mode")
    print("   ")
    print("Delete files - Write a sentence with 'delete' and 'file' to remove file (you may use '../' before the file "
          "name to get out of the program's folder, use this as many times as needed)")
    print("   ")
    print(" Image Editing:")
    print("   ")
    print(" Black and White - Type the words 'black' and 'white' in a sentence to edit image")
    print("   ")
    print(" Increase contrast n - Write a sentence with the words 'increase' and 'contrast' plus a number between 1-5 "
          " to edit image")
    print("   ")
    print(" Remove EXIF data - Write a sentence with the words 'remove' and 'contrast' to remove data PS: Every time "
          "you edit an image the data is removed")
    print("   ")
    print(" Internet Tools:")
    print("   ")
    print(" Write a phrase with 'IP' (or ip) to retrieve your IP Address")
    print("   ")
    print(" Science Tools:")
    print("   ")
    print(" Calculator - Write a sentence with the word 'calculator' to do math")
    print("   ")
    print("Time and Timezones - Write a sentence with either 'time' or 'timezones' to get or time and timezones "
          "around the globe")
    print("   ")
    print(" ")
    print("   ")
    print(" More Tools to Come - Send some recommendations in the github repo" + bcolors.ENDC)
    print("   ")
    os.execl(sys.executable, sys.executable, *sys.argv)

if '-q' in text or 'quit' in text:
    print(bcolors.WARNING + " You are quiting the program!")
    print(" To reopen type 'python3 instance.py'" + bcolors.ENDC)
    print("   ")
    sys.exit()

if '-c' in text or 'clear' in text:
    os.system('clear')

if '-r' in text or 'restart' in text:
    print("   ")
    print(bcolors.WARNING + " You are restarting the program" + bcolors.ENDC)
    print("   ")
    os.execl(sys.executable, sys.executable, *sys.argv)

if '-env' in text or 'environment' in text:
    os.system('clear')

# Search for specific terms
if 'black' and 'white' in text:
    start_time = time.time()
    black_and_white_convert()
    print("---It took you %s seconds to edit this Image---" % (time.time() - start_time))
    print("   ")


# Creates a function when finds the common terms | Also My First Def/ Function in Python
def increase_contrast_num():
    # After Searching common terms search for individual term
    if any(i in text for i in ["1"]):
        increase_contrast_1()

    # After Searching common terms search for individual term
    if any(i in text for i in ["2"]):
        increase_contrast_2()

    # After Searching common terms search for individual term
    if any(i in text for i in ["3"]):
        increase_contrast_3()

        # After Searching common terms search for individual term
    if any(i in text for i in ["4"]):
        increase_contrast_4()

        # After Searching common terms search for individual term
    if any(i in text for i in ["5"]):
        increase_contrast_5()


# Searches for term in common
if any(i in text for i in ["increase", "contrast"]):
    start_time = time.time()
    increase_contrast_num()
    print("---It took you %s seconds to edit this Image---" % (time.time() - start_time))
    print("   ")

if "play" in text:
    url = "https://www.youtube.com/watch?v=mfI1S0PKJR8"
    vlc.Instance().media_player_new().set_media(vlc.Instance().media_new(pafy.new(url).getbest().url).get_mrl()).play()

# Reruns Program
os.execl(sys.executable, sys.executable, *sys.argv)

# TODO Tkinter not working

