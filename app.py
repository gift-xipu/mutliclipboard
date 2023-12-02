#how we run the app:

#py app.py save, to save to json file
#py app.py load, to load from json file
#py app.py list, to list all saved keys
# py app.py clear, to clear all saved

import sys
import clipboard
import json
from colorama import Fore, Style

# File name where we store data
SAVED_DATA = "items.json"

# Function to write data into the items.json file in JSON format
def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

# Function to load or read data from the items.json file that was saved
def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        # If the file is not found, return an empty dictionary
        return {}
    except json.JSONDecodeError:
        print(Fore.RED + "Error decoding JSON. Resetting data." + Style.RESET_ALL)
        # If there's a JSON decoding error, return an empty dictionary
        return {}

# Function to list all the keys in the data of the items.json file
def list_keys(data):
    if data:
        print("Keys in the data:")
        for key in data.keys():
            print("- " + key)
    else:
        print("No keys in the data.")

# Function that clears the clipboard content
def clear_clipboard():
    clipboard.copy("")
    print("Clipboard cleared.")

# Checks if the number of command-line arguments is 2.
# Assigns the second argument to the command variable.
# This is so we skip the app.py command and move to the one after it.
if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    # If the command is "save," prompts the user for a key, then saves the corresponding clipboard data.
    if command == "save":
        key = input("Enter a key: ").strip()
        if key:
            data[key] = clipboard.paste()
            save_data(SAVED_DATA, data)
            print(Fore.GREEN + "Data saved!" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Key cannot be empty." + Style.RESET_ALL)

    # If the command is "load," prompts the user for a key and copies the corresponding data to the clipboard if the key exists.
    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print(Fore.GREEN + "Data copied to clipboard." + Style.RESET_ALL)
        else:
            print(Fore.RED + "Key does not exist." + Style.RESET_ALL)

    # If the command is "list," prints the keys in the data.
    elif command == "list":
        list_keys(data)

    # If the command is "clear," clears the clipboard.
    elif command == "clear":
        clear_clipboard()

    else:
        print(Fore.YELLOW + "Unknown command." + Style.RESET_ALL)

else:
    print(Fore.RED + "Please pass exactly one command." + Style.RESET_ALL)
