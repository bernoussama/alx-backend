#!/usr/bin/env python3
"""A Basic Flask app with internationalization support."""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Optional


class Config:
    """Configuration for supported languages and defaults."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Optional[dict]:
    """Retrieve a user based on the login ID."""
    user_id = request.args.get("login_as")
    return users.get(int(user_id)) if user_id else None


@app.before_request
def before_request() -> None:
    """Set the user for the current request context."""
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """Determine the best match locale for the current request."""
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale
    if g.user and g.user.get("locale") in app.config["LANGUAGES"]:
        return g.user["locale"]
    header_locale = request.headers.get("locale")
    if header_locale in app.config["LANGUAGES"]:
        return header_locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index() -> str:
    """Render the home/index page."""
    return render_template("6-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
