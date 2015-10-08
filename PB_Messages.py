__author__ = 'harry'

#-----------------------------------------------------------------------------
#   Class for collect and output messages, which make
#   in PhoneBook class methods
#-----------------------------------------------------------------------------
class Messages:
    messages = []   # Messages queue
    msg = ""        # Single message

#-----------------------------------------------------------------------------
#   Constructor
#-----------------------------------------------------------------------------
    def __init__(self):
        """
        Prepare messages queue. Create new queue
        :return: nothing
        """
        self.messages = list()

#-----------------------------------------------------------------------------
#   Add message to queue
#-----------------------------------------------------------------------------
    def add_message(self):
        """
        Append message to queue
        :return: nothing
        """
        self.messages.append(self.msg)

#-----------------------------------------------------------------------------
#   Clear queue of messages
#-----------------------------------------------------------------------------
    def clear_messages(self):
        """
        Create empty queue
        :return: nothing
        """
        self.messages.clear()

#-----------------------------------------------------------------------------
#   Output messages from queue
#-----------------------------------------------------------------------------
    def print_messages(self):
        """
        Output messages from queue to screen
        :return: nothing
        """
        for message in self.messages :
            print(message)
        input("Press Enter to continue...")
