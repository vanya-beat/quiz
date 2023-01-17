from app import app, babel
from app.config import LANGUAGES
from flask_babel import gettext, _
from flask import request, render_template


@babel.localeselector
def get_locale():
    # Basic method, can be used as a fallback if a user's profile does not specify a language,
    # or a user hasn't yet registered.
    result = request.accept_languages.best_match(LANGUAGES.keys())

    # # will return language code (en/es/etc).
    return 'en'
    # return result


menu = ["Установка", "Первое приложение", "Обратная связь"]

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html',
                           title=_('Please translate me, I am a message or some stuff!'), menu=menu)


@app.route("/about")
def about():
    return render_template('about.html')
