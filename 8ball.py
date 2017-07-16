import random

responses = ["Yes", "No", "Maybe"]
keep_playing = True


def greeting():
    """Prompts user for their name, greets them"""

    name = raw_input("I see you've come to the magic 8 ball to tell your fortune, what is your name? ")
    print "hello {}!".format(name)
    return name


def user_question():
    """Prompts user for up to 5 questions"""

    count = 0
    while count < 5:
        question = raw_input("What questions do you have? Type 'exit' to stop playing\n")

        if question == 'exit':
            break
        else:
            count = count + 1
            print(random.choice(responses))
            if count == 5:
                print "You've used all 5 fortunes, good bye"


def closing(user_name):
    """Thanks user for playing"""

    print "Thank you {} for visiting the magic 8-ball".format(user_name)


def show_magic_eightball():
    """Shows the user a magic 8 ball ascii art"""

    pass


def show_crayons():

    print """
        ,'|`.
     _    _.-"-"`-.`. _
    |.`,-' .  .  . ".",|
    |C`:  . .  . . .,' |
    | R `._.  . . ,'   |
    |  A   |"-..-'     |
    |   Y  |C R A Y O N|
     `.  O |        _.-"
       `. N|    _.-"
         `.|_.
    """

def main():
    show_crayons()
    show_magic_eightball()
    user = greeting()
    show_magic_eightball()
    user_question()
    closing(user)

main()
    
