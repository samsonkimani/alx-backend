#!/usr/bin/env python3

"""
creating a flask app
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    """ an endpoint to the index page"""
    return render_template('0-index.html')
