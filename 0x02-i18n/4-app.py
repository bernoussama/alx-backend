#!/usr/bin/env python3
"""basic flask app with Babel configuration, locale selector, and URL locale support"""
from flask import Flask, render_template, request
from flask_babel import Babel


# Define configuration class
class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Create the Flask app instance
app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False

# Initialize Babel with the app
babel = Babel(app)


# Locale selector function
@babel.localeselector
def get_locale():
    """Determine the best match for supported languages."""
    # Check if 'locale' is in request arguments
    locale = request.args.get("locale")
    # check if its supported
    if locale in app.config["LANGUAGES"]:
        return locale
    # Fall back to the best match from request headers
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index():
    """index page"""
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
