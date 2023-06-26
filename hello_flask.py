# importing two methods from flask, "Flask" and "render_template"
from flask import Flask, render_template
My_app = Flask(__name__) # creates the Flask instance.
#__name__ is the name of the current Python module. 
# #The app needs to know where it’s located to set up some paths, and __name__ is a convenient way to tell it that.

@My_app.route("/")
def index():
    '''
    Displays the index page accessible at '/'
    '''
    return render_template('index.html')

@My_app.route("/other")
def other():
    '''
    Displays the index page accessible at '/'
    '''
    return render_template('other_page.html')
    
@My_app.route("/home")
def home():
    return render_template('home.html')

if __name__=='__main__':
    My_app.debug = True
    My_app.run()