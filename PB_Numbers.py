__author__ = 'harry'

#-----------------------------------------------------------------------------
#   Class for PhoneBook numbers
#-----------------------------------------------------------------------------
class PhoneBookNumbers :
    numbers = []    # List of PhoneBook number by name
    name = ""       # Name of client PhoneBook

#-----------------------------------------------------------------------------
#   Constructor
#-----------------------------------------------------------------------------
    def __init__(self, name):
        """
        Init object of PhoneBook numbers
        :param name: Client name
        :return: nothing
        """
        self.numbers = list()
        self.name = name

#-----------------------------------------------------------------------------
#   Add new number
#-----------------------------------------------------------------------------
    def add_number(self, number):
        """
        Add new number if it is not exist
        :param number: New phone number
        :return: nothing
        """
        if not number in self.numbers :
            self.numbers.append(number)

#-----------------------------------------------------------------------------
#   Delete numbers
#-----------------------------------------------------------------------------
    def del_number(self, number):
        """
        Remove number if it is exist in list
        :param number: Phone number
        :return: nothing
        """
        if number in self.numbers:
            self.numbers.remove(number)

#-----------------------------------------------------------------------------
#   Clear numbers
#-----------------------------------------------------------------------------
    def clear_numbers(self):
        """
        Erase all number from list
        :return: nothing
        """
        self.numbers.clear()

#-----------------------------------------------------------------------------
#   Get client name
#-----------------------------------------------------------------------------
    def get_name(self):
        """
        Get client name for object PhoneBookNumbers
        :return: string - client namr
        """
        return self.name

#-----------------------------------------------------------------------------
#   Get list of numbers
#-----------------------------------------------------------------------------
    def get_list(self):
        """
        Send phone numbers list
        :return: list - phone numbers
        """
        return self.numbers

#-----------------------------------------------------------------------------
#   Replace new number to old number
#-----------------------------------------------------------------------------
    def replace_number(self, old, new):
        """
        Replace new number to old number
        :param old: digital string
        :param new: digital string
        :return: nothing
        """
        self.numbers[old] = new
