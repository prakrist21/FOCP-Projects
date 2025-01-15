# Importing required modules
import random
import json
import datetime

def load_files():
# This function loads json file and conversation file and stores it on 'dict' and 'f1' respectively
    global dict,f1
    try:
        with open('dict.json') as f:
            dict=json.load(f) 
    except:
        print("Required files not found.")

    f1=open("conversation.txt","a")

def input_name():
# This function asks the user's name and displays it
    global name
    name=input("Enter your name: ")
    print(f"{name}, Welcome to Chatbot. You can ask anything about our college.")


def user_agent():
# This function randomly chooses a agent and displays it
    agent=['Alex','John','Jimmy','Ryan','Denis','Roger']
    useragent=random.choice(agent)
    print(f"Hello, I am your agent {useragent}")

def date():
# This function returns the current date and time
    time=datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")
    return time

def randomly_disconnect():
# This function randomly disconnects the program with 10% chance.
    disconnect=random.randint(1,100)  
    if disconnect<=10:                  
        print("Sorry, network disconnected !!!")
        f1.write(f"{date()} Sorry, network disconnected !!!\n\n")
        quit()

def bye():
# This function says goodbye to the user and saves the message to a file.
    bye=f"Bye {name}! It was nice talking with you."
    print(bye)
    f1.write(f"{date()} Answer: {bye}\n\n")

def chatbot(choice):
# This function replies according to the user's questions and ends when the user types 'bye'.
    while choice != 'bye':
        randomly_disconnect()  # Function call for randomly disconnect
        
        # Split the user's input into words and find matches in the JSON keys
        lst=set([x for x in choice.split(' ')])
        keys=set(dict.keys())

        # If a matching keyword is found, respond with a random answer from the JSON file
        if lst.intersection(keys) != set():
            key=list(lst.intersection(keys))
            lst1=set(dict[key[0]].keys())
            key1=list(lst1.intersection(lst))   
            # If a specific sub-key is found
            if key1 != []:
                answer=random.choice(dict[key[0]][key1[0]])
                f1.write(f"{(date())} Answer: {answer}\n")
                print("Chatbot: ",answer)
            else:
            ## If no specific sub-key is found, ask the user to be more specific
                lst_keywords=list(dict[key[0]].keys())
                answer=f"What do you want to know about {key[0]}. Try be more specific like {key[0]} {f', {key[0]} '.join(lst_keywords)}."
                print(answer)
                choice=input("Enter again or use 'bye' to exit: ")
                f1.write(f"{(date())} Answer: {answer}\n")
                f1.write(f"{(date())} Question: {choice}\n")
                continue # Continue to the next iteration of the loop
        else: 
            # If no keyword matches, respond with a default "no reply" message
            answer=random.choice(dict['noreply'])
            print(f"Chatbot: Sorry {name}, {answer}")
            f1.write(f"{date()} Answer: Sorry {name}, {answer}\n")

        # Ask for the next question or allow the user to exit
        choice=input("Ask another question to Chatbot or use 'bye' to exit: ").lower()
        f1.write(f"{date()} Question: {choice}\n")
        
    # Say goodbye when the user exits
    bye()


# Loading files and calling the necessary functions
load_files()
input_name()
user_agent()

choice=input("Ask Chatbot: ").lower()
f1.write(f"{date()} Question: {choice}\n")


# Run the chatbot function with the user's input when the script is executed directly
if __name__=="__main__":
    chatbot(choice)

# Closing the conversation file
f1.close()


