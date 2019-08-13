'''
Flask model to display file contents
'''

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index() -> str:
    return render_template('index.html', title='My Working Title', joke='Bonjour, tout les monde')

# end index


@app.route("/file")
def show_file() -> str:

    with open("showable.txt") as file:
        lines = [line for line in file]
    #end with

    return render_template('file_contents.html', lines=lines)

# end show_file
