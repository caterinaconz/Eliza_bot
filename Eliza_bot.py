

import ast  #This module will be used to import the set of patterns and respones as a dictionary from a .txt file.
import re  #This module will be used to check if the string typed by the user matches one of the specified patterns.
import random #This module will be used to randomly choose one of the possible responses to each matched pattern.
# import time  #This module will be used to simulate the bot typing an answer and to solicit the user to type a message, if he has not written anything for a while.

#As soon as the program is run, it imports the set of patterns and responses that the bot will have to use from a .txt file.
#The content of the .txt file is read and stored as "dictionary_contents". However, it is a string, unusable for the bot in this form.
#Hence, it is used as argument of the function "ast.literal_eval" to compile the dictionary "phrases", which the bot is able to use properly.
bot_dictionary = open ("/Users/Cate/PycharmProjects/PProjectIII/responses_dict.txt", "r")
dictionary_contents = bot_dictionary.read()
phrases = ast.literal_eval(dictionary_contents)
bot_dictionary.close()

#This dictionary is used in the function "swap" to invert subject and object of the user's message.
#Additionally, it is used by the function "swap" to transform some abbreviations used by the user into an extended form, in the attempt to make the bot maintain a more formal language.
change_subject = {
    "i": "you",
    "you": "I",
    "me": "you",
    "am": "are",
    "are": "am",
    "was": "were",
    "were": "was",
    "my": "your",
    "your": "my",
    "mine": "yours",
    "yours": "mine",
    "myself": "yourself",
    "yourself": "myself",
    "he is": "he is", #it is necessary to prevent the swap of is/was with was/were in the case of a third singular person
    "he was": "he was",
    "she is": "she is",
    "she was": "she was",
    "it is": "it is",
    "it was": "it was",
    "we": "you",
    "us": "you",
    "we are": "you are", #it is necessary to prevent the swap of are/were with is/was in the case of a first plural person
    "we were": "you were",
    "our": "your",
    "ours": "yours",
    "ourself": "yourselves",
    "they are": "they are", #it is necessary to prevent the swap of are/were with is/was in the case of a third plural person
    "they were": "they were",
    "i'm": "you are", #to maintain a formal language, any abbreviation used by the user is turned into an extended form in the bot's reply
    "i'd": "you would",
    "i've": "you have",
    "I'll": "you will",
    "you'd": "I would",
    "you've": "I have",
    "you'll": "I will",
    "he's": "he is",
    "he'd": "he would",
    "he'll": "he will",
    "she's": "she is",
    "she'd": "she would",
    "she'll": "she will",
    "we'd": "you would",
    "we've": "you have",
    "we'll": "you will",
    "they're": "they are",
    "they've": "they have",
    "they'd": "they would",
    "they'll": "they will"
}

#The function uses the dictionary "phrases" (compiled using the content of a .txt file), to check if the user's message matches a pattern and to compile an adeguate reply.
#To do so, the function first calls the method ".rstrip" on the user's statement, to remove any full stop or exclamation mark at the end of the statement.
#Then, it uses the function "re.match" to look for a match between the user's statement and a pattern (a key) from the dictionary "phrases".
#If a match is found, the bot's response is chosen at random (through the function "random.choice") between the values that match the pattern in the dictionary. The bot's response is stored as "reply".
#In the end, if the response randomly chosen as "reply" contains one or more blanks (denoted by {number}), those need to be filled with fragments extracted from the users message.
#Indeed, any part of the user's message which corresponds to a (.*) in the matched pattern is numbered, modified by the function "swap" and used to fill any blank denoted by the same number.

def analyze(statement):
    for pattern, responses in phrases:
        match = re.match(pattern, statement.rstrip(".!").capitalize())
        if match:
            reply = random.choice(responses)
            return reply.format(*[swap(g) for g in match.groups()])

# randomised responses -> replies to one single question at a time,
# does not store a history of the chat -> answers do not depend from previous ones
# A possible implementation would be to store messages (in a database) and train to bot to
# build replies depending on the previous ones

#This function uses the dictionary "change_subject" to invert subject and object of the fragment extracted from the user's message and to turn abbreviations used by the user into an extended form, in the attempt to make the bot maintain a more formal language (i.e. "I'm" becomes "you are").
#The function achieves this by first splitting the user's message into single, lowercase words (stored in "tokens"), and then checking if any of them matches one of the keys in the dictionary.
#If a match is found, the word in tokens is replaced by the corresponding value in the dictionary.
#In the end, the "tokens" are joined again to form a string that can possibly be inserted in a "reply" by the function "analyze".
def swap(fragment):
    tokens = fragment.lower().split()
    for word, pronoun in enumerate(tokens):
        if pronoun in change_subject:
            tokens[word] = change_subject[pronoun]
    return " ".join(tokens)


#########
#def do_POST(statement):
 #   self.send_response(200)
 #   content_lenght = int(self.headers['Content-Lenght'])
  #  post_body = self.rfile.read(content_lenght)
   # self.end_headers()
    #print('user query', post_body)
    #get_bot_response =

########



#This function first prints one initial greeting message from the bot to the user and then creates a while loop.
#Inside the while loop, first
def main():
    print ("Hello!")
    while True:
        statement = input("> ")
        print (analyze(statement))
        if statement == "quit":
            break


#main()







