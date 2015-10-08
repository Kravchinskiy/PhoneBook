__author__ = 'Kravchinskiy.IV'
import os
import PB_Messages as msg
import PB_Numbers as num


#-----------------------------------------------------------------------------
#  Main class - PhoneBook - array of client names and their phone numbers
#-----------------------------------------------------------------------------
class PhoneBook (msg.Messages):
    """
    Main class - PhoneBook - array of client names and their phone numbers
    """
    filename = ""   # file name of phone book
    numbers = []    # list of numbers objects
    cmd = -1        # user command
    status = False  # status of list True - changed, False - not

#-----------------------------------------------------------------------------
#   Constructor of PhoneBook
#-----------------------------------------------------------------------------
    def __init__(self, filename):
        """
        Init PhoneBook object, save data file name as attribute,
        clear messages queue and client names list
        :param filename: File name of PhoneBook data
        :return:
        """
        self.filename = filename    # file name with PhoneBook data
        self.clear_messages()       # messages clear direct!
        self.names = list()         # array of client names

#-----------------------------------------------------------------------------
#   Destructor of PhoneBook
#-----------------------------------------------------------------------------
    def __del__(self):
        """
        Check status of PhoneBook data. If data is changed,
        then try to save their. After clear all variables of PhoneBook
        :return: nothing
        """
        if self.status:
            yes = input("Save changes? Y/N ")
            if yes == "Y" or yes == "y" :
                self.save_phone_book()
#        self.data.clear()
        for element in self.numbers:
            element.clear_numbers()
        self.filename = ""
        self.clear_messages()

#-----------------------------------------------------------------------------
#   Check name in PhoneBook
#-----------------------------------------------------------------------------
    def check_name(self, name, with_msg = True):
        """
        Check name in PhoneBook
        :param name: Name of client PhoneBook
        :return: boolean
        """
        for element in self.numbers:
            if element.get_name() == name:
                return True
        if with_msg:
            self.msg = "Invalid name " + name
            self.add_message()
        return False

#-----------------------------------------------------------------------------
#   Add new name to PhoneBook
#-----------------------------------------------------------------------------
    def add_new_name(self, name):
        """
        Add new name to PhoneBook
        :param name: Name of client PhoneBook
        :return: nothing
        """
        self.numbers.append(num.PhoneBookNumbers(name))

#-----------------------------------------------------------------------------
#   Add new number by name to PhoneBook for new version
#-----------------------------------------------------------------------------
    def add_new_number(self, name, number):
        """
        Find PhoneBook record by name and add phone number,
        if it is not exist/
        :param name: Name of client PhoneBook
        :param number: New phone number
        :return: nothing
        """
        for element in self.numbers:
            if element.get_name() == name:
                element.add_number(number)

#-----------------------------------------------------------------------------
#   Add number to phone book to PhoneBook
#-----------------------------------------------------------------------------
    def add_number(self, name, number):
        """
        New variant for multi phone numbers.
        In the beginning check valid phone number.
        Then check client name. If name is not exist, create record.
        Then add new phone number to record by client name.
        PhoneBook status mark as changed.
        :param name: Name of client PhoneBook
        :param number: New phone number
        :return: nothing
        """
        if not number.isdigit():
            self.msg = "Invalid number " + number
            self.add_message()
            return
        if not self.check_name(name, False):
            self.add_new_name(name)
        self.add_new_number(name, number)
        self.status = True          # status changed

#-----------------------------------------------------------------------------
#   Load data to PhoneBook from file
#-----------------------------------------------------------------------------
    def load_phone_book(self):
        """
        Load data to PhoneBook from file. Open file as object attribute
        in read mode and load data to PhoneBook object.
        In case error message push to queue.
        Set PhoneBook status to not changed (False). File has closed.
        :return: nothing
        """
        if self.filename != "":
            try:
                in_file = open(self.filename, 'r')
            except FileNotFoundError:
                self.msg = "Error open file: " + self.filename
                self.add_message()
                return
#            self.data.clear()
            for element in self.numbers:
                element.clear_numbers()
            self.numbers.clear()
            while True:         # Read data from file
                in_line = in_file.readline()
                if not in_line:
                    break
                in_line = in_line[:-1]
                name, number = in_line.split(";")
                self.add_number(name.strip(), number.strip())
            in_file.close()
            self.status = False     # not changed status
        else:
            self.msg = "Phone Book not found"
            self.add_message()

#-----------------------------------------------------------------------------
#   Save data of PhoneBook to file
#-----------------------------------------------------------------------------
    def save_phone_book(self):
        """
        Save data of PhoneBook to file. Open file as object attribute
        in write mode and save all records of PhoneBook to it.
        In case error message push to queue.
        Set PhoneBook status to not changed (False). File has closed.
        :return: nothing
        """
        try:
            out_file = open(self.filename, 'w')
        except FileExistsError:
            self.msg = "File already exist " + self.filename
            self.add_message()
            self.msg = ""
            self.add_message()
            return
        for element in self.numbers:
            phones = element.get_list()
            for number in phones:
                self.msg = element.get_name() + ";" + number + "\n"
                out_file.write(self.msg)
        out_file.close()
        self.status = False

#-----------------------------------------------------------------------------
#   Get user command
#-----------------------------------------------------------------------------
    def get_cmd(self):
        """
        Get user command and return it as integer
        If user command is wrong then return unknown command (-1)
        :return: Integer
        """
        cmd = input("Your command: ")
        os.system('cls')
        if cmd.isdigit():
            self.cmd = int(cmd)
        else:
            self.cmd = -1
        return self.cmd

#-----------------------------------------------------------------------------
#   Draw user menu (prompt)
#-----------------------------------------------------------------------------
    def prompt(self):
        """
        Draw user menu (prompt)
        :return: nothing
        """
        os.system('cls')
        print("PhoneBook v.0.2")
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

#-----------------------------------------------------------------------------
#   Show list of names with phone numbers
#-----------------------------------------------------------------------------
    def numbers_list(self):
        """
        Output list for all phone numbers for all client names from PhoneBook
        Scan loaded PhoneBook and all records push to messages queue.
        New variant for multi phone numbers.
        :return: nothing
        """
        os.system('cls')
        self.msg = "Phone numbers: "
        self.add_message()
        for element in self.numbers:
            phones = element.get_list()
            for number in phones:
                self.msg = "Name: " + element.get_name() + "\tNumber: " + number
                self.add_message()
            self.msg = ""
            self.add_message()

#-----------------------------------------------------------------------------
#   Lookup number by name (Old version)
#-----------------------------------------------------------------------------
    def lookup_number(self, name):
        """
        2. Variant for multi numbers for each name
        If record for client name is exist, then return list of numbers
        otherwise push error message to queue
        :param name: Client name
        :return: string or list!!! This is ERROR
        """
        if not self.check_name(name):
            return
        for element in self.numbers:
            if element.get_name() == name:
                return element.get_list()

#-----------------------------------------------------------------------------
#   Get client name and lookup number by name
#-----------------------------------------------------------------------------
    def find_number(self):
        """
        Get client name and lookup number by name. Two variants:
        New variant for multi phone numbers.
        In the beginning get client name and check it.
        If record of PhoneBook with this name is exist then push all numbers
        to message queue.
        :return: nothing
        """
        print("Find a record")
        name = input("Input name: ")
        if not self.check_name(name):
            return
        for element in self.numbers:
            if element.get_name() == name:
                phones = element.get_list()
                for number in phones:
                    self.msg = "Phone number for " + name + " is " + number
                    self.add_message()

#-----------------------------------------------------------------------------
#   Create new record in PhoneBook
#-----------------------------------------------------------------------------
    def new_number(self):
        """
        Create new record in phone book
        :return: nothing
        """
        print("Add new record")
        name = input("Input name: ")
        number = input("Input number: ")
        self.add_number(name, number)

#-----------------------------------------------------------------------------
#   Edit record of phonebook
#-----------------------------------------------------------------------------
    def edit_number(self):
        """
        Edit record of PhoneBook. New variant for multi phone numbers.
        In the beginning get client name and check it.
        If record of PhoneBook with this name is exist,
        then get old phone number and search it. If old phone number is exist
        then get new number and replace it. If client name, old or new number
        is invalid, then create message in queue and break method.
        :return: nothing
        """
        name = input("Input name: ")
        if not self.check_name(name):
            return
        old_num = input("Input old number: ")
        for element in self.numbers:
            if element.get_name() == name:
                phones = element.get_list()
                if not old_num in phones:
                    self.msg = "Invalid old number " + old_num
                    self.add_message()
                    return
                new_num = input("Input new number: ")
                if new_num == "":
                    self.msg = "Invalid new number " + new_num
                    self.add_message()
                    return
                element.replace_number(old_num, new_num)

#-----------------------------------------------------------------------------
#   Delete record from PhoneBook by name
#-----------------------------------------------------------------------------
    def delete_record(self):
        """
        Remove record from PhoneBook by client name.
        In the beginning get client name, if record with this name is exist,
        then delete it from PhoneBook
        :return: nothing
        """
        name = input("Input name: ")
        for idx in range(len(self.numbers)):
            element = self.numbers[idx]
            if element.get_name() == name:
                self.msg = "Record for: " + name + " will be delete."
                if self.get_sure(self.msg):
                    del self.numbers[idx]
                    self.msg = "Record for: " + name + " was deleted."
                    self.add_message()
                return

#-----------------------------------------------------------------------------
#   Get sure from user
#-----------------------------------------------------------------------------
    def get_sure(self, question):
        """
        Get sure from user. True if sure, False if not
        :return: boolean
        """
        if question != "":
            print(question)
        answer = input("Are you sure? Y/N ")
        if answer == "Y" or answer == "y":
            return True
        else:
            return False