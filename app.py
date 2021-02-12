

from flask import Flask, render_template, request # import render library and request library

app = Flask(__name__)  # we are creating a web app whose name is our current module's name

# Filters will reduce the number of statements that a chat bot has to process when it is selecting a response.

from Eliza_bot import analyze
#from Eliza_bot import swap


@app.route("/")
# this syntax that goes before the function definition is what is called a decorater, it
# indicates the route, which file I want to open
# the input argument it takes is what is called a url rule, which is basically like a pattern
# the incoming request's url has to match in order to trigger the function we defined for the route to take
# @app.route('file:///Users/Cate/PycharmProjects/pythonProject/index.html')
# In case the path is just /, this function will e
# I used slash as I do not have any template, and I just want to print the phrase
# the url ('/') is associated with the 'home()' function. The output of that function will be rendered
# on the browser's screen and in our case it will be the string that will be the body
# # of my HTTP response, the 'index.html' , namely the html of th page.
def home():
    return render_template("index.html") # my frontend
# this and the following functions, are functions I am telling the decorator
# @app.route() to call at some point , during the execution of internal commands
# whenever I hit the home page, this piece of code will run
# render function: fct that takes data out from a database
# each function is going to be triggered depending on which action the user is doing on the site.

@app.route("/get")
def get_bot_response():
    try:
        return str(analyze(request.args.get('msg')))
    except Exception as e:
        print("Error", e)
        return str("I didn't get you")


if __name__ == '__main__':           # if the name is main, then app.run
    app.run(debug=False, host='0.0.0.0', port=3000)   # 0.0... -> local host / 3000 -> multiple ports
# the "main" file that is run, in our case app.py, will have its file name internally replaced
# with "__main__" before it is interpreted. Therefore, if we run the file with this piece of code as
# our main file, the code inside the conditional statement "__name__== "__main__" will be executed.
# Consequently, app.run() will be executed.

# Tipically, Flask looks for a static folder, for serving up static assets like
# css and html pages that don't ever change and templates folder for templates
# that typically have placeholders that are to be filled in by data coming from the
# server
