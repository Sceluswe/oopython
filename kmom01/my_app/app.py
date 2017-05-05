#!/usr/bin/env python3
"""
My first Flask app
"""
# Importera relevanta moduler
# from flask import Flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    """ Main route """
    return render_template("index.html")

@app.route("/about/")
def about():
    """ About route """
    return render_template("about.html")

if __name__ == "__main__":
    app.run()
