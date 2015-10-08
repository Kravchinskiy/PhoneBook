import PB_Functions as f
import PB_Classes as cl
import sys

#-----------------------------------------------------------------------------
#   Procedure variant
#-----------------------------------------------------------------------------
def main_proc():
    if len(sys.argv) > 1 :
        filename = sys.argv[1]
    else :
        filename = ""
    phone_list = {}
    f.load_data(filename, phone_list)
    cmd = -1                    # Need to think!
    while cmd != 0 :
        f.prompt()
        cmd = f.get_cmd()
        if cmd == 0 :           # Quit from program
            print("Phone Book is finished!")
        elif cmd == 1 :         # View PhoneBook
            f.numbers_list(phone_list)
            input()
        elif cmd == 2 :         # Lookup number by name
            print("Find a record")
            name = input("Input name: ")
            print("Phone number for ", name, " is ", f.lookup_number(phone_list, name))
            input()
        elif cmd == 3 :         # Add new number to PhoneBook
            print("Add new record")
            name = input("Input name: ")
            number = input("Input number: ")
            f.add_number(phone_list, name, number)
        elif cmd == 4 :         # Change number by name in PhoneBook
            print("Change the record")
            name = input("Input name: ")
            number = input("Input number: ")
            f.change_number(phone_list, name, number)
            input()
        elif cmd == 5 :         # Remove record by name from PhoneBook
            print("Delete the record")
            name = input("Input name: ")
            f.remove_number(phone_list, name)
            input()
        elif cmd == 6 :         # Save PhoneBook to file
            savename = filename
            yes = input("Save to file " + savename + " Y/N? ")
            if yes != "Y" and yes != "y" :
                filename = input("Input file name: ")
            if filename == "" :
                filename = savename
            f.save_data(filename, phone_list)
        elif cmd == 7 :         # Load new PhoneBook
            filename = input("Input file name: ")
            f.load_data(filename, phone_list)
        else :
            print("Unknown command")

# Object oriented variant
def main_oop() :
    if len(sys.argv) > 1 :
        filename = sys.argv[1]
    else :
        filename = "pbook.dat"
    phone_book = cl.PhoneBook(filename)
    phone_book.load_phone_book()
    while phone_book.cmd != 0 :
        phone_book.prompt()
        phone_book.get_cmd()
        if phone_book.cmd == 0 :        # quit from program
            continue
        elif phone_book.cmd == 1 :      # get list of phone numbers
            phone_book.numbers_list()
        elif phone_book.cmd == 2 :      # find number by name
            phone_book.find_number()
        elif phone_book.cmd == 3 :      # create new record in phone book
            phone_book.new_number()
        elif phone_book.cmd == 4 :      # change number by name
            phone_book.edit_number()
        elif phone_book.cmd == 5 :      # delete record by name from phonebook
            phone_book.delete_record()
        elif phone_book.cmd == 6 :      # save phone book to file
            if phone_book.status :
                phone_book.save_phone_book()
            else :
                print("Phone book wasn't changed!")
        elif phone_book.cmd == 7 :      # load new phone book
            filename = input("Input file name: ")
            phone_book = cl.PhoneBook(filename)
            phone_book.load_phone_book()
        else :
#            input("Unknown command")
            phone_book.msg = "Unknown command"
            phone_book.add_message()
#       output messages queue
        phone_book.print_messages()
        phone_book.clear_messages()

# two variants of main prog
def main() :
    if 1 == 1 :
        main_oop()
    else :
        main_proc()

main()