import random
import time

responses = ["Yes", "No", "Maybe", "It is certain", "It is decidedly so", "Without a doubt", "You may rely on it" "Most likely", "Outlook good", "Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My sources say no", "Outlook not so good", "Very doubtful"]
keep_playing = True


def greeting():
    """Prompts user for their name, greets them"""

    name = raw_input("I see you've come to the magic 8 ball to tell your fortune, what is your name?\n")
    print
    print "hello {}!".format(name)
    print
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
            print show_magic_eightball()
            print "\n....shaking...\n"
            time.sleep(3)
            print(random.choice(responses))
            print
            if count == 5:
                print "You've used all 5 fortunes, good bye"


def closing(user_name):
    """Thanks user for playing"""

    print "Thank you {} for visiting the magic 8-ball".format(user_name)


def show_magic_eightball():
    """Shows the user a magic 8 ball ascii art"""

    return """
            ____
    ,dP9CGG88@b,
  ,IP  _   Y888@@b,
 dIi  (_)   G8888@b
dCII  (_)   G8888@@b
GCCIi     ,GG8888@@@
GGCCCCCCCGGG88888@@@
GGGGCCCGGGG88888@@@@...
Y8GGGGGG8888888@@@@P.....
 Y88888888888@@@@@P......
 `Y8888888@@@@@@@P'......
    `@@@@@@@@@P'.......
"""

def show_magic_eightball_opener():

    print """
    
          ......._
      .-:::::::::::-.
    .:::::::::::::::::.
   :::::::' .-. `:::::::
  :::::::  :   :  :::::::
 ::::::::  :   :  ::::::::
 :::::::::._`-'_.:::::::::
 :::::::::' .-. `:::::::::
 ::::::::  :   :  ::::::::
  :::::::  :   :  :::::::
   :::::::._`-'_.:::::::
    `:::::::::::::::::'
      `-:::::::::::-'
         `'''''''`
         """
def main():
    show_magic_eightball_opener()
    show_magic_eightball()
    user = greeting()
    show_magic_eightball()
    user_question()
    closing(user)

main()
    
