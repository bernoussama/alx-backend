#!/usr/bin/env python3
"""Basic Flask app with i18n and timezone support."""
import pytz
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """Configures supported languages and defaults."""

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


def get_user():
    """Return user by login ID, if provided."""
    user_id = request.args.get("login_as")
    return users.get(int(user_id)) if user_id else None


@app.before_request
def before_request():
    """Set the user for the current request."""
    g.user = get_user()


@babel.localeselector
def get_locale():
    """Return best-matching locale for request."""
    return (
        request.args.get("locale")
        or (g.user and g.user.get("locale"))
        or request.headers.get("locale")
        or request.accept_languages.best_match(app.config["LANGUAGES"])
    )


@babel.timezoneselector
def get_timezone():
    """Return best-matching timezone for request."""
    tz = request.args.get("timezone") or (g.user and g.user.get("timezone"))
    try:
        return (
            pytz.timezone(tz).zone
            if tz
            else app.config["BABEL_DEFAULT_TIMEZONE"]
        )
    except pytz.UnknownTimeZoneError:
        return app.config["BABEL_DEFAULT_TIMEZONE"]


@app.route("/")
def index():
    """Render the home page."""
    return render_template("7-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
