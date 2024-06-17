# --- OOP Email Simulator --- 


# --- Email Class --- #
class Email:
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    # Declare the class variable, with default value, for emails.
    has_been_read = False
    is_spam = False

    # Method to change 'has_been_read' emails from False to True.
    def mark_as_read(self):
        self.has_been_read = True

    # Method to change 'has_been_read' emails from True to False.
    def mark_as_unread(self):
        self.has_been_read = False

    # Method to change 'is_spam' emails from False to True.
    def mark_as_spam(self):
        self.is_spam = True

    # Method to change 'is_spam' emails from True to False.
    def mark_as_not_spam(self):
        self.is_spam = False
