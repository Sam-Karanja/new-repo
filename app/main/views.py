from flask import render_template
from.import main
from..request import get_quotes

# Views


@main.route('/',methods=['GET'])
def index():

    '''
    View root page function that returns the index page and its data
    '''
    my_quote=get_quotes()

    message ="Quote for you. You are the best and nobody can change that"
    return render_template('index.html',message=message,quotes=my_quote)

