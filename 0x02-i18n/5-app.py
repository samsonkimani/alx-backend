#!/usr/bin/env python3

"""
creating a flask app
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """ config class to set babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

@babel.localeselector
def get_locale():
    """ getting the locale best match languages"""
    locale = request.args.get("locale")

    if locale and locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])

def get_user():
    get_id = request.args.get("login_as")

    if get_id and get_id in users:
        return users.get(int(login_id))
    else:
        return None

@app.before_request
def before_request():
    user = get_user()
    g.user = user

@app.route("/")
def home():
    """ an endpoint to the index page"""
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run()
