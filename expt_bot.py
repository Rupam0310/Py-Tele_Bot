
# Importing all the necessary modules required for bot processing
# contains the API key provided by the botfather for specifying in which bot we are adding the functionalities
from telegram.ext.updater import Updater       
# For responding to the command/message give by the user    
from telegram.update import Update
# to call a specific function to execute the output
from telegram.ext.callbackcontext import CallbackContext
# use to handle commands and the commands should be in the format (/Command)
from telegram.ext.commandhandler import CommandHandler  
# To handle the normal message
from telegram.ext.messagehandler import MessageHandler       
# To differentiate between commands,messages,etc.
from telegram.ext.filters import Filters
import os
import telegram
import requests
import re



# Creating an instance for Updater with API KEY OF TELEGRAM BOT
updater = Updater(
    "5131911803:AAEKmeHzscj4qZ0MJdiMQ6fd58QTbhM6g8k", use_context=True)

# All commands Operations functions


    
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
    '''Hello!! 
We are the students of  Artificial Intelligence and Data Science(FY) from Vishwakarma Institute of Information Technology, Pune.
ADMINS:-1. Rupam Patil
                  2. Pranav Wagholikar 
                  3. Pratik Nule
                  4. Rashmi Sontakke
                  5. Shoaib Ahmed 
We have created this bot to make notes accessible in the easiest way possible
Enter /help to check the available commands''')


def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
	/PE_ - To get PE notes
	/BXE_ - To get BXE notes
	/Chemistry_ - To get Chemistry notes
	/Maths_- To get Maths notes
/PE_classwork - To get all the codes in one notebook
/For_more_material - To get the youtube links and websites of specific subject
/For_more_details - To get the contacts of the admin 
/Sem_1_papers - To get the Sem-1 papers
/get_fees - To get the fees
/fees - To know the exact college fees""")   
#shoaib  

def For_more_details(update: Update, context: CallbackContext):
    update.message.reply_text('''
                 Contacts:       1) Rupam Patil 
                              Email ID - rupam.22110203@viit.ac.in
                              LinkedIn - https://www.linkedin.com/in/rupam-patil-470848223/
                              
                           2) Pranav Wagholikar 
                              Email ID - pranav.22110262@viit.ac.in
                              LinkedIn - https://www.linkedin.com/in/pranav-wagholikar-010b7822a 
                            
                           3) Pratik Nule
                              Email ID - pratik.22110235@viit.ac.in
                              LinkedIn - https://www.linkedin.com/in/pratik-nule-6aa3aa22a/
                              
                           4) Rashmi Sontakke 
                              Email Id - rashmi.22110087@viit.ac.in
                              LinkedIn - https://www.linkedin.com/in/rashmi-sontakke-b3162a229
                              
                           5) Shoaib Ahmed 
                              Email Id - Shoaib.22110347@viit.ac.in
                              LinkedIn - https://www.linkedin.com/in/shoaib-ahmed-3a3615232''') 
  
    update.message.reply_text(
        '''Available Commands :-
	/PE_ - To get PE notes
	/BXE_ - To get BXE notes
	/Chemistry_ - To get Chemistry notes
	/Maths_- To get Maths notes
/PE_classwork - To get all the codes in one notebook
/For_more_material - To get the youtube links and websites of specific subject
/For_more_details - To get the contacts of the admin 
/Sem_1_papers - To get the Sem-1 papers''')                        

def PE_classwork(update: Update, context: CallbackContext):
    update.message.reply_text(
        ' Please wait.., \n https://colab.research.google.com/drive/1fUrwsQ5yKM4HfKBOi7IoAHTAcaoRwl9F')



    update.message.reply_text(
        '''Available Commands :-
	/PE_ - To get PE notes
	/BXE_ - To get BXE notes
	/Chemistry_ - To get Chemistry notes
	/Maths_- To get Maths notes
/PE_classwork - To get all the codes in one notebook
/For_more_material - To get the youtube links and websites of specific subject
/For_more_details - To get the contacts of the admin 
/Sem_1_papers - To get the Sem-1 papers''')  
#pratik


def PE_(update: Update, context: CallbackContext):
    update.message.reply_text(
        '''Your file is downloading, Please wait...''')
    
    i=1
    os.chdir("notes")  #to go from currect directory to the folder's directory

    while i < 50:
        try:        #if an error occurs in line 2 then it will move to the except block
            context.bot.sendDocument(update.effective_chat.id, document=open("Python-"+ str(i) + ".pdf","rb"))
            i+=1
        except:
            i+=1
            continue

# rb = we can only read  the file but can't edit the file
        
    os.chdir("..")     #to return to previous directory
    
    update.message.reply_text(
        '''Available Commands :-
	/PE_ - To get PE notes
	/BXE_ - To get BXE notes
	/Chemistry_ - To get Chemistry notes
	/Maths_- To get Maths notes
/PE_classwork - To get all the codes in one notebook
/For_more_material - To get the youtube links and websites of specific subject
/For_more_details - To get the contacts of the admin 
/Sem_1_papers - To get the Sem-1 papers''')

'''rb-Opens the file as read-only in binary format and 
starts reading from the beginning of the file. While binary
 format can be used for different purposes, it is usually
  used when dealing with things like images, videos, etc'''

def PE_Assignments(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Your file is downloading, Please wait..")
    
    i=1
    os.chdir("notes")  #to go from currect directory to the folder's directory

    while i < 50:
        try:        #if an error occurs in line 2 then it will move to the except block
            context.bot.sendDocument(update.effective_chat.id, document=open("PE_Assignments-"+ str(i) + ".pdf","rb"))
            i+=1
        except:
            i+=1
            continue
        
    os.chdir("..")

    update.message.reply_text(
        '''Available Commands :-
	/PE_ - To get PE notes
	/BXE_ - To get BXE notes
	/Chemistry_ - To get Chemistry notes
	/Maths_- To get Maths notes
/PE_classwork - To get all the codes in one notebook
/For_more_material - To get the youtube links and websites of specific subject
/For_more_details - To get the contacts of the admin 
/Sem_1_papers - To get the Sem-1 papers''')
    


def BXE_(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Your file is downloading, Please wait..")
    i=1
    os.chdir("notes")  #to go from currect directory to the folder's directory

    while i < 50:
        try:        #if an error occurs in line 2 then it will move to the except block
            context.bot.sendDocument(update.effective_chat.id, document=open("BXE-"+ str(i) + ".pdf","rb"))
            i+=1
        except:
            i+=1
            continue
        
    os.chdir("..") 

    update.message.reply_text(
        '''Available Commands :-
	/PE_ - To get PE notes
	/BXE_ - To get BXE notes
	/Chemistry_ - To get Chemistry notes
	/Maths_- To get Maths notes
/PE_classwork - To get all the codes in one notebook
/For_more_material - To get the youtube links and websites of specific subject
/For_more_details - To get the contacts of the admin 
/Sem_1_papers - To get the Sem-1 papers''')


def Chemistry_(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Your file is downloading, Please wait..")
    i=1
    os.chdir("notes")  #to go from currect directory to the folder's directory

    while i < 50:
        try:        #if an error occurs in line 2 then it will move to the except block
            context.bot.sendDocument(update.effective_chat.id, document=open("Chemistry-"+ str(i) + ".pdf","rb"))
            i+=1
        except:
            i+=1
            continue
        
    os.chdir("..") 


    update.message.reply_text(
        '''Available Commands :-
	/PE_ - To get PE notes
	/BXE_ - To get BXE notes
	/Chemistry_ - To get Chemistry notes
	/Maths_- To get Maths notes
/PE_classwork - To get all the codes in one notebook
/For_more_material - To get the youtube links and websites of specific subject
/For_more_details - To get the contacts of the admin 
/Sem_1_papers - To get the Sem-1 papers''')


   

def Maths_(update: Update, context: CallbackContext):
    update.message.reply_text("Your file is downloading, Please wait..")
    i=1
    os.chdir("notes")

    while i < 50:
        try:        
            context.bot.sendDocument(update.effective_chat.id, document=open("Maths-"+ str(i) + ".pdf","rb"))
            i+=1
        except:
            i+=1
            continue
        
    os.chdir("..")


    update.message.reply_text(
        '''Available Commands :-
	/PE_ - To get PE notes
	/BXE_ - To get BXE notes
	/Chemistry_ - To get Chemistry notes
	/Maths_- To get Maths notes
/PE_classwork - To get all the codes in one notebook
/For_more_material - To get the youtube links and websites of specific subject
/For_more_details - To get the contacts of the admin 
/Sem_1_papers - To get the Sem-1 papers''')
 #rupam 


def Sem_1_papers(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Your file is downloading, Please wait..")
    
    i=1
    os.chdir("Sem-1 papers")  #to go from currect directory to the folder's directory

    while i < 50:
        try:        #if an error occurs in line 2 then it will move to the except block
            context.bot.sendDocument(update.effective_chat.id, document=open("Paper_module-"+ str(i) + ".pdf","rb"))
            i+=1
        except:
            i+=1
            continue
        
    os.chdir("..")

    update.message.reply_text(
        '''Available Commands :-
	/PE_ - To get PE notes
	/BXE_ - To get BXE notes
	/Chemistry_ - To get Chemistry notes
	/Maths_- To get Maths notes
/PE_classwork - To get all the codes in one notebook
/For_more_material - To get the youtube links and websites of specific subject
/For_more_details - To get the contacts of the admin 
/Sem_1_papers - To get the Sem-1 papers''')

def For_more_material(update: Update, context: CallbackContext):
    update.message.reply_text(
    '''Please wait...
🌟 Learn Python Here : 

1. W3schools.com
2. Freecodecamp.org
3. geeksforgeeks.org
4. udacity.com
5. udemy.com
6. codeacademy.com
7. coursera.org
8. edx.org
9. youtube.com

🌟 Practice Python Here : 

1. codewars.com
2. hackerrank.com
3. topcoder.com
4. coderbyte.com
5. hackerearth.com
6. leetcode.com
7. codechef.com
8. edabit.com
9. codeforces.com

🌟 Ask Python Questions here :

1. stackoverflow.com
2. quora.com
3. github.com
4. reddit.com


🌟 Some of the youtube channels:
1. Code with Harry
2. Telusko
3. Great learning
4. Edureka
5. Apni Kaksha
6. Love babbar
7. Programming with Mosh
8. DevTips
9. Hitesh choudhary
10. the new boston

Some playlist :
https://youtube.com/playlist?list=PLAE85DE8440AA6B83

https://youtube.com/playlist?list=PLu0W_9lII9aiXlHcLx-mDH1Qul38wD3aR

https://youtube.com/playlist?list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3

https://youtube.com/playlist?list=PLsyeobzWxl7oBxHp43xQTFrw9f1CDPR6C

https://youtube.com/playlist?list=PLsyeobzWxl7qXgEySfUYucoqKCnL9y2sA''')


    update.message.reply_text(
        '''Available Commands :-
	/PE_ - To get PE notes
	/BXE_ - To get BXE notes
	/Chemistry_ - To get Chemistry notes
	/Maths_- To get Maths notes
/PE_classwork - To get all the codes in one notebook
/For_more_material - To get the youtube links and websites of specific subject
/For_more_details - To get the contacts of the admin 
/Sem_1_papers - To get the Sem-1 papers''')


def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        '''Sorry '%s' is not a valid command \n
 Available Commands :-
	/PE_ - To get PE chapter 1 notes
	/BXE_ - To get BXE chapter 1 notes
	/Chemistry_ - To get Chemistry chapter 1 notes
	/Maths_- To get Maths chapter 1 notes
/PE_classwork - To get all the codes in one notebook
/For_more_material - To get the youtube links and websites of specific subject
/For_more_details - To get the contacts of the admin 
/Sem_1_papers - To get the Sem-1 papers''' % update.message.text)


def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        '''Sorry I can't recognize you , you said '%s'" \n
Available Commands :-
	/PE_ - To get PE chapter 1 notes
	/BXE_ - To get BXE chapter 1 notes
	/Chemistry_ - To get Chemistry chapter 1 notes
	/Maths_- To get Maths chapter 1 notes
/PE_classwork - To get all the codes in one notebook
/For_more_material - To get the youtube links and websites of specific subject
/For_more_details - To get the contacts of the admin 
/Sem_1_papers - To get the Sem-1 papers'''% update.message.text)
#rashmi

    










import requests

def fees(update: Update, context: CallbackContext):
    update.message.reply_text('''Enter the college name''')
 

  # Get the college name from the user.
    college_name = update.message.text
    # Convert the college name to lower case and replace spaces with hyphens.
    college_name_lower = re.sub(r" ", "-", college_name.lower())

  # Get the fees of the college from the website.
    response = requests.get
    fees = response.json()["college_details"]["fees"]

    # Get the specific parameters from the fees dictionary.
    specific_parameters = [
    "Total Fees"
  ]

  # Create a dictionary to store the specific parameters.
    specific_fees = {}
    for parameter in specific_parameters:
        specific_fees[parameter] = fees[parameter]

  # Send the specific fees to the user.
    context.bot.send_message(update.effective_chat.id, specific_fees)












# calling the function on specific commands
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('PE_', PE_))
updater.dispatcher.add_handler(CommandHandler('BXE_', BXE_))
updater.dispatcher.add_handler(CommandHandler('Chemistry_', Chemistry_))
updater.dispatcher.add_handler(CommandHandler('Maths_', Maths_))
updater.dispatcher.add_handler(CommandHandler('For_more_material', For_more_material))
updater.dispatcher.add_handler(CommandHandler('PE_classwork', PE_classwork))
updater.dispatcher.add_handler(CommandHandler('For_more_details',For_more_details))
updater.dispatcher.add_handler(CommandHandler('PE_Assignments', PE_Assignments))
updater.dispatcher.add_handler(CommandHandler('Sem_1_papers',Sem_1_papers ))

updater.dispatcher.add_handler(CommandHandler('fees',fees ))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))  # Filters out unknown commands
#pranav


# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
#rupam

'''Polling is a powerful python utility used to wait for a 
function to return a certain expected condition. Some possible uses cases include:

Wait for API response to return with code 200
Wait for a file to exist (or not exist)
Wait for a thread lock on a resource to expire'''