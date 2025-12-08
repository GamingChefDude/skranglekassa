# app_core.py
from flask import Flask

app = Flask(
    __name__,
    template_folder='../SRC/HTML/',
    static_folder='../SRC/'
)

loggedIn = False
