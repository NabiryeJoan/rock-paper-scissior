#  First the program makes its desicion
# Here is also when the RANDOM & Time module 
# Gets used. After that is aske's 
# The user to choose its operation
# And then it compares the two
# to see who won!

# This is a variable that will always be true =>
import time
import random

i = True


# Here is when the while loop starts =>
while i == True:
    
    
    time.sleep(3)
    # ------------------------------
    # Here is how the bot chooses his operation.
    operations = ["rock", "paper", "sissers"]
    operation_choice = random.choice(operations)
    # ------------------------------


    # ------------------------------
    # Here is when the user get's asked
    # And then based on that the might win, lose
    # Or have a tie
    input_ = input("Choose: ")
    if input_ == "r":
        if operation_choice == "rock":
            print(f"I choose {operation_choice}")
            time.sleep(2)
            print("Looks like its a tie!")
        if operation_choice == "paper":
            print(f"I choose {operation_choice}")
            time.sleep(2)
            print("I won, HAHA")
        if operation_choice == "sissers":
            print(f"I choose {operation_choice}")
            time.sleep(2)
            print("I lost, I will defeat you next time!")

    elif input_ == "p":
        if operation_choice == "rock":
            print(f"I choose {operation_choice}")
            time.sleep(2)
            print("I lost, I will defeat you next time!")
        if operation_choice == "paper":
            print(f"I choose {operation_choice}")
            time.sleep(2)
            print("Looks like its a tie!")
        if operation_choice == "sissers":
            print(f"I choose {operation_choice}")
            time.sleep(2)
            print("I won! HAHA")

    elif input_ == "s":
        if operation_choice == "rock":
            print(f"I choose {operation_choice}")
            time.sleep(2)
            print("I won! HAHA")
        if operation_choice == "paper":
            print(f"I choose {operation_choice}")
            time.sleep(2)
            print("I lost! I will defeat you next time!")
        if operation_choice == "sissers":
            print(f"I choose {operation_choice}")
            time.sleep(2)
            print("Looks like its a tie!")

        # ------------------------------


        # ------------------------------
        # If the user doesnt enter the right words
        # Then this program gets executed
        # This is great because normally
        # It would yell at them.
    else:
        print("Hmm... I dont get what you are saying")
        time.sleep(2)
        print('''
    Here are the keys:

    For rock: r
    For paper: p
    For sissers: s

    ''')
        # ------------------------------
# ----------------------------------------