"**************************SPY_CHAT*********************"



#IMPORTING IS HERE

import spy_details
from steganography.steganography import Steganography
from datetime import datetime



#CLASSES
class user:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class messages:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me


friend_one = user('yogesh', 'Mr.', 22,9)
friend_two = user('chinti', 'Ms.',19 , 6)
friend_three = user('Kajal', 'Ms.', 19, 8)


friends = [friend_one, friend_two, friend_three]       #LIST OF FRIENDS


# ADD STATUS FUNCTION
def add_status():

    updated_status_message = None

    if USER.current_status_message != None:

        print 'Your current status message is %s \n' % (USER.current_status_message)
    else:
        print 'You don\'t have any status message currently \n'

    default = raw_input("Do you want to select from the older status (y/n)? ")

    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set? ")


        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message
            print STATUS_MESSAGES

    elif default.upper() == 'Y':

        item_position = 1

        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("\nChoose from the above messages "))


        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    else:
        print 'The option you chose is not valid! Press either y or n.'

    if updated_status_message:
        print 'Your updated status message is: %s' % (updated_status_message)
    else:
        print 'You current don\'t have a status update'

    return updated_status_message



# ADD FRIEND FUNCTION
def add_friend():

    new_friend = user('','',0,0.0)

    new_friend.name = raw_input("Please add your friend's name: ")
    new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")

    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = raw_input("Age?")
    new_friend.age = int(new_friend.age)

    new_friend.rating = raw_input("Spy rating?")
    new_friend.rating = float(new_friend.rating)

    if len(new_friend.name) > 0 and new_friend.age > 12:
        friends.append(new_friend)
        print 'Friend Added!'
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

    return len(friends)



# SELECT FRIEND FUNCTION
def select_a_friend():
    item_number = 0

    for friend in friends:
        print '%d. %s %s aged %d with rating %.2f is online' % (item_number +1, friend.salutation, friend.name,friend.age,friend.rating)
        item_number = item_number + 1

    friend_choice = raw_input("Choose from your friends")

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position




#  SEND MESSAGE FUNCTION
def send_message():

    friend_choice = select_a_friend()

    original_image = raw_input("What is the name of the image?")
    output_path = "output.jpg"
    text = raw_input("What do you want to say? ")
    Steganography.encode(original_image, output_path, text)

    new_chat = messages(text,True)

    friends[friend_choice].chats.append(new_chat)

    print "Your secret message image is ready!"




# READ MESSAGE FUNCTION
def read_message():

    sender = select_a_friend()

    output_path = raw_input("What is the name of the file?")

    secret_text = Steganography.decode(output_path)

    new_chat = messages(secret_text,False)

    friends[sender].chats.append(new_chat)

    print "Your secret message has been saved!"



# READ CHAT HISTORY FUNCTION
def read_chat_history():

    read_for = select_a_friend()

    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print '[%s] %s: %s' % (chat.time.strftime("%d %B %Y"), 'You said:', chat.message)
        else:
            print '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), friends[read_for].name, chat.message)





# START CHAT FUNCTION
def start_chat(spy):

    USER.name = USER.salutation + " " + USER.name


    if USER.age > 12 and USER.age < 50:


        print "Authentication complete. Welcome " + USER.name + " age: " \
              + str(USER.age) + " and rating of: " + str(USER.rating) + " Proud to have you onboard"

        show_menu = True

        while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    USER.current_status_message = add_status()
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)
                elif menu_choice == 3:
                    send_message()
                elif menu_choice == 4:
                    read_message()
                elif menu_choice == 5:
                    read_chat_history()
                else:
                    show_menu = False
    else:
        print 'Sorry you have entered the age not in between 12 to 50 so you are not a valid user'







STATUS_MESSAGES = ['Busy','Working On Spy_Chat' ,'Hey there i am using spy-chat']
print "Hello! Let\'s get started"
USER=user('','',0,0.0)
USER.name=raw_input("Welcome to spy chat,Enter Your Name please:")
if spy_details.spy_name==USER.name:
    USER.age=spy_details.spy_age
    USER.rating=spy_details.spy_rating
    USER.salutation=spy_details.spy_salutation
    start_chat(USER)
else:

    if len(USER.name) > 0 and USER.name.isalpha():
        USER.salutation = raw_input("Should I call you Mr. or Ms.?: ")

        USER.age = raw_input("What is your age?")
        USER.age = int(USER.age)

        USER.rating = raw_input("What is your spy rating?")
        USER.rating = float(USER.rating)

        start_chat(USER)
    else:
        print 'Please add a valid spy name'