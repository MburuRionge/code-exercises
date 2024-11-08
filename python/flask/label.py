from flask import Flask, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)

#define supported locales
SUPPORTED_LOCALES = ['en', 'fr']

@babel.localeselector
def get_locale():
    #get locale from the request arguments
    requested_locale = request.args.get('locale')

    #check if the requested locale is supported
    if requested_locale in SUPPORTED_LOCALES:
        return requested_locale
    
    #fallback to default behaviour english
    return 'en'