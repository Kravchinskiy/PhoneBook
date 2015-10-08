__author__ = 'Kravchinskiy.IV'

import os

#----------------------------------------------------
#   .draw user menu
#----------------------------------------------------
def prompt():
    os.system('cls')
    print("PhoneBook v.0.1")
    print("Next operation is avalaible:")
    print("1. List of records")
    print("2. Find a record")
    print("3. Add new record")
    print("4. Change the record")
    print("5. Delete the record")
    print("6. Save the changes")
    print("7. Load PhoneBook file")
    print("0. Exit")
    print()

#----------------------------------------------------
#   .load data from file
#----------------------------------------------------
def load_data(filename, data) :
    if filename != "" :
        try :
            in_file = open(filename, 'r')
        except FileNotFoundError :
            print("Error open file: ", filename)
            input()
            return
        data.clear()
        while True :    # read data from file
            in_line = in_file.readline()
            if not in_line :
                break
            in_line = in_line[:-1]
            name, number = in_line.split(";")
            add_number(data, name, number)
        in_file.close()
    else :
        print("Phone Book not found")
        input()

#----------------------------------------------------
#   .save data to file
#----------------------------------------------------
def save_data(filename, data) :
    try :
        out_file = open(filename, 'w')
    except FileExistsError :
        print("File already exist ", filename)
        print()
        return
    for name in data :
        out_file.write(name + ";" + data[name] + "\n")
    out_file.close()

#----------------------------------------------------
#   .add number by name
#----------------------------------------------------
def add_number(data, name, number) :
    if not number.isdigit() :
        print("Invalid number ", number)
        return
    if name in data :
        print("Record for ", name, " is exist.")
        yes = input("Replace it? Y/N ")
        if yes == "Y" or yes == "y" :
            data[name] = number
    else :
        data[name] = number

#----------------------------------------------------
#   .show list of number with names
#----------------------------------------------------
def numbers_list(data):
    os.system('cls')
    print("Phone numbers: ")
    for name in data.keys() :
        print("Name: ", name, "\tNumber: ", data[name])
    print()

#----------------------------------------------------
#   .get user command
#----------------------------------------------------
def get_cmd():
    cmd = input("Your command: ")
    os.system('cls')
    if cmd.isdigit() :
        return int(cmd)
    else :
        return -1

#----------------------------------------------------
#   .find number by name
#----------------------------------------------------
def lookup_number(data, name) :
    if name in data :
        return data[name]
    else :
        return "Invalid name"


#----------------------------------------------------
#   .remove name from phone book
#----------------------------------------------------
def remove_number(data, name) :
    if name in data :
        del data[name]
        print("Number for ", name, " is deleted.")
    else :
        print("Invalid name:", name)

#----------------------------------------------------
#   .change number by name
#----------------------------------------------------
def change_number(data, name, number) :
    if not number.isdigit() :
        print("Invalid number ", number)
        return
    if name in data :
        data[name] = number
        print("Number for ", name, " is changed to ", number)
    else :
        print("Invalid name:", name)
