from flask import Flask

from src.views import link_blueprint


app = Flask(__name__)

app.config.from_object("config")

app.register_blueprint(link_blueprint, url_prefix="/shortlinks")


from src import database